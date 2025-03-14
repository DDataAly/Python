import requests
from bs4 import BeautifulSoup

print('Here comes a web crawler!')

URL = 'https://pythonjobs.github.io/'
page = requests.get(URL)

print(page.text)

soup = BeautifulSoup(page.content, 'html.parser')

job_publications = soup.find(class_='job_list')

backend_only = job_publications.find_all('h1', string = lambda role: 'backend' in role.lower())
for item in backend_only:
    print(item)



# import requests
# from bs4 import BeautifulSoup

# print('Here comes a web crawler!')

# URL =  'https://realpython.github.io/fake-jobs/'
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(id='ResultsContainer')

# python_jobs = results.find_all('h2', string = lambda text:'python' in text.lower())

# python_job_cards = [h2_element.parent.parent.parent for h2_element in python_jobs]

# for job in python_job_cards[0:1]:
#     title_element = job.find('h2',class_='title')
#     company_element = job.find('h3', class_='company')
#     location_element = job.find('p', class_='location')
#     link_url = job.find_all('a')[1]['href']  
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print(f'Apply here: {link_url}', end='\n'*2)  






