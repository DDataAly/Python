from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class myHandler(BaseHTTPRequestHandler):
    storage = {}

    def do_GET(self):
        print(f"this is the path {self.path}")
        url = self.path
        parsed_url = urlparse (url)
        url_query_dict=parse_qs(parsed_url.query)


        if self.path.startswith('/set'):
            new_storage_item={k:v[0] for k,v in url_query_dict.items()}
            print(f'This is new pair to store {new_storage_item}')
            self.storage.update(new_storage_item)
            print(f'This is what the storage contains: {self.storage}')

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'The pair {new_storage_item} was added to the storage'.encode())


        if self.path.startswith('/get'):
            item_to_fetch_key = url_query_dict['key'][0]
            item_to_fetch_value = self.storage[item_to_fetch_key]  

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(item_to_fetch_value.encode())

with HTTPServer(('127.0.0.1', 4000), myHandler) as server:
    server.serve_forever()     





