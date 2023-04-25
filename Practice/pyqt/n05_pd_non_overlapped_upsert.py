import pymysql
import pandas as pd




# link python to mysql
con = pymysql.connect(

	user='root',
	passwd='smoke1sland!',
	host='127.0.0.1',
	db='exam',
	charset='utf8'
	)

mycursor = con.cursor()



price = pd.DataFrame({
    "날짜": ['2021-01-04', '2021-01-04'],
    "티커": ['000001', '000002'],
    "종가": [1320, 1315],
    "거래량": [2100, 1500]
})

args = price.values.tolist()


print(args)

#query = """
#INSERT INTO price (날짜, 티커, 종가, 거래량)
#values (%s, %s, %s, %s) as new
#on duplicate key update
#종가 = new.종가,거래량 = new.거래량;
#"""
#
#mycursor = con.cursor()
#mycursor.executemany(query, args)
#con.commit()
#
#con.close()
#
#
