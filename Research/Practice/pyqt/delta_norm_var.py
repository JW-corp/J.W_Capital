import FinanceDataReader as fdr
import pandas as pd
import numpy as np
import math

df = fdr.DataReader('048260', '2022-04-15')


invest =1000000
std_return = df['Close'].pct_change().std()
t = math.sqrt(1)
z = 2.33

VaR = invest * std_return * z * t
print(f"Var: {VaR}")


