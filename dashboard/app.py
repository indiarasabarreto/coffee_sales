import streamlit as st
import pandas as pd

from pathlib import Path

df = pd.read_csv(Path(__file__).parent / 'coffee_data.csv')

st.title("Dashboard de Vendas")

cafe_selecionado = st.selectbox("Escolha o café", df['coffee_name'].unique())

# Filtra os dados pelo café selecionado (que você já tem)
df_filtrado = df[df['coffee_name'] == cafe_selecionado]

# ── Cartões de métricas ──────────────────────────────
col1, col2, col3 = st.columns(3)

col1.metric("💰 Receita Total", f"R$ {df_filtrado['money'].sum():,.2f}")
col2.metric("📦 Total de Vendas", len(df_filtrado))
col3.metric("🎯 Ticket Médio", f"R$ {df_filtrado['money'].mean():.2f}")

st.write(df_filtrado)
st.bar_chart(df_filtrado.groupby('date')['money'].sum())


# run with streamlit run .\app.py
