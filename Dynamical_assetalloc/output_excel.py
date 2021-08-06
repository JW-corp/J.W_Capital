import pandas as pd
df = pd.read_pickle('krx.pkl')

mask = df['avg_p_score'] == 12
df = df[mask]

df = df.dropna()
df.to_excel("output.xlsx")
