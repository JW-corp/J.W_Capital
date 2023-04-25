import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head())

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:smoke1sland!@127.0.0.1:3306/shop')
iris.to_sql(name='iris', con=engine, if_exists='replace', index=False)
engine.dispose()



