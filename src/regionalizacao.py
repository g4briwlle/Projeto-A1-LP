"""
Módulo de visualização dos datasets por região 
"""

import streamlit as st
import plotly.express as px
import cleaning as cl
import pandas as pd

# Carregando os datasets
cl.df_co2_pcap_limpo.bfill(inplace=True)
cl.df_mil_exp_limpo.bfill(inplace=True)
cl.df_gdp_total_limpo.bfill(inplace=True)

paises_norte = ["Albania", "Armenia", "Australia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Canada", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Israel", "Italy", "Japan", "Kazakhstan", "Latvia", "Lithuania", "Luxembourg", "Malta", "Moldova", "Montenegro", "Netherlands", "New Zealand", "Norway", "North Macedonia", "Poland", "Portugal", "Romania", "Russia", "Serbia", "Singapore", "Slovak Republic", "Slovenia", "South Korea", "Spain", "Sweden", "Switzerland", "Turkey", "UK", "Ukraine", "USA"]

paises_sul = ["Afghanistan", "Algeria", "Angola", "Argentina", "Bahrain", "Bangladesh", "Belize", "Benin", "Bolivia", "Botswana", "Brazil", "Brunei", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Cape Verde", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Congo, Dem. Rep.", "Congo, Rep.", "Cote d'Ivoire", "Cuba", "Djibouti", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Fiji", "Gabon", "Gambia", "Ghana", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "India", "Indonesia", "Iran", "Iraq", "Jamaica", "Jordan", "Kenya", "Kuwait", "Kyrgyz Republic", "Lao", "Lebanon", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Malaysia", "Mali", "Mauritania", "Mauritius", "Mexico", "Mongolia", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nepal", "Nicaragua", "Niger", "Nigeria", "Oman", "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Qatar", "Rwanda", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sri Lanka", "Sudan", "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Trinidad and Tobago", "Tunisia", "Turkmenistan", "UAE", "Uganda", "Uruguay", "Uzbekistan", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]

# Função para filtrar os dados por norte e sul
def filtrar_por_região(df, year, region):
    if region == "Norte":
        return df[df["country"].isin(paises_norte)][["country", str(year)]]
    elif region == "Sul":
        return df[df["country"].isin(paises_sul)][["country", str(year)]]


# Função para gerar mapas
def plot_regionalizacao(df, year, nome_dataset, regiao):

    df_por_regiao = filtrar_por_região(df, year, regiao)
    mapa_geral = px.choropleth(
        df_por_regiao,
        locations="country",
        locationmode="country names",
        color=str(year),
        hover_name="country",
        color_continuous_scale=px.colors.sequential.Plasma,
        title=f"{nome_dataset} - {regiao} ({year})")
    
    mapa_geral.update_layout(
        plot_bgcolor='#161A28',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            title_font_color='white',
            geo=dict(bgcolor='#161A28'),
            margin = dict(
                l=0,
                r=100,
                b=0,
                t=40,
                pad=4,
                autoexpand=False),
            height=300
    )
    return mapa_geral


def plot_regionalizacao_mapas(year):

    # Dados para o ano selecionado
    df_gdp_total_viz = cl.df_gdp_total_limpo[["country", str(year)]]
    df_co2_pcap_viz = cl.df_co2_pcap_limpo[["country", str(year)]]
    df_mil_exp_viz = cl.df_mil_exp_limpo[["country", str(year)]]

    # Removendo valores não numéricos ou nulos
    df_mil_exp_viz = df_mil_exp_viz[pd.to_numeric(df_mil_exp_viz[str(year)], errors="coerce").notnull()]
    
    # Transformando a série em numérica
    df_mil_exp_viz[str(year)] = pd.to_numeric(df_mil_exp_viz[str(year)], errors="coerce")

    # Adicionando título da página
    st.title(f"Datasets separados por Norte e Sul econômicos ({year})")

    # Mostrando os mapas
    st.subheader("Despesas Militares")

    mil_exp_norte, mil_exp_sul = st.columns(2)

    with mil_exp_norte:
        mapa_mil_exp_norte = plot_regionalizacao(df_mil_exp_viz, year, "Dados do SIPRI", "Norte")
        st.plotly_chart(mapa_mil_exp_norte, use_container_width=True)

    with mil_exp_sul:
        mapa_mil_exp_sul = plot_regionalizacao(df_mil_exp_viz, year, "Dados do SIPRI", "Sul")
        st.plotly_chart(mapa_mil_exp_sul, use_container_width=True)

    st.subheader("PIB (Dólares)")

    gdp_total_norte, gdp_total_sul = st.columns(2)

    with gdp_total_norte:
        mapa_gdp_norte = plot_regionalizacao(df_gdp_total_viz, year, "Dados do World Bank", "Norte")
        st.plotly_chart(mapa_gdp_norte, use_container_width=True)

    with gdp_total_sul:
        mapa_gdp_sul = plot_regionalizacao(df_gdp_total_viz, year, "Dados do World Bank", "Sul")
        st.plotly_chart(mapa_gdp_sul, use_container_width=True)

    st.subheader("Emissão de CO2 per Capita")

    co2_pcap_norte, co2_pcap_sul = st.columns(2)

    with co2_pcap_norte:
        mapa_co2_norte = plot_regionalizacao(df_co2_pcap_viz, year, "Dados do GM CO2 e CDIAC", "Norte")
        st.plotly_chart(mapa_co2_norte, use_container_width=True)

    with co2_pcap_sul:
        mapa_co2_sul = plot_regionalizacao(df_co2_pcap_viz, year, "Dados do GM CO2 e CDIAC", "Sul")
        st.plotly_chart(mapa_co2_sul, use_container_width=True)
        
    # Retornando todos os gráficos para verificar nos testes
    return mapa_mil_exp_norte, mapa_mil_exp_sul, mapa_gdp_norte, mapa_gdp_sul, mapa_co2_norte, mapa_co2_sul