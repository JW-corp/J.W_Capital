import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

def crawl_quotes(quote_html):
	quote_text = quote_html.select('div.quote > span.text')
	quote_text_list = [i.text for i in quote_text]
	print(quote_text_list)
	return quote_text_list

def craw_authors(quote_html):
	quote_author = quote_html.select('div.quote > span > small.author')
	quote_author_list = [i.text for i in quote_author]
	print(quote_author_list)
	return quote_author_list

def craw_links(quote_html):
	quote_link = quote_html.select('div.quote > span > a')
	quote_link_list = ['https://quotes.toscrape.com'+i['href'] for i in quote_link]
	print(quote_link_list)
	return quote_link_list

if __name__ == "__main__":

	text_list = []
	author_list = []
	infor_list = []

	for i in range(1,100):
		url = f'https://quotes.toscrape.com/page/{i}/'
		print(url)
		quote = rq.get(url)
		quote_html = BeautifulSoup(quote.content, 'html.parser')

		quote_text_list 	= crawl_quotes(quote_html)
		quote_author_list   = craw_authors(quote_html)
		quote_link_list 	= craw_links(quote_html)
		
		if len(quote_text_list) > 0:
			text_list.extend(quote_text_list)
			author_list.extend(quote_author_list)
			infor_list.extend(quote_link_list)

		else:
			break


	quote_df = pd.DataFrame({'text':text_list, 'author':author_list, 'link':infor_list})
	print(quote_df)


