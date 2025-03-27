import streamlit as st

st.set_page_config(page_title="Retenção | BR Bank", layout="wide")
st.title("⏱️ Dashboard de Retenção e Conversão no Funil")
st.markdown("---")

st.markdown("""
Esse painel mostra **como os leads evoluem dentro do CRM**, desde o contato inicial até a conversão — ou perda.

### 🎯 Objetivo
Identificar gargalos no funil e otimizar o processo comercial.

### 🔍 Métricas Monitoradas
- Leads ativos vs. convertidos
- Tempo médio para conversão
- Principais motivos de perda
- Taxa de conversão por vendedor
- Etapas com mais desistências

Use os gráficos para encontrar padrões de comportamento e oportunidades de melhoria no funil.
""")
