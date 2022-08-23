import requests
from bs4 import BeautifulSoup
website = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(website.text, 'html.parser')
title = soup.find('title')
print("Title of the webiste: ", title, title.text)
links = soup.findAll('a')
for link in links:
    print(link.text)
quote = soup.find(class_="text")
print("Quote == ", quote)
links_2 = soup.find_all('a')
print("All Links : 2::\n", links_2)
quotes = soup.find_all(class_='text')
for quote in quotes:
    print(quote.text)
login_link = soup.find(href="/login")
print("Login Link : ", login_link)
quote = soup.find(class_='quote')
quote_text = quote.find(class_='text')
quote_author = quote.find(class_='author')
print(quote, quote_text.text, quote_author.text)
