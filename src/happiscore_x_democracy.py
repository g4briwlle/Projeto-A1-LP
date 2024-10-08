"""
Módulo de visualização Happiscore x Democracy
"""
import plotly.express as px
import cleaning as cl



def happiscore_x_democracy():
    """
    Função que exibe a visualização dos datasets "Hapiscore" e "Democracy Index"

    """
    # Preenchendo valores vazios com os anteriores
    cl.df_hapiscore_limpo.fillna(method="ffill", inplace=True)
    cl.df_democracy_limpo.fillna(method="ffill", inplace=True)

    # Selecionando a coluna de felicidade e o país
    df_viz = cl.df_hapiscore_limpo[['country', '2020']] 

    # Criando um mapa coroplético 
    fig = px.choropleth(df_viz,
                        locations="country",  
                        locationmode='country names',
                        color="2020", 
                        hover_name="country", 
                        color_continuous_scale=px.colors.sequential.Plasma, 
                        title="Índice de Felicidade por País (2020)")

    # Exibindo o mapa
    fig.show()

    # TODO Adicionar argumentos e "returns" no docstring da função
    # TODO Adicionar filtro para ano
    # TODO Adicionar visualização do dataset democracy com hapiscore
    # TODO Adicionar outra forma de visualização conjunta (talvez um gráfico convencional mesmo)

