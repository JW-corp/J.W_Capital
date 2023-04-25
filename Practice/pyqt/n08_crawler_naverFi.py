import requests as rq
from bs4 import BeautifulSoup
import numpy as np
import html


return_list=[]

def traker(title_list,href_list,return_list):
	mylist = ["블록","올리지오","원텍","루트로닉"]
	
	# -- loop all topics
	for idx,line in enumerate(title_list):
	
		# -- Check my topics
		if any(i in line for i in mylist):
			print(idx,line)
			return_list.append([line,"https://finance.naver.com"+href_list[idx]])
	
	


for page in range(1,100):

	url         = f'https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258&page={page}'
	data        = rq.get(url)
	
	# -- change parser to deal with spection charater auto-convertin 
	#html        = BeautifulSoup(data.content, 'html.parser')
	html        = BeautifulSoup(data.content, 'lxml')
	
	html_select = html.select('dl > dd.articleSubject > a')
	
	title_list = [i['title'] for i in html_select]
	href_list   =[i['href'] for i in html_select]
	
	
	if len(title_list) >0:
		traker(title_list,href_list,return_list)
	else:
		break


print("Summary ###############")
for i in return_list:
	print(i)
	#f = open("my_news_list.csv",'a')
	#f.write(f"{i[0],i[1]} \n")
