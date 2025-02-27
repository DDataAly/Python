from http.server import HTTPServer, BaseHTTPRequestHandler 
from urllib.parse import parse_qs, urlparse

# Creating a class for processing GET and POST requests
class myHandler(BaseHTTPRequestHandler):
    storage = {}


    def do_GET(self):
        url = self.path
        parsed_url= urlparse(url)
        key_value_parsed_url = parse_qs(parsed_url.query)

        if parsed_url.path == '/get':
            self.storage = { k: v[0] for k, v in key_value_parsed_url.items()}
            print(f'This is in the storage {self.storage}')

        if parsed_url.path == '/set':
            requested_dict =  { k: v[0] for k, v in key_value_parsed_url.items()}
            print(f'This is what we have in the GET request: {requested_dict}')
            requested_key = requested_dict.get('key')
            i=requested_key[0]
            print(f'This is the key I want to look for in the storage: {i}')
            requested_value = self.storage.get(i)
            print(f'And this is what I got in return: {requested_value}')

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(requested_value.encode())

# Setting up a server 
# Using with statement to manage resources automatically when closing the program
with HTTPServer(('127.0.0.1', 4000), myHandler) as server:
    server.serve_forever()


# Drafts - trying to figure out the dictionary logic bit        
# storage = {}

# url = 'http://localhost:4000/set?somekey=somevalue'
# u = urlparse(url)
# u1 = parse_qs(u.query)

# storage = {
#     k: v[0] if len(v) == 1 else v 
#     for k, v in u1.items()
# }
# print(f'This is in the storage {storage}')


# url = 'http://localhost:4000/get?key=somekey'
# parsed_url = urlparse(url)
# key_value_pair =  parse_qs(parsed_url.query)

# requested_dict = {
#     k: v[0] if len(v) == 1 else v 
#     for k, v in key_value_pair.items()
# }

# print(f'This is what we have in the GET request: {requested_dict}')

# requested_key = key_value_pair.get('key')
# i=requested_key[0]
# print(f'This is the key I want to look for in the storage: {i}')

# requested_value = storage.get(i)
# print(f'And this is what I got in return: {requested_value}')

