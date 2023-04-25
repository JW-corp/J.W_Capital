import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:smoke1sland!@127.0.0.1:3306/shop')
query  = """select * from Goods"""

goods  = pd.read_sql(query, con=engine)

engine.dispose() # end connection

print(goods.head())
