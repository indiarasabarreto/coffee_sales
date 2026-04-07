import streamlit as st
import pandas as pd

df = pd.read_csv('coffee_data.csv')
# print(df.columns)

st.title("Dashboard de Vendas")

coffee_name = st.selectbox("Escolha o café", df['coffee_name'].unique())
filtered_data = df[df['coffee_name'] == coffee_name]
st.write(filtered_data)
st.bar_chart(filtered_data.groupby('date')['money'].sum())


# run with streamlit run .\app.py
