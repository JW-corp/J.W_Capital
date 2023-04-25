from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy_utils import create_database


#engine = create_database('mysql+pymysql://root:smoke1sland!@127.0.0.1:3306/exam')


price = pd.DataFrame({
    "날짜": ['2021-01-02', '2021-01-03'],
    "티커": ['000001', '000001'],
    "종가": [1340, 1315],
    "거래량": [1000, 2000]
})

engine = create_engine('mysql+pymysql://root:smoke1sland!@127.0.0.1:3306/exam')
price.to_sql('price', con=engine, if_exists='append', index=False)
data_sql = pd.read_sql('price', con=engine)
engine.dispose()


