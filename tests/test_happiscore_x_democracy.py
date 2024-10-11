import unittest
import pandas as pd
import plotly.express as px
import sys
import os

# Adicionar o diretório src ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src import happiscore_x_democracy as h_x_d
from src import cleaning as cl

class TestHappinessDemocracyVisualization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicializar os DataFrames
        cls.df_hapiscore_limpo = cl.df_hapiscore_limpo
        cls.df_democracy_limpo = cl.df_democracy_limpo

    def test_scatter_plot_generation(self):
        # Testar se o scatter plot é gerado corretamente
        year = 2020  # Por exemplo, o ano 2020
        df_hapiscore_viz = self.df_hapiscore_limpo[["country", str(year)]]
        df_democracy_viz = self.df_democracy_limpo[["country", str(year)]]

        scatter_plot = px.scatter(x=df_hapiscore_viz[str(year)],
                                  y=df_democracy_viz[str(year)],
                                  labels={"x": "Índice de Felicidade", "y": "Índice de Democracia"},
                                  hover_name=df_hapiscore_viz["country"],
                                  trendline="ols",
                                  title=f"Felicidade vs Democracia ({year})")

        # Verificar se o objeto do gráfico foi gerado corretamente
        self.assertIsNotNone(scatter_plot)
        self.assertEqual(scatter_plot.layout.title.text, f"Felicidade vs Democracia ({year})")

    def test_choropleth_map_generation(self):
        # Testar se o mapa coroplético é gerado corretamente
        year = 2020  # Por exemplo, o ano 2020
        df_hapiscore_viz = self.df_hapiscore_limpo[["country", str(year)]]

        happiness_map = px.choropleth(df_hapiscore_viz,
                                      locations="country",
                                      locationmode="country names",
                                      color=str(year),
                                      hover_name="country",
                                      color_continuous_scale=px.colors.sequential.Plasma,
                                      title="Dados do World Happiness Report")

        # Verificar se o objeto do gráfico foi gerado corretamente
        self.assertIsNotNone(happiness_map)
        self.assertEqual(happiness_map.layout.title.text, "Dados do World Happiness Report")

if __name__ == '__main__':
    unittest.main()