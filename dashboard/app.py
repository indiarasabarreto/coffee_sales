import streamlit as st
import pandas as pd

from pathlib import Path

# Filtra os dados pelo café selecionado (que você já tem)
df_filtrado = df[df['coffee_name'] == cafe_selecionado]

# ── Cartões de métricas ──────────────────────────────
col1, col2, col3 = st.columns(3)

col1.metric("💰 Receita Total", f"R$ {df_filtrado['money'].sum():,.2f}")
col2.metric("📦 Total de Vendas", len(df_filtrado))
col3.metric("🎯 Ticket Médio", f"R$ {df_filtrado['money'].mean():.2f}")

df = pd.read_csv(Path(__file__).parent / 'coffee_data.csv')


st.title("Dashboard de Vendas")

coffee_name = st.selectbox("Escolha o café", df['coffee_name'].unique())
filtered_data = df[df['coffee_name'] == coffee_name]
st.write(filtered_data)
st.bar_chart(filtered_data.groupby('date')['money'].sum())


# run with streamlit run .\app.py
