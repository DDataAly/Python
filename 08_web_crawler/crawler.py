# Practice - Multiple pages output https://remote.co/remote-jobs/developer 
import requests
from bs4 import BeautifulSoup

print('Here comes a web crawler!')

URL = 'https://remote.co/remote-jobs/developer'
page=requests.get('https://remote.co/remote-jobs/developer')
soup = BeautifulSoup(page.content, 'html.parser')
job_table = soup.find(id='job-table-wrapper')
engineering_jobs = job_table.find_all(class_='sc-jv5lm6-13 cMHfum textWrap', string = lambda title: 'engineer' in title.lower())
engineering_job_cards = [job.parent.parent.parent.parent for job in engineering_jobs]


for job in engineering_job_cards:
    title = job.find(class_='sc-jv5lm6-13 cMHfum textWrap').get_text()
    location = job.find(class_='sc-jv5lm6-10 efTTiy allowed-location').get_text()
    print(title)
    print(location)
    print(f'/n')
    # print(job.prettify())



# Tutorial
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


# # Practice - https://pythonjobs.github.io/
# import requests
# import re
# from bs4 import BeautifulSoup

# print('Here comes a web crawler!')

# URL = 'https://pythonjobs.github.io/'
# page = requests.get(URL)


# soup = BeautifulSoup(page.content, 'html.parser')
# job_publications = soup.find(class_='job_list')

# backend_only = job_publications.find_all('h1', string = re.compile(r'[Bb]ack[-\s]?[Ee]nd'))

# backend_full_card = [h1.parent for h1 in backend_only]

# for item in backend_full_card:
#     # .text is a BS object/tag attribute, and .get_text() is a BS method.
#     # .get_text has optional attributes including strip which is False by default
#     # .text.strip() does the same as .get_text(strip=True) but latter is cleaner
#     title = item.find('h1').text.strip()
#     location = (item.find(class_='i-globe').parent).get_text(strip=True)
#     company = (item.find(class_='i-company').parent).get_text(strip=True)
#     details = item.find(class_='go_button')['href']
#     print(f'\nRole: {title}')
#     print(f'Location: {location}')
#     print(f'Company: {company}')
#     print(f'Apply here: {details}')




