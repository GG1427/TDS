from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        response_body = "Guess who's back"

        if path.startswith("/api"):
            params = {}
            if "?" in path:
                query_string = path.split("?", 1)[1]

                for pair in query_string.split("&"):
                    if "=" in pair:
                        key, value = pair.split("=", 1)
                        if key in params:
                            params[key].append(value)
                        else:
                            params[key] = [value]

                response_body = str(params)
            else:
                response_body = "No query parameters provided"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_body.encode())
