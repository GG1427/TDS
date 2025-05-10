from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        response_body = "Guess who's back"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_body.encode())
