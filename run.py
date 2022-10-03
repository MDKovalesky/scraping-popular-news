import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detik-populer')
def popular_detik():
    url = 'https://www.detik.com/terpopuler'

    html_doc = requests.get(url)

    soup = BeautifulSoup(html_doc.text, 'html.parser')

    popular_area = soup.find(attrs={'class': 'grid-row list-content'})

    titles = popular_area.findAll(attrs={'class': 'media__title'})
    images = popular_area.findAll(attrs={'class': 'media__image'})

    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)