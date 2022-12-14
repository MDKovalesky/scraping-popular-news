import requests
from bs4 import BeautifulSoup

url = 'https://www.detik.com/terpopuler'

html_doc = requests.get(url)

soup = BeautifulSoup(html_doc.text, 'html.parser')

popular_area = soup.find(attrs={'class': 'grid-row list-content'})

titles = popular_area.findAll(attrs={'class': 'media__title'})
images = popular_area.findAll(attrs={'class': 'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])

# print(titles)