from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        with open('login.html', 'rb') as f:
            self.wfile.write(f.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)
        
        user = params.get('user', [''])[0]
        password = params.get('pass', [''])[0]
        
        self.send_response(200)
        self.end_headers()
        
        if user == 'admin' and password == 'secret':
            self.wfile.write(b"SUCCESS")
        else:
            self.wfile.write(b"FAIL")

print("Server started on port 8080")
HTTPServer(('127.0.0.1', 8080), RequestHandler).serve_forever()
