from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    title = 'Form Sample'
    message = '選択してください'
    return render_template('index.html',
                           title=title,
                           message=message
                           )


@app.route('/<id>/<password>')
def index_query(id, password):
    title = 'Index with Jinja'
    msg = f'id: {id} password: {password}'
    return render_template('index.html',
                           title=title,
                           message=msg
                           )


@app.route('/', methods=['POST'])
def form():
    # field = request.form['field']
    ck = request.form.get('check')
    rd = request.form.get('radio')
    sel = request.form.getlist('sel')
    return render_template(
        'index.html',
        title='Form sample',
        message=[ck, rd, sel]
    )


@app.route('/index2', methods=['GET'])
def index2():
    flg = True
    return render_template(
        'index2.html',
        title='Template sample',
        message='This is Jinja template sample.',
        flg=flg
    )


@app.route('/index3', methods=['GET'])
def index3():
    data = [
        'Windows',
        'macOS',
        'Linux',
        'ChromeOS'
    ]
    return render_template(
        'index3.html',
        title='Form sample',
        message=data,
        data=data
    )


@app.route('/index4', methods=['GET'])
def index4():
    return render_template(
        'index4.html',
        title='Template sample',
        message='<a href="/">go to top page</a>'
    )


@app.route('/index5', methods=['GET'])
def index5():
    return render_template(
        'index5.html',
        title='Template sample',
        message='※メッセージがあります.'
    )


@app.route('/index6', methods=['GET'])
def index6():
    data = [
        'One',
        'Two',
        'Three'
    ]
    person = {
        'name': 'Taro',
        'mail': 'taro@yamada'
    }
    return render_template(
        'index6.html',
        title='Template sample',
        message='This is sample message',
        data=data,
        person=person
    )


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
