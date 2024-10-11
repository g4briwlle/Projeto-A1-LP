import unittest
import pandas as pd
import plotly.express as px
import sys
import os

# Adicionar o diretório src ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src import co2_pcap_x_mil_exp as c_x_m
from src import cleaning as cl

class TestCo2PcapXMilExpVisualization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicializar os DataFrames
        cls.df_co2_pcap_limpo = cl.df_co2_pcap_limpo
        cls.df_mil_exp_limpo = cl.df_mil_exp_limpo

    def test_scatter_plot_generation(self):
        # Testar se o scatter plot é gerado corretamente chamando a função de c_x_m
        year = 2020  # Por exemplo, o ano 2020
        scatter_plot, _, _ = c_x_m.plot_co2_pcap_x_mil_exp(year)  # Chamando a função diretamente do módulo

        # Verificar se o objeto do gráfico foi gerado corretamente
        self.assertIsNotNone(scatter_plot)
        self.assertEqual(scatter_plot.layout.title.text, f" CO2 per Capita vs Despesas Militares (% do PIB) ({year})")

    def test_choropleth_map_generation(self):
        # Testar se os mapas coropléticos são gerados corretamente chamando a função de c_x_m
        year = 2020
        _, co2_pcap_map, df_mil_exp_map = c_x_m.plot_co2_pcap_x_mil_exp(year)  # Chamando a função diretamente do módulo

        # Verificar se os objetos do gráfico foram gerados corretamente
        self.assertIsNotNone(co2_pcap_map)
        self.assertIsNotNone(df_mil_exp_map)
        self.assertEqual(co2_pcap_map.layout.title.text, "Dados do GM CO2 e CDIAC")
        self.assertEqual(df_mil_exp_map.layout.title.text, "Dados do Stockholm International Peace Research Institute (SIPRI)")

if __name__ == '__main__':
    unittest.main()