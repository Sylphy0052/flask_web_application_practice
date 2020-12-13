from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = b'random string...'

member_datas = {}
message_datas = []


@app.route('/', methods=['GET'])
def index():
    if 'login' in session and session['login']:
        title = 'Messages'
        msg = f'Login id: {session["id"]}'
        return render_template(
            'messages.html',
            title=title,
            message=msg,
            data=message_datas
        )
    else:
        return redirect('/login')


@app.route('/', methods=['POST'])
def form():
    global message_datas
    msg = request.form.get('content')
    message_datas.append((session['id'], msg))
    if len(message_datas) > 25:
        message_datas.pop(0)
    return redirect('/')


@app.route('/login', methods=['GET'])
def login():
    title = 'Login'
    msg = 'IDとパスワードを入力:'
    return render_template(
        'login.html',
        title=title,
        err=False,
        message=msg,
        id=''
    )


@app.route('/login', methods=['POST'])
def login_post():
    global member_datas
    idx = request.form.get('id')
    password = request.form.get('pass')
    if idx in member_datas:
        if password == member_datas[idx]:
            session['login'] = True
        else:
            session['login'] = False
    else:
        member_datas[idx] = password
        session['login'] = True
    session['id'] = idx
    if session['login']:
        return redirect('/')
    else:
        title = 'Login'
        msg = 'パスワードが違います'
        return render_template(
            'login.html',
            title=title,
            err=False,
            message=msg,
            id=idx
        )


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('id', None)
    session.pop('login')
    return redirect('/login')


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
