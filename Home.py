import streamlit as st

st.set_page_config(page_title="BR Bank | Dashboard de Growth", layout="wide")

st.title("📊 BR Bank – Dashboard de Growth")
st.markdown("---")

st.markdown("""
Bem-vindo(a) ao painel estratégico da fintech BR Bank.

Este dashboard foi desenvolvido para acompanhar toda a jornada do lead — desde a aquisição até a monetização — e apoiar decisões orientadas por dados.

Use o menu lateral para navegar entre os dashboards de **Aquisição**, **Retenção**, **Monetização**, **Performance** e **Exploração Analítica**.

""")

st.subheader("🚀 Visão Geral do Projeto")
st.markdown("""
- **Objetivo:** Monitorar aquisição, funil de vendas, desempenho dos vendedores e retorno financeiro.
- **Fontes de dados:** Google Analytics, Google Ads, Meta Ads e CRM interno.
- **Indicadores principais:** CAC, LTV, ROAS, Receita, Taxa de Conversão, Motivo de Perda, Ticket Médio.
""")

st.subheader("📁 Navegação")
st.markdown("""
- **1_Aquisicao:** Análise do funil de entrada (Visitantes → Leads → Clientes).
- **2_Retencao:** Gargalos no CRM e tempo de conversão por vendedor.
- **3_Monetizacao:** Receita por vendedor, Ticket Médio, ROAS e LTV.
- **4_Performance:** Painel resumo com KPIs gerais.
- **5_Exploracao_Analitica:** Visualizações livres para cruzamento de dados.
""")
