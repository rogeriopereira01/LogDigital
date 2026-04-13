import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rogerin001@",
    database="logistica_db"
)

query = """
SELECT 
    p.PedidoID,
    c.Nome_Cliente,
    t.Nome_Transportadora,
    p.Custo_Frete,
    p.DistanciaKM,
    (p.Custo_Frete / p.DistanciaKM) AS Custo_KM,
    DATEDIFF(p.DataEntrega_Real, p.DataEntrega_Prevista) AS Atraso
FROM pedidos p
JOIN clientes c ON p.ClienteID = c.ClienteID
JOIN transportadoras t ON p.Transportadora_id = t.id
"""

df = pd.read_sql(query, conn)

st.title("📊 Dashboard Logístico")

col1, col2, col3 = st.columns(3)

col1.metric("Total de Pedidos", len(df))
col2.metric("Custo Médio/KM", round(df["Custo_KM"].mean(), 2))
col3.metric("Atraso Médio", round(df["Atraso"].mean(), 1))

st.subheader("Custo por Transportadora")

df_transp = df.groupby("Nome_Transportadora")["Custo_KM"].mean()

fig, ax = plt.subplots()
df_transp.plot(kind='bar', ax=ax)
st.pyplot(fig)

st.subheader("Dados")

st.dataframe(df)