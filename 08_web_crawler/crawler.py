import requests

print('Here comes a web crawler!')

URL =  'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)
print(page.text)

