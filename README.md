![Python](https://img.shields.io/badge/Python-3.10-blue)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Completed-green)

# 📊 Análise de Dados Logísticos com MySQL e Python

## 🚀 Objetivo do Projeto
O objetivo deste projeto é analisar dados logísticos utilizando o MySQL como base de dados principal e o Python como ferramenta de processamento e análise.

Como diferencial, foi desenvolvido um dashboard interativo para visualização dos indicadores, agregando valor à análise.

---

## 🌐 Dashboard Interativo
👉 [https://logdigital.streamlit.app](https://logdigital-x9bb3v5vn5j8sq7ejdupre.streamlit.app)

---

## 🧠 Descrição do Projeto

O projeto simula um ambiente logístico real, envolvendo:

- Pedidos
- Clientes
- Produtos
- Transportadoras
- Entregas

Os dados foram estruturados em um banco relacional no MySQL e posteriormente analisados com Python.

---

## 🗄️ Banco de Dados (MySQL)

Foi desenvolvido um banco de dados relacional com as seguintes tabelas:

- `clientes`
- `pedidos`
- `itens_pedido`
- `produtos`
- `transportadoras`
- `localidades`

### 🔹 Modelagem

A modelagem foi feita com foco em:

- Normalização dos dados
- Integridade referencial
- Relacionamentos entre entidades

---

## 🔄 ETL e Tratamento de Dados (Python)

O Python foi utilizado para:

- Tratamento do arquivo CSV
- Padronização de dados
- Conversão de datas
- Tratamento de valores nulos
- Preparação para carga no MySQL

Bibliotecas utilizadas:

- Pandas
- MySQL Connector

---

## 📊 Consultas SQL

Foram realizadas consultas para extração de indicadores logísticos, como:

- Custo por KM
- Atraso nas entregas
- Desempenho por transportadora

Exemplo:

```sql
SELECT 
    p.PedidoID,
    p.Custo_Frete,
    p.DistanciaKM,
    (p.Custo_Frete / p.DistanciaKM) AS Custo_KM
FROM pedidos p;

## 🔄 Arquitetura do Projeto

CSV → Python (Tratamento) → MySQL → Python (Consulta) → Streamlit (Dashboard)
