from flask import Flask, render_template, request, session, url_for, redirect


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    title = 'Index'
    msg = 'This is Bootstrap sample'
    return render_template(
        'index.html',
        title=title,
        message=msg
    )


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
