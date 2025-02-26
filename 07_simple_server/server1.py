from http.server import BaseHTTPRequestHandler
import socketserver 
from urllib.parse import urlparse


class myHandler(BaseHTTPRequestHandler):
    storage = {}

    def do_GET(self):
        url = self.path
        parsed_url = urlparse (url)
        # print(key_value_dict)

        if self.path == '/set':
            key_value_dict = {parsed_url.query.split('=')[0]:parsed_url.query.split('=')[1]}
            self.storage.update(key_value_dict)
            # print(f'New key-value pair {key_value_dict} was added to the dictionary')

        if self.path == '/get':
            key_requested = parsed_url.query.split('=')[0]
            value_requested = self.storage[key_requested]    
            # print(f'The requested value is {value_requested}')

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(value_requested.encode())

PORT = 4000
with socketserver.TCPServer(("", PORT), myHandler) as httpd:
    httpd.serve_forever()        







