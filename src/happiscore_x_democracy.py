"""
Módulo de visualização Happiscore x Democracy
"""
import streamlit as st
import plotly.express as px
import cleaning as cl

# TODO Melhorar design da página

# Preenchendo valores vazios com os anteriores
cl.df_hapiscore_limpo.fillna(method="ffill", inplace=True)
cl.df_democracy_limpo.fillna(method="ffill", inplace=True)


# Função para plotar os gráficos
def plot_happiness_democracy(year):
    # Dados para o ano selecionado
    df_hapiscore_viz = cl.df_hapiscore_limpo[['country', str(year)]]
    df_democracy_viz = cl.df_democracy_limpo[['country', str(year)]]

    st.title(f"Análise de Correlação entre Felicidade e Democracia ({year})")
    
    # Gráfico de correlação
    scatter_plot = px.scatter(x=df_hapiscore_viz[str(year)],
                              y=df_democracy_viz[str(year)],
                              labels={'x': 'Índice de Felicidade', 'y': 'Índice de Democracia'},
                              hover_name=df_hapiscore_viz['country'],
                              trendline="ols",
                              title=f"Felicidade x Democracia ({year})")
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
        happiness_map = px.choropleth(df_hapiscore_viz,
                                      locations="country",
                                      locationmode='country names',
                                      color=str(year),
                                      hover_name="country",
                                      color_continuous_scale=px.colors.sequential.Plasma,
                                      title="Dados do World Happiness Report")
        happiness_map.update_layout(
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
        st.plotly_chart(happiness_map, use_container_width=True)

    with col2:
        st.subheader(f"Índice de Democracia ({year})")
        democracy_map = px.choropleth(df_democracy_viz,
                                      locations="country",
                                      locationmode='country names',
                                      color=str(year),
                                      hover_name="country",
                                      color_continuous_scale=px.colors.sequential.Plasma,
                                      title="Dados do Economist Inteligence Unit")
        democracy_map.update_layout(
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
        st.plotly_chart(democracy_map, use_container_width=True)
