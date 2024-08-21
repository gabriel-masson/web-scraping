import pandas as pd
from datetime import datetime
import sqlite3


df = pd.read_json('..\data\data.json')

# Ao criar um web scrapping, devemos colocar uma coluna fixa dizendo a origem dos dados
df['_source'] = 'https://lista.mercadolivre.com.br/tenis-corrida-masculino'

# Add data
df['_data_coleta'] = datetime.now()

# conversão dos dados
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)

df['reviews_amount'] = df['reviews_amount'].str.replace(
    '[\(\)]', '', regex=True)

df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

df['old_price'] = df['old_price_reais'] + df['old_price_centavos']/100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos']/100

df.drop(columns=['old_price_reais', 'old_price_centavos',
        'new_price_centavos', 'new_price_reais'], inplace=True)

conn = sqlite3.connect('..\data\quotes.db')

df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

conn.close()
print(df.columns)
print(df)
