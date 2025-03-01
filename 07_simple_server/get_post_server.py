# Start the program is VSC
# Send a post request in the shell: curl -X POST "http://localhost:4000/set?somekey=somevalue"
# Go to the browser to run get request http://localhost:4000/get?key=somekey

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Telling server what to do when receiving a request for the client
class MyHandler(BaseHTTPRequestHandler):
    storage = {}

    # This block of code tells server what to send to the client
    def send_response_message (self,return_object):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(return_object.encode())

    # This block of code tells how to split the clients URL to retrieve the information we need (key-value pair)
    def url_path_parser(self): 
        print(f"this is the path {self.path}")      
        url = self.path
        parsed_url = urlparse (url)
        url_query_dict=parse_qs(parsed_url.query)
        return(url_query_dict)
    

    # This block of code handles set requests (adds new key-value pairs to the storage)
    # Required format of set request is http://localhost:4000/set?somekey=somevalue
    # Using next(iter) to access the first (and only) key-pair in the dictionary since dictionary.items() returns a view object
    def do_POST(self):
        if self.path.startswith('/set'):
            url_query_dict = self.url_path_parser()
            new_storage_item = {k:v[0] for k,v in url_query_dict.items()}
            new_storage_item_key, new_storage_item_value = next(iter(new_storage_item.items()))

            if new_storage_item_key in self.storage and new_storage_item_value in self.storage.values():
                return_object = f'The pair {new_storage_item} is already in the storage'

            elif new_storage_item_key in self.storage:
                return_object = f'This key is already used. Please change the key to add new value to the storage'
                
            else:      
                self.storage.update(new_storage_item)
                return_object = f'The pair {new_storage_item} was added to the storage'
            
            self.send_response_message(return_object) 

        else:
            self.send_response_message('Invalid POST request')    

   
    # This block of code handles get requests (retrieves the requested value from the storage)
    # Required format of get request http://localhost:4000/get?key=somekey
    # Using dictionary.get method to access the value of the key Or return None if value doesn't exist or the word 'key' is missing
    def do_GET(self):   
        if self.path.startswith('/get'):
            url_query_dict = self.url_path_parser()    
            item_to_fetch_key = url_query_dict.get('key', None)
            if item_to_fetch_key == None:
                return_object = 'The request doesn\'t contain the "key" word'
            else:
                try: 
                    item_to_fetch_key = url_query_dict.get('key')[0]   
                    item_to_fetch_value = self.storage[item_to_fetch_key] 
                    return_object = item_to_fetch_value    
                except KeyError:
                    return_object = 'The key is not in the storage'
            
            self.send_response_message(return_object) 
        else:
            self.send_response_message('Invalid POST request')   


# This block of code runs a server on port 400 of the localhost
# With block makes sure that server stops running on when we close the program
with HTTPServer(('127.0.0.1', 4000), MyHandler) as server:
    server.serve_forever()     





