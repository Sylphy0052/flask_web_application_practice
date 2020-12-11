from http.server import BaseHTTPRequestHandler, HTTPServer


with open('index.html', mode='r') as f:
    index = f.read()


class HelloServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        html = index.format(
            title='Hello',
            message='ようこそ、HTTPServerの世界へ!！'
            )
        self.wfile.write(html.encode('utf-8'))
        return


HTTPServer(('', 8000), HelloServerHandler).serve_forever()
