"""
"""
from happiscore_x_democracy import plot_happiness_democracy
from mil_expend_x_gdp import plot_mil_exp_x_gdp_total
from co2_pcap_x_mil_exp import plot_co2_pcap_x_mil_exp
import streamlit as st
import cleaning as cl

# TODO Adicionar as outras visualizações

st.set_page_config(page_title="Análise de Felicidade e Democracia", layout="wide")

# Adicionando CSS
st.markdown("""
    <style>
    .main {
        color: white;
    }
    .stPlotlyChart {
        background-color: #161A28;
        border-radius: 15px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Barra lateral para seleção de análise
st.sidebar.title("Navegação")
analise_selecionada = st.sidebar.selectbox("Selecione a análise", ["Happiness vs Democracy", "Military Expenditure vs GDP", "Emissões de CO2 per Capita vs Military Expenditure", "OUTRAS ANÁLISES"])


# Modificando o que aparece na página de acordo com a análise escolhida pelo usuário
if analise_selecionada == "Happiness vs Democracy":
    ano = st.sidebar.slider(
    "Selecione o ano",
    min_value=int(min(cl.df_hapiscore_limpo.columns[1:])), 
    max_value=int(max(cl.df_hapiscore_limpo.columns[1:])),
    value=int(min(cl.df_hapiscore_limpo.columns[1:])),
    step=1)
    plot_happiness_democracy(ano)
elif analise_selecionada == "Military Expenditure vs GDP":
    ano = st.sidebar.slider(
    "Selecione o ano",
    min_value=int(min(cl.df_mil_exp_limpo.columns[1:])), 
    max_value=int(max(cl.df_mil_exp_limpo.columns[1:])),
    value=int(min(cl.df_mil_exp_limpo.columns[1:])),
    step=1)
    plot_mil_exp_x_gdp_total(ano)
elif analise_selecionada == "Emissões de CO2 per Capita vs Military Expenditure":
    ano = st.sidebar.slider(
    "Selecione o ano",
    min_value=int(min(cl.df_mil_exp_limpo.columns[1:])), 
    max_value=int(max(cl.df_mil_exp_limpo.columns[1:])),
    value=int(min(cl.df_mil_exp_limpo.columns[1:])),
    step=1)
    plot_co2_pcap_x_mil_exp(ano)
else:
    st.title("Outras Correlações")
    st.write("Colocar outras análises aqui")