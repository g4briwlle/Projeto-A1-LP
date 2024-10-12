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
        # Testar se o scatter plot é gerado corretamente chamando a função de h_x_d
        year = 2020  # Por exemplo, o ano 2020
        scatter_plot, _, _ = h_x_d.plot_happiness_democracy(year)  # Chamando a função diretamente do módulo

        # Verificar se o objeto do gráfico foi gerado corretamente
        self.assertIsNotNone(scatter_plot)
        self.assertEqual(scatter_plot.layout.title.text, f"Felicidade vs Democracia ({year})")

    def test_choropleth_map_generation(self):
        # Testar se o mapa coroplético (choropleth) é gerado corretamente chamando a função de h_x_d
        year = 2020
        _, happiness_map, democracy_map = h_x_d.plot_happiness_democracy(year)  # Chamando a função diretamente do módulo

        # Verificar se os objetos do gráfico foram gerados corretamente
        self.assertIsNotNone(happiness_map)
        self.assertIsNotNone(democracy_map)
        self.assertEqual(happiness_map.layout.title.text, "Dados do World Happiness Report")
        self.assertEqual(democracy_map.layout.title.text, "Dados do Economist Inteligence Unit")

if __name__ == '__main__':
    unittest.main()
