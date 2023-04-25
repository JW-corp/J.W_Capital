import pymysql


# link python to mysql
con = pymysql.connect(

	user='root',
	passwd='smoke1sland!',
	host='127.0.0.1',
	db='shop',
	charset='utf8'
	)

mycursor = con.cursor()


# fisrt query
query="""
select * from goods;
"""

mycursor.execute(query) # Send query
data = mycursor.fetchall() # Get data from DB
con.close() # Quit DB

print(data)

