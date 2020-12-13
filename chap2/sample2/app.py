import random
from flask import Flask, render_template, request, session, url_for, redirect
from flask.views import MethodView

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    n = random.randrange(5, 10)
    data = []
    for n in range(n):
        data.append(random.randrange(0, 100))
    title = 'Template sample'
    msg = 'This is Sample Page.'
    return render_template(
        'index.html',
        title=title,
        message=msg,
        data=data
    )


@app.route('/next', methods=['GET'])
def next():
    title = 'Next page'
    msg = 'This is Next Page.'
    data = ['One', 'Two', 'Three']
    return render_template(
        'next.html',
        title=title,
        message=msg,
        data=data
    )


@app.template_filter('sum')
def sum_filter(data):
    total = 0
    for item in data:
        total += item
    return total


app.jinja_env.filters['sum'] = sum_filter


@app.context_processor
def sample_processor():
    def total(n):
        total = 0
        for i in range(n + 1):
            total += i
        return total
    return dict(total=total)


app.secret_key = b'random string...'


class HelloAPI(MethodView):
    def get(self):
        if 'send' in session:
            msg = f'send: {session["send"]}'
            send = session['send']
        else:
            msg = 'なにか書いてください'
            send = ''
        title = 'Next page'
        return render_template(
            'next.html',
            title=title,
            message=msg,
            send=send
        )

    def post(self):
        session['send'] = request.form.get('send')
        return redirect('/hello/')


app.add_url_rule('/hello/', view_func=HelloAPI.as_view('hello'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
