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


st.set_page_config(page_title="Análise de Felicidade e Democracia", layout="wide")

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

# Dados para o ano selecionado
df_hapiscore_viz = cl.df_hapiscore_limpo[['country', str(ano)]]
df_democracy_viz = cl.df_democracy_limpo[['country', str(ano)]]

if analise_selecionada == "Happiness vs Democracy":
    st.title(f"Análise de Correlação entre Felicidade e Democracia ({ano})")
    
    # Gráfico de correlação
    scatter_plot = px.scatter(x=df_hapiscore_viz[str(ano)],
                              y=df_democracy_viz[str(ano)],
                              labels={'x': 'Índice de Felicidade', 'y': 'Índice de Democracia'},
                              hover_name=df_hapiscore_viz['country'],
                              trendline="ols",
                              title=f"Felicidade x Democracia ({ano})")
    scatter_plot.update_layout(
        plot_bgcolor='#161A28',
        paper_bgcolor='#161A28',
        title_font_color='white',
        legend_font_color='white'
    )
    st.plotly_chart(scatter_plot, use_container_width=True)

    # Mapas coropléticos
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Índice de Felicidade ({ano})")
        happiness_map = px.choropleth(df_hapiscore_viz,
                                      locations="country",
                                      locationmode='country names',
                                      color=str(ano),
                                      hover_name="country",
                                      color_continuous_scale=px.colors.sequential.Plasma,
                                      title=f"Índice de Felicidade por País ({ano})")
        happiness_map.update_layout(
            plot_bgcolor='#161A28',
            paper_bgcolor='#161A28',
            font_color='white',
            title_font_color='white',
            geo=dict(bgcolor='#161A28')
        )
        st.plotly_chart(happiness_map, use_container_width=True)

    with col2:
        st.subheader(f"Índice de Democracia ({ano})")
        democracy_map = px.choropleth(df_democracy_viz,
                                      locations="country",
                                      locationmode='country names',
                                      color=str(ano),
                                      hover_name="country",
                                      color_continuous_scale=px.colors.sequential.Plasma,
                                      title=f"Índice de Democracia por País ({ano})")
        democracy_map.update_layout(
            plot_bgcolor='#161A28',
            paper_bgcolor='#161A28',
            title_font_color='white',
            geo=dict(bgcolor='#161A28')
        )
        st.plotly_chart(democracy_map, use_container_width=True)

else:
    st.title("Outras Correlações")
    st.write("Colocar outras análises aqui")
