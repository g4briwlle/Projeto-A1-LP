"""
Módulo de visualização Happiscore x Democracy
"""
import streamlit as st
import plotly.express as px
import cleaning as cl
import pandas as pd


# Preenchendo valores vazios com os anteriores
cl.df_co2_pcap_limpo.bfill(inplace=True)
cl.df_mil_exp_limpo.bfill(inplace=True)


# Função para plotar os gráficos
def plot_co2_pcap_x_mil_exp(year):

    # Dados para o ano selecionado
    df_co2_pcap_viz = cl.df_co2_pcap_limpo[["country", str(year)]]
    df_mil_exp_viz = cl.df_mil_exp_limpo[["country", str(year)]]

    # Adicionando título da página
    st.title(f"Análise de Correlação entre emissões de CO2 com despesas militares ({year})")
    
    # Gráfico de correlação
    scatter_plot = px.scatter(
        x=df_mil_exp_viz[str(year)],
        y=df_co2_pcap_viz[str(year)],
        labels={"x": "Despesas militares (% do PIB)", "y": "Emissões de CO2 (Toneladas)"},
        hover_name=df_mil_exp_viz["country"],
        trendline="ols",
        title=f"CO2 per Capita (Toneladas) vs Despesas Militares (% do PIB) ({year})")
    
    scatter_plot.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        title_font_color="white",
        legend_font_color="white",
        height=450
    )
    st.plotly_chart(scatter_plot, use_container_width=True)

    # Mapas coropléticos
    co2_pcap_column, mil_exp_column = st.columns(2)

    with co2_pcap_column:
        st.subheader(f"Emissão de CO2 per Capita (Toneladas) ({year})")
        co2_pcap_map = px.choropleth(
            df_co2_pcap_viz,
            locations="country",
            locationmode="country names",
            color=str(year),
            hover_name="country",
            color_continuous_scale=px.colors.sequential.Plasma,
            title="Dados do GM CO2 e CDIAC")
        
        co2_pcap_map.update_layout(
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
        st.plotly_chart(co2_pcap_map, use_container_width=True)

    with mil_exp_column:
        st.subheader(f"Despesas Militares (% do PIB) ({year})")
        df_mil_exp_map = px.choropleth(
            df_mil_exp_viz,
            locations="country",
            locationmode='country names',
            color=str(year),
            hover_name="country",
            color_continuous_scale=px.colors.sequential.Plasma,
            title="Dados do Stockholm International Peace Research Institute (SIPRI)")
        
        df_mil_exp_map.update_layout(
            plot_bgcolor="#161A28",
            paper_bgcolor="rgba(0,0,0,0)",
            title_font_color="white",
            geo=dict(bgcolor="#161A28"),
            height=300,
                margin = dict(
                l=0,
                r=100,
                b=0,
                t=40,
                pad=4,
                autoexpand=False),
        )

        st.plotly_chart(df_mil_exp_map, use_container_width=True)
