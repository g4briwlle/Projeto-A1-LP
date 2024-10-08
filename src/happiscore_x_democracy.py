"""
Módulo de visualização Happiscore x Democracy
"""
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import cleaning as cl
import plotly.graph_objects as go

# TODO Mudar a cor de background dos gráficos
# TODO Melhorar design da página
# TODO Selecionar cores para os plots e textos


# Preenchendo valores vazios com os anteriores
cl.df_hapiscore_limpo.fillna(method="ffill", inplace=True)
cl.df_democracy_limpo.fillna(method="ffill", inplace=True)

# Iniciando o Dash
app = dash.Dash(__name__)

# Selecionando os anos disponíveis
available_years = [col for col in cl.df_hapiscore_limpo.columns if col != 'country']

# Layout da página
app.layout = html.Div([
    html.H1("Comparação de Índice de Felicidade e Democracia por País", style={'color': 'white'}),
    
    dcc.Slider(
        id='year-slider',
        min=int(min(available_years)),
        max=int(max(available_years)),
        value=int(available_years[0]),
        marks={int(year): year for year in available_years},
        step=None,
    ),
    
    html.Div([
        html.Div([
            dcc.Graph(id='happiness-map'),
        ], style={
            'flex': '1',
            'background-color': '#161A28',
            'border-radius': '15px',
            'padding': '20px',
            'margin': '10px'
        }),
        
        html.Div([
            dcc.Graph(id='democracy-map'),
        ], style={
            'flex': '1',
            'background-color': '#161A28',
            'border-radius': '15px',
            'padding': '20px',
            'margin': '10px'
        }),
    ], style={
        'display': 'flex',
        'justify-content': 'space-between',
        'align-items': 'stretch',
    }),
    
    html.Div([
        dcc.Graph(id='scatter-plot'),
    ], style={
        'width': '100%',
        'background-color': '#161A28',
        'border-radius': '15px',
        'padding': '20px',
        'margin': '10px',
        'font-family': 'sans-serif',
    }),
], style={
    'background-color': '#161A28',
    'padding': '20px',
    'font-family': 'sans-serif',
    'text-align': 'center',
})


# Função para criar o mapa coroplético e gráfico de dispersão com base no ano
@app.callback(
    [Output('happiness-map', 'figure'),
     Output('democracy-map', 'figure'),
     Output('scatter-plot', 'figure')],
    [Input('year-slider', 'value')]
)
def update_graphs(selected_year):
    """
    Função que faz o update dos gráficos coropléticos e do gráfico de dispersão com base no ano escolhido no slider

    Args:
        selected_year: 

    Returns:
        happiness_map:
        democracy_map:
        scatter_plot:
    """
    year = str(selected_year)
    
    # Dados para felicidade e democracia
    df_hapiscore_viz = cl.df_hapiscore_limpo[['country', year]]
    df_democracy_viz = cl.df_democracy_limpo[['country', year]]
    
    # Mapa coroplético para índice de felicidade
    happiness_map = px.choropleth(df_hapiscore_viz,
                                  locations="country",
                                  locationmode='country names',
                                  color=year,
                                  hover_name="country",
                                  color_continuous_scale=px.colors.sequential.Plasma,
                                  title=f"Índice de Felicidade por País ({year})")
    
    # Mapa coroplético para índice de democracia
    democracy_map = px.choropleth(df_democracy_viz,
                                  locations="country",
                                  locationmode='country names',
                                  color=year,
                                  hover_name="country",
                                  color_continuous_scale=px.colors.sequential.Plasma,
                                  title=f"Índice de Democracia por País ({year})")
    
    # Gráfico de dispersão
    scatter_plot = px.scatter(x=df_hapiscore_viz[year],
                              y=df_democracy_viz[year],
                              labels={'x': 'Índice de Felicidade', 'y': 'Índice de Democracia'},
                              hover_name=df_hapiscore_viz['country'],
                              trendline="ols",
                              title=f"Correlação Felicidade vs Democracia ({year})")
    
    return happiness_map, democracy_map, scatter_plot


if __name__ == '__main__':
    app.run_server()
