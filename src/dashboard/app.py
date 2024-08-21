import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('..\data\quotes.db')

df = pd.read_sql_query('SELECT * FROM mercadolivre_items', conn)

conn.close()

st.title("Pesquisa de Mercado - Preço de Tenis Masculino")

# Aqui é o print do streamlit (pd.head)
# st.write(df)

# Colocando colunas no nosso dash
st.subheader("Principais KPIs do Sistema")
col1, col2, col3 = st.columns(3)

# KPI 1 - numero total de itens
total_itens = df.shape[0]
col1.metric("Numero Total de Tênis", value=total_itens)

# KPI 2: Número de marcas
brands_counts = df['brand'].nunique()
col2.metric("Numero de Marcas Unica", value=brands_counts)

# KPI 3: Preço méc\io novo
average_new_price = df['new_price'].mean()
col3.metric("Preço Médio Novo (R$)", value=f'{average_new_price:.2f}')

# Quais são as marcas mais encontradas
col1, col2 = st.columns([4, 2])  # Proporção das colunas
top_10_pages_brand = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brand)
col2.write(top_10_pages_brand)


# Preço medio por marca
st.subheader("Preço médio por marca")
col1, col2 = st.columns([4, 2])  # Proporção das colunas
average_price_by_brand = df.groupby(
    'brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)
