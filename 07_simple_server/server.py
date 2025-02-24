import http.server
class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pass

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        



