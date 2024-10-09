"""
Módulo de visualização Happiscore x Democracy
"""

# TODO Melhorar design da página
# TODO Selecionar cores para os plots e textos

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import cleaning as cl
import plotly.graph_objects as go

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
            dcc.Graph(id='happiness-map', 
                       config={'displayModeBar': False}, 
                       style={'height': '100%', 'width': '100%'}
                      ),
        ], className='graph-container'),
        
        html.Div([
            dcc.Graph(id='democracy-map', 
                       config={'displayModeBar': False}, 
                       style={'height': '100%', 'width': '100%'}
                      ),
        ], className='graph-container'),
    ], className='flex-container'),
    
    html.Div([
        dcc.Graph(
            id='scatter-plot',
            config={'displayModeBar': False}, 
            style={'height': '100%', 'width': '100%'}
        )
    ], className='graph-container'),
], 
style={
    'padding': '20px',
    'background-color': '#161A28',
    'font-family': 'sans-serif',
})


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
    happiness_map.update_layout(
        plot_bgcolor='#161A28',
        paper_bgcolor='#161A28',
        font_color='white',
        title_font_color='white',
        geo=dict(bgcolor='#161A28')
    )
    
    # Mapa coroplético para índice de democracia
    democracy_map = px.choropleth(df_democracy_viz,
                                  locations="country",
                                  locationmode='country names',
                                  color=year,
                                  hover_name="country",
                                  color_continuous_scale=px.colors.sequential.Plasma,
                                  title=f"Índice de Democracia por País ({year})")
    democracy_map.update_layout(
        plot_bgcolor='#161A28',
        paper_bgcolor='#161A28',
        title_font_color='white',
        geo=dict(bgcolor='#161A28')
    )
    
    # Gráfico de dispersão
    scatter_plot = px.scatter(
        x=df_hapiscore_viz[year],
        y=df_democracy_viz[year],
        labels={'x': 'Índice de Felicidade', 'y': 'Índice de Democracia'},
        hover_name=df_hapiscore_viz['country'],
        trendline="ols",
        title=f"Correlação Felicidade vs Democracia ({year})",
        color_discrete_sequence=['orange']  # Cor dos pontos
    )
    
    scatter_plot.update_layout(
        plot_bgcolor='#161A28',
        paper_bgcolor='#161A28',
        font_color='white',
        title_font_color='white',
        legend_font_color='white',
        xaxis=dict(color='white'),  
        yaxis=dict(color='white')   
    )

    scatter_plot.update_traces(marker=dict(size=7, color='orange'))  

    return happiness_map, democracy_map, scatter_plot


if __name__ == '__main__':
    app.run_server(debug=True)
