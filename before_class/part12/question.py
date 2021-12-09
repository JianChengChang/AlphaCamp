# Q1

import pandas as pd

df = pd.read_json(r"D:\git\AlphaCamp\before_class\data\meta_All_Beauty.json.gz", lines=True, compression='gzip')
df.shape
# (32892,19)
df.brand.value_counts()[1:4]
# VAGA, L'Oreal Paris, Philips Norelco

# Q2
df = df[['asin','brand', 'title', 'price', 'rank', 'description']]
df['rank'] = df['rank'].str.extract(r"([\d,]*)")
df['rank'] = df['rank'].str.replace(',','')
df['rank'] = pd.to_numeric(df['rank'])
df.iloc[df['rank'].idxmin()]['rank'] 
# 35
df.iloc[df['rank'].idxmin()]['title'].replace('&amp;','&') 
# Braun Clean & Renew Refill Cartridges CCR, 4 Count (Packaging May Vary)

# Q3
df2 = pd.read_json(r"D:\git\AlphaCamp\before_class\data\All_Beauty.json.gz", lines=True, compression='gzip')
df2.asin.value_counts()
# B000FOI48G, 8672
df2.groupby(by=['asin']).overall.mean().loc['B000FOI48G']
# 4.393450184501845

# Q4
df = df.set_index('asin')
df['overall_mean'] = df2.groupby(by=['asin']).overall.mean()
df['review_count'] = df2.groupby(by='asin').size()
df.loc[df['rank'].idxmin()]
# 4.846, 13
