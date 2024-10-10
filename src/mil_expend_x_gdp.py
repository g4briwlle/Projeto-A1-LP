"""
Módulo de visualização Military Expenditure x GDP per Capita
"""
import streamlit as st
import plotly.express as px
import cleaning as cl

# TODO Melhorar design da página

# Preenchendo valores vazios com os anteriores
cl.df_gdp_pcap_limpo.fillna(method="ffill", inplace=True)
cl.df_mil_exp_limpo.fillna(method="ffill", inplace=True)


# Função para plotar os gráficos
def plot_mil_exp_x_gdp_pcap(year):
    # Dados para o ano selecionado
    df_gdp_pcap_viz = cl.df_gdp_pcap_limpo[['country', str(year)]]
    df_mil_exp_viz = cl.df_mil_exp_limpo[['country', str(year)]]

    st.title(f"Análise de Correlação entre PIB per Capita e Military Expenditure ({year})")
    
    # Gráfico de correlação
    scatter_plot = px.scatter(x=df_gdp_pcap_viz[str(year)],
                              y=df_mil_exp_viz[str(year)],
                              labels={'x': 'PIB per Capita', 'y': 'Military Expenditure'},
                              hover_name=df_gdp_pcap_viz['country'],
                              trendline="ols",
                              title=f"GDP per Capita x Military Expenditure ({year})")
    scatter_plot.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title_font_color='white',
        legend_font_color='white',
        height=450
    )
    st.plotly_chart(scatter_plot, use_container_width=True)

    # Mapas coropléticos
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Índice de Felicidade ({year})")
        mil_expend_map = px.choropleth(df_mil_exp_viz,
                                      locations="country",
                                      locationmode='country names',
                                      color=str(year),
                                      hover_name="country",
                                      color_continuous_scale=px.colors.sequential.Plasma,
                                      title="Dados do World Happiness Report")
        mil_expend_map.update_layout(
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
        st.plotly_chart(mil_expend_map, use_container_width=True)

    with col2:
        st.subheader(f"PIB per Capita ({year})")
        df_gdp_pcap_map = px.choropleth(df_gdp_pcap_viz,
                                      locations="country",
                                      locationmode='country names',
                                      color=str(year),
                                      hover_name="country",
                                      color_continuous_scale=px.colors.sequential.Plasma,
                                      title="Dados do Economist Inteligence Unit")
        df_gdp_pcap_map.update_layout(
            plot_bgcolor='#161A28',
            paper_bgcolor='rgba(0,0,0,0)',
            title_font_color='white',
            geo=dict(bgcolor='#161A28'),
            height=300,
                margin = dict(
                l=0,
                r=100,
                b=0,
                t=40,
                pad=4,
                autoexpand=False),
        )
        st.plotly_chart(df_gdp_pcap_map, use_container_width=True)
