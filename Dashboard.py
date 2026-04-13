import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/rogeriopereira01/LogDigital/refs/heads/main/logistica_tratada.csv"

df = pd.read_csv(url)

df["Custo_KM"] = df["CustoFrete"] / df["DistanciaKM"]

df["Atraso"] = (
    pd.to_datetime(df["DataEntregaReal"], errors="coerce") - 
    pd.to_datetime(df["DataEntregaPrevista"], errors="coerce")
).dt.days

st.title("📊 Dashboard Logístico")

col1, col2, col3 = st.columns(3)

col1.metric("Total de Pedidos", len(df))
col2.metric("Custo Médio/KM", round(df["Custo_KM"].mean(), 2))
col3.metric("Atraso Médio (dias)", round(df["Atraso"].mean(), 1))

st.subheader("🚚 Custo Médio por Transportadora")

df_transp = df.groupby("Transportadora")["Custo_KM"].mean()

fig, ax = plt.subplots()
df_transp.plot(kind='bar', ax=ax)
st.pyplot(fig)

st.subheader("⏱️ Distribuição de Atrasos")

fig2, ax2 = plt.subplots()
df["Atraso"].dropna().plot(kind='hist', ax=ax2)
st.pyplot(fig2)

st.subheader("📦 Dados Completos")

st.dataframe(df)
