from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from cgi import FieldStorage

with open('index.html', mode='r') as f:
    index = f.read()
with open('next.html', mode='r') as f:
    next = f.read()


routes = []


def route(path, method):
    routes.append((path, method))


route('/', 'index')
route('/index', 'index')
route('/next', 'next')
route('/xml', 'xml')


class HelloServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global routes
        _url = urlparse(self.path)
        for r in routes:
            if (r[0] == _url.path):
                eval(f'self.{r[1]}()')
                break
        else:
            self.error()
        return

    def do_POST(self):
        form = FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        res = form['textfield'].value
        self.send_response(200)
        self.end_headers()
        html = next.format(
            message=f'you typed: {res}',
            data=form
        )
        self.wfile.write(html.encode('utf-8'))
        return

    def index(self):
        # _url = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        html = index.format(
            title='Hello',
            message='Form送信'
            # message='ようこそ、HTTPServerの世界へ!！',
            # link=f'/next?{_url.query}'
        )
        self.wfile.write(html.encode('utf-8'))
        return

    def next(self):
        # _url = urlparse(self.path)
        # query = parse_qs(_url.query)
        # id = query['id'][0]
        # password = query['pass'][0]
        # msg = f'id={id}, password={password}'
        self.send_response(200)
        self.end_headers()
        # html = next.format(
        #     message=msg,
        #     data=query
        # )
        html = next.format(
            message='header data.',
            data=self.headers
        )
        self.wfile.write(html.encode('utf-8'))
        return

    def xml(self):
        xml = '''<?xml version="1.0" encoding="utf-8"?>
        <data>
        <person>
        <name>Taro</name>
        <mail>taro@yamada</mail>
        <age>39</age>
        </person>
        <message>Hello Python!!</message>
        </data>'''
        self.send_response(200)
        self.send_header('Content-Type',
                         'application/xml; charset=utf-8')
        self.end_headers()
        self.wfile.write(xml.encode('utf-8'))

    def error(self):
        self.send_error(404, "Cannot Access!!")
        return


HTTPServer(('', 8000), HelloServerHandler).serve_forever()
