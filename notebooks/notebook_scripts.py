# %% [markdown]
# ## 1. Consolidated files in the unique DataFrame and show the total files extracted

# %%

import os
import sys

notebook_path = os.path.dirname(os.path.abspath("data_explorer.ipynb"))
sys.path.append(os.path.dirname(notebook_path))

from etl.utils.common import DefaultOutputFolder as dir
import pandas as pd

files = os.listdir(dir())
dfs = []

if not files: print("No files found in the output folder.")

for file in files:
    if file.endswith(".parquet"):
        df = pd.read_parquet(dir() + file)
        dfs.append(df)
    
allFiles = pd.concat(dfs, ignore_index=True)

# Ordering DataFrame by column name
allFiles = allFiles.sort_values(by=['extracted_at'], ascending=False)

# count the rows in dataframe
allFiles.shape[0]

# %% [markdown]
# ## 1.1 Data set sample, list 5 files

# %%
allFiles.head(3)

# %% [markdown]
# ## 2. Change DataTypes and Reorder columns

# %%
# Change data types
df = allFiles.astype({'ask': float, 'bid': float, 'varBid': float, 'pctChange': float})

# Show the dataframe
df.head(3)


# %% [markdown]
# ## 3. Using SQL for Data Exploration
#     3.1 What is the currency with the highest ask value?

# %%
from pandasql import sqldf

query = """
    SELECT symbol, name, max(ask) max_ask FROM df 
    where code = 'BRL' 
    group by symbol, name
    order by 3 desc limit 1
"""

newDf = sqldf(query, locals())

newDf



# %% [markdown]
#     3.1 Disponible Data

# %%
from pandasql import sqldf

query = """
    SELECT code, codein, name FROM df 
    group by 1,2,3
"""

newDf = sqldf(query, locals())

newDf

# %% [markdown]
# ## 4. Using SQL + Matplotlib for Data Viz
#     4.1 What is the TOP 10 Most Value Currency considering BRL?

# %%

import matplotlib.pyplot as plt

query = """
    SELECT 
        name
        ,round(avg(ask),2) AvgAsk
    FROM df 
    where codein = 'BRL'
    and not code in ('BTC', 'ETH', 'LTC', 'DOGE')
    group by name
    order by avg(ask) desc limit 10
"""

newDf = sqldf(query, locals())
newDf.sort_values(by='AvgAsk', ascending=True, inplace=True)

AvgAskByCurrency = newDf.plot(
    kind='barh', x='name', y='AvgAsk', 
    figsize=(15, 10), 
    legend=False, 
    color='blue', title='Top 10 Most Valuable Currencies by Ask Price', xlabel='Ask Price', ylabel='Symbol')


# Adicionando rótulos aos dados
for index, value in enumerate(newDf['AvgAsk']):
    plt.text(value, index, str(value))

# Exibir o gráfico
plt.show()

# %% [markdown]
# 4.2 What is the TOP 10 locations BRL has + value?

# %%

import matplotlib.pyplot as plt

query = """
    SELECT 
        name
        ,round(avg(ask),2) AvgAsk
    FROM df 
    where codein = 'BRL'
    and not code in ('BTC', 'ETH', 'LTC', 'DOGE')
    group by name
    order by avg(ask) limit 10
"""

newDf = sqldf(query, locals())
newDf.sort_values(by='AvgAsk', ascending=False, inplace=True)

AvgAskByCurrency = newDf.plot(
    kind='barh', x='name', y='AvgAsk', 
    figsize=(15, 10), 
    legend=False, 
    color='blue', title='Top 10 Most Valuable Currencies by Ask Price', xlabel='Ask Price', ylabel='Symbol')


# Adicionando rótulos aos dados
for index, value in enumerate(newDf['AvgAsk']):
    plt.text(value, index, str(value))

# Exibir o gráfico
plt.show()

# %% [markdown]
# 4.3 What the top 10 like BRL in value?

# %%

import matplotlib.pyplot as plt

query = """
    SELECT 
        name
        ,round(avg(ask),2) AvgAsk
    FROM df 
    where codein = 'BRL'
    and not code in ('BTC', 'ETH', 'LTC', 'DOGE')
    and ask >=1
    group by name
    order by avg(ask) desc limit 5
"""

newDf = sqldf(query, locals())
newDf.sort_values(by='AvgAsk', ascending=False, inplace=True)

AvgAskByCurrency = newDf.plot(
    kind='barh', x='name', y='AvgAsk', 
    figsize=(15, 10), 
    legend=False, 
    color='blue', title='Top 10 Most Valuable Currencies by Ask Price', xlabel='Ask Price', ylabel='Symbol')


# Adicionando rótulos aos dados
for index, value in enumerate(newDf['AvgAsk']):
    plt.text(value, index, str(value))

# Exibir o gráfico
plt.show()

# %% [markdown]
# 4.4 Average Ask By Day

# %%

import matplotlib.pyplot as plt

query = """
    SELECT 
        create_date DT_REF
        ,round(avg(ask),2) AvgAsk
        ,round(avg(bid),2) Avgbid
    FROM df 
    where not code in ('BTC', 'ETH', 'LTC', 'DOGE')
    group by 1
    order by 1 
"""

newDf = sqldf(query, locals())
newDf.sort_values(by='DT_REF', ascending=True, inplace=True)

cht = newDf.plot(
    kind='line', x='DT_REF', y='AvgAsk',
    figsize=(15, 10), 
    legend=False, 
    color='blue', title='Average ASK tendence by Day', xlabel='Date', ylabel='AvgAsk')

#exibir o grafico
plt.show()

# %% [markdown]
# 4.5 Average Bid By Day

# %%

import matplotlib.pyplot as plt

query = """
    SELECT 
        create_date DT_REF
        ,round(avg(ask),2) AvgAsk
        ,round(avg(bid),2) Avgbid
    FROM df 
    where not code in ('BTC', 'ETH', 'LTC', 'DOGE')
    group by 1
    order by 1 
"""

newDf = sqldf(query, locals())
newDf.sort_values(by='DT_REF', ascending=True, inplace=True)

cht = newDf.plot(
    kind='line', x='DT_REF', y='Avgbid',
    figsize=(15, 10), 
    legend=False, 
    color='blue', title='Average BID tendence by Day', xlabel='Date', ylabel='Avgbid')

#exibir o grafico
plt.show()

# %% [markdown]
# 

# %%