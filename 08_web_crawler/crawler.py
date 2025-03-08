import requests
from bs4 import BeautifulSoup

print('Here comes a web crawler!')

URL =  'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


