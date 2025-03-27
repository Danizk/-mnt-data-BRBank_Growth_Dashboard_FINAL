# 📊 Projeto de Estudo – BR Bank

Estudo de caso fictício de análise de dados aplicada à construção de dashboards estratégicos com **Python + Streamlit**.

---

## 🎯 Objetivo

Acompanhar a jornada do lead — desde o primeiro acesso ao site até a conversão em cliente ativo — e avaliar o desempenho financeiro da fintech BR Bank.

Este projeto consolida dados de **Google Analytics**, **Google Ads**, **Meta Ads** e **CRM** para gerar insights sobre **aquisição, conversão e monetização** de clientes, permitindo decisões táticas baseadas em dados.

---

## 📌 Problema Resolvido

A BR Bank enfrentava dificuldades para visualizar e integrar os dados de aquisição, vendas e receita em um único painel.  
O dashboard resolve essa limitação e permite:

- Identificar gargalos no funil de vendas
- Avaliar a performance dos vendedores
- Medir o retorno sobre o investimento em mídia
- Garantir o crescimento baseado em dados confiáveis

---

## 🧠 Tecnologias Utilizadas

- **Python 3.11**
- **Streamlit** (para interface interativa)
- **Plotly Express** (para gráficos responsivos e acessíveis)
- **Pandas** (tratamento e análise de dados)
- **Streamlit Multipage App Structure** (pages/)

---

## 🧭 Estrutura de Navegação

Acesse as páginas pelo menu lateral:

| Página                            | Descrição                                                                 |
|----------------------------------|---------------------------------------------------------------------------|
| `Home.py`                        | Apresentação do projeto, objetivo e links rápidos                        |
| `1_Aquisicao.py`                 | Análise do funil de aquisição: visitantes → leads → clientes             |
| `2_Retencao.py`                  | Motivos de perda, tempo médio de conversão, gargalos no CRM              |
| `3_Monetizacao.py`              | Receita por vendedor, Ticket Médio, LTV, ROAS e Margem                   |
| `4_Performance.py`              | Painel de KPIs executivos: CAC, Receita, Conversão, Vendas, ROAS         |
| `5_Exploracao_Analitica.py`     | Ferramenta para análise exploratória com filtros dinâmicos               |

---

## 📊 Indicadores Monitorados

- CAC (Custo de Aquisição de Cliente)
- LTV (Lifetime Value)
- ROAS (Retorno sobre investimento em Ads)
- Receita Total e Receita por Vendedor
- Ticket Médio
- Conversão por Etapa e por Vendedor
- Tempo Médio de Conversão
- Motivos de Perda de Clientes

---

## 📂 Fontes de Dados

| Fonte          | Finalidade                                                                 |
|----------------|-----------------------------------------------------------------------------|
| Google Analytics | Visitantes no site, datas e acessos                                        |
| Google Ads      | Dados de campanhas pagas, impressões, cliques, custos, conversões          |
| Meta Ads        | Dados de campanhas em Facebook/Instagram                                   |
| CRM             | Leads, vendedores, datas de conversão/perda, receita, status de conversão  |

---

## 📎 Visualize o Projeto Online

[🌐 Ver Demo no Streamlit Cloud](https://dashboard-growth-brbank.streamlit.app)

---

## 💻 Como Rodar Localmente

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/dashboard-growth-brbank.git
cd dashboard-growth-brbank
