import requests
import pandas as pd
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(website.text, 'html.parser')

links = soup.findAll('a')

with open('links.txt', 'w') as f:
    for link in links[1:]:
        f.write(link["href"])
        f.write("\n")

quotes = soup.find_all(class_='quote')
quotes_list = []
author_list = []
for quote in quotes:
    quotes_list.append(quote.find(class_="text").text[1:-1])
    author_list.append(quote.find(class_='author').text)


quotation = pd.DataFrame(columns = ['Quote' , 'Author' ])

quotation = pd.DataFrame({"Quote" : quotes_list , "Author" : author_list })


quotation.to_csv('quotes.csv' , index=False)