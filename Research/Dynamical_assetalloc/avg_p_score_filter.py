import FinanceDataReader as fdr
import pandas as pd
import numpy as np



df_krx = fdr.StockListing("KRX")
def avg_p_score_filter(code,t):
  df = fdr.DataReader(code, t)
  score=0
  for i in range(1,13):
    col_name = str(i)
    if (df['Close'].pct_change(i*20) > 0).loc[t]:
      score+=1
  return score 

from tqdm import tqdm
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('date', type=str,
            help="ex) python avg_p_score_filter.py 2021-08-27")
args = parser.parse_args()


date = args.date



avg_p_score_arr = []
for i in tqdm(df_krx['Symbol']):
  try:
     avg_p_score_arr.append(avg_p_score_filter(i,date))
  except:
    avg_p_score_arr.append(-1)

df_krx['avg_p_score'] =  avg_p_score_arr

df_krx.to_pickle("krx.pkl")

