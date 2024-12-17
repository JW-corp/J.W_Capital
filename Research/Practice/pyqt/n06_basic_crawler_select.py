import requests as rq
from bs4 import BeautifulSoup


def crawl_quotes(quote_html):
	
	quote_text = quote_html.select('div.quote > span.text')
	quote_text_list = [i.text for i in quote_text]
	print(quote_text_list)


def craw_authors(quote_html):
	quote_author = quote_html.select('div.quote > span > small.author')
	quote_author_list = [i.text for i in quote_author]
	print(quote_author_list)
	
def craw_links(quote_html):
	quote_link = quote_html.select('div.quote > span > a')

	print(['https://quotes.toscrape.com'+i['href'] for i in quote_link])


if __name__ == "__main__":
	url = 'https://quotes.toscrape.com/'
	quote = rq.get(url)
	quote_html = BeautifulSoup(quote.content, 'html.parser')

	#crawl_quotes(quote_html)
	#craw_authors(quote_html)
	craw_links(quote_html)
	
