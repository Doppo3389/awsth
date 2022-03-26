import requests
from bs4 import BeautifulSoup

url = 'https://pkvartal.mskobr.ru/edu-news/3565'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_="kris-redaktor-format")

for quote in quotes:
    print(quote.text)