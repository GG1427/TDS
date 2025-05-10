from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
		response_body = "Guess who's back"
		
        if path.startswith("/api?"):
            query_string = path.split("?", 1)[1]
            params = {}

            # Manual parsing of query string
            for pair in query_string.split("&"):
                key, value = pair.split("=")
                if key in params:
                    params[key].append(value)
                else:
                    params[key] = [value]

            response_body = str(params)
            
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_body.encode())
        
       return
