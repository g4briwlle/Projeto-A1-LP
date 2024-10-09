"""
"""
from happiscore_x_democracy import plot_happiness_democracy
import streamlit as st
import cleaning as cl

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
analise_selecionada = st.sidebar.selectbox("Selecione a análise", ["Happiness vs Democracy", "OUTRAS ANÁLISES"])

# Slider de ano
ano = st.sidebar.slider(
    "Selecione o ano",
    min_value=int(min(cl.df_hapiscore_limpo.columns[1:])), 
    max_value=int(max(cl.df_hapiscore_limpo.columns[1:])),
    value=int(min(cl.df_hapiscore_limpo.columns[1:])),
    step=1)


if analise_selecionada == "Happiness vs Democracy":
    plot_happiness_democracy(ano)
else:
    st.title("Outras Correlações")
    st.write("Colocar outras análises aqui")
