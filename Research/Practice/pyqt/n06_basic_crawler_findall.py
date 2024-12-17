import requests as rq
from bs4 import BeautifulSoup


# -- General usage
url = 'https://quotes.toscrape.com/'
quote = rq.get(url)

#print(quote)
#print(quote.content[:1000])

quote_html = BeautifulSoup(quote.content, 'html.parser')
#print(quote_html.head())

quote_div = quote_html.find_all('div', class_='quote')

#print(quote_div[0])
quote_span = quote_div[0].find_all('span', class_='text')
print(quote_span[0].text)

# -- Put all-toghether
quote_div = quote_html.find_all('div', class_ = 'quote')
quote_list = [i.find_all('span', class_ ='text')[0].text for i in quote_div]
print(quote_list)



