import unittest
import pandas as pd
import sys
import os
from src import cleaning as cl
import plotly.express as px

# Adicionar o diretório src ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src import mil_expend_x_gdp as m_x_g
from src import cleaning as cl

class TestMilitaryExpenditureXGdpVisualization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicializar os DataFrames
        cls.df_gdp_total_limpo = cl.df_gdp_total_limpo
        cls.df_mil_exp_limpo = cl.df_mil_exp_limpo

    def test_scatter_plot_generation(self):
        # Testar se o scatter plot é gerado corretamente chamando a função de m_x_g
        year = 2020  # Por exemplo, o ano 2020
        scatter_plot, _, _ = m_x_g.plot_mil_exp_x_gdp_total(year)

        # Verificar se o objeto do gráfico foi gerado corretamente
        self.assertIsNotNone(scatter_plot)
        self.assertEqual(scatter_plot.layout.title.text, f"PIB (Dólares) vs Despesas Militares (% do PIB) ({year})")

    def test_choropleth_map_generation(self):
        # Testar se os mapas coropléticos são gerados corretamente chamando a função de m_x_g
        year = 2020
        _, mil_expend_map, df_gdp_total_map = m_x_g.plot_mil_exp_x_gdp_total(year) 

        # Verificar se os objetos do gráfico foram gerados corretamente
        self.assertIsNotNone(mil_expend_map)
        self.assertIsNotNone(df_gdp_total_map)
        self.assertEqual(mil_expend_map.layout.title.text, "Dados do Stockholm International Peace Research Institute (SIPRI)")
        self.assertEqual(df_gdp_total_map.layout.title.text, "Dados do World Bank")

if __name__ == '__main__':
    unittest.main()