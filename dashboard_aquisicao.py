import streamlit as st

st.set_page_config(page_title="Aquisição | BR Bank", layout="wide")
st.title("📥 Dashboard de Aquisição de Leads")
st.markdown("---")

st.markdown("""
Essa página foca na **análise da jornada inicial do lead**, desde o tráfego no site até o registro no CRM.

### 🎯 Objetivo
Avaliar se os canais de aquisição estão atraindo visitantes qualificados e convertendo de forma eficiente.

### 🔍 Métricas Monitoradas
- Visitantes no site (Google Analytics)
- Leads gerados (CRM)
- Conversão de Visitantes → Leads
- Conversão de Leads → Clientes
- Conversão de Visitantes → Clientes
- Desempenho de campanhas de tráfego pago (Google Ads & Meta Ads)
- CTR, CPC, Custo por Conversão, ROAS

Use os filtros para analisar variações por canal, campanha e período.
""")
