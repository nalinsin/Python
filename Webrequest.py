pip install requests
pip install beautifulsoup4

# Collecting a Web Page with Requests

import requests
url='https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'

pagge=requests.get(url)
pagge
pagge.text

# Stepping Through a Page with Beautiful Soup

from bs4 import BeautifulSoup
sooup=BeautifulSoup(pagge.text,'html.parser')
print(soup.prettify())

# Finding Instances of a Tag

sooup.find_all('p')
sooup.find_all('p')[2].get_text()

# Finding Tags by Class and ID

sooup.find_all(class_='verse')
sooup.find_all(class_='verse')[0]
sooup.find_all('p', class_='verse')
sooup.find_all('p', class_='verse', id='third')

