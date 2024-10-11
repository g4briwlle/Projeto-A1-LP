"""
Módulo de visualização Military Expenditure x GDP per Capita
"""
import streamlit as st
import plotly.express as px
import cleaning as cl
import pandas as pd

# Preenchendo valores vazios com os anteriores
cl.df_gdp_total_limpo.bfill(inplace=True)
cl.df_mil_exp_limpo.bfill(inplace=True)

# Função para plotar os gráficos
def plot_mil_exp_x_gdp_total(year):

    # Dados para o ano selecionado
    df_gdp_total_viz = cl.df_gdp_total_limpo[["country", str(year)]]
    df_mil_exp_viz = cl.df_mil_exp_limpo[["country", str(year)]]
    
    # Removendo valores não numéricos ou nulos
    df_mil_exp_viz = df_mil_exp_viz[pd.to_numeric(df_mil_exp_viz[str(year)], errors="coerce").notnull()]
    
    # Transformando a série em numérica
    df_mil_exp_viz[str(year)] = pd.to_numeric(df_mil_exp_viz[str(year)], errors="coerce")
    
    # Verificando se o número de países é igual após a remoção de valores não numéricos/nulos
    df_gdp_total_viz = df_gdp_total_viz[df_gdp_total_viz["country"].isin(df_mil_exp_viz["country"])]
    df_mil_exp_viz = df_mil_exp_viz[df_mil_exp_viz["country"].isin(df_gdp_total_viz["country"])]


    st.title(f"Análise de Correlação entre PIB per Capita e Despesas Militares ({year})")

    # Gráfico de correlação
    scatter_plot = px.scatter(
        x=df_gdp_total_viz[str(year)],
        y=df_mil_exp_viz[str(year)],
        labels={"x": "PIB", "y": 'Despesas Militares'},
        hover_name=df_mil_exp_viz['country'],
        trendline="ols",
        title=f"PIB (Dólares) vs Despesas Militares (% do PIB) ({year})"
    )
    scatter_plot.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        title_font_color="white",
        legend_font_color="white",
        height=450
    )
    st.plotly_chart(scatter_plot, use_container_width=True)

    # Mapas coropléticos
    coluna_1, coluna_2 = st.columns(2)

    with coluna_1:
        st.subheader(f"Despesas Militares (% do PIB) ({year})")
        mil_expend_map = px.choropleth(
            df_mil_exp_viz,
            locations="country",
            locationmode='country names',
            color=str(year),
            hover_name="country",
            color_continuous_scale=px.colors.sequential.Plasma,
            range_color=(df_mil_exp_viz[str(year)].min(), df_mil_exp_viz[str(year)].max()),
            title="Military Expenditure Data"
        )
        mil_expend_map.update_layout(
            plot_bgcolor='#161A28',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            title_font_color='white',
            geo=dict(bgcolor='#161A28'),
            margin=dict(
                l=0,
                r=100,
                b=0,
                t=40,
                pad=4,
                autoexpand=False
            ),
            height=300
        )
        st.plotly_chart(mil_expend_map, use_container_width=True)

    with coluna_2:
        st.subheader(f"PIB (Dólares) ({year})")
        df_gdp_total_map = px.choropleth(df_gdp_total_viz,
                                        locations="country",
                                        locationmode='country names',
                                        color=str(year),
                                        hover_name="country",
                                        color_continuous_scale=px.colors.sequential.Plasma,
                                        title="Dados do World Bank"
        )
        df_gdp_total_map.update_layout(
            plot_bgcolor="#161A28",
            paper_bgcolor="rgba(0,0,0,0)",
            title_font_color="white",
            geo=dict(bgcolor="#161A28"),
            height=300,
            margin=dict(
                l=0,
                r=100,
                b=0,
                t=40,
                pad=4,
                autoexpand=False
            ),
        )
        st.plotly_chart(df_gdp_total_map, use_container_width=True)

