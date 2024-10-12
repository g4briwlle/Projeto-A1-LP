import unittest
import pandas as pd
import plotly.express as px
import sys
import os

# Adicionar o diretório src ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src import regionalizacao as reg
from src import cleaning as cl

class TestRegionalizacaoVisualization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicializar os DataFrames
        cls.df_gdp_total_limpo = cl.df_gdp_total_limpo
        cls.df_co2_pcap_limpo = cl.df_co2_pcap_limpo
        cls.df_mil_exp_limpo = cl.df_mil_exp_limpo

    def test_year_column_exists(self):
        # Verificar se a coluna do ano está presente nos DataFrames
        year = 2020  # Por exemplo, o ano 2020
        self.assertIn(str(year), self.df_gdp_total_limpo.columns)
        self.assertIn(str(year), self.df_co2_pcap_limpo.columns)
        self.assertIn(str(year), self.df_mil_exp_limpo.columns)

    def test_country_column_exists(self):
        # Verificar se a coluna 'country' está presente nos DataFrames
        self.assertIn('country', self.df_gdp_total_limpo.columns)
        self.assertIn('country', self.df_co2_pcap_limpo.columns)
        self.assertIn('country', self.df_mil_exp_limpo.columns)

    def test_regional_map_generation(self):
        # Testar se os mapas por região são gerados corretamente chamando a função de reg
        year = 2020  # Exemplo de ano
        (
            mapa_mil_exp_norte,
            mapa_mil_exp_sul,
            mapa_gdp_norte,
            mapa_gdp_sul,
            mapa_co2_norte,
            mapa_co2_sul
        ) = reg.plot_regionalizacao_mapas(year)

        # Verificar se os objetos dos gráficos foram gerados corretamente
        self.assertIsNotNone(mapa_mil_exp_norte)
        self.assertIsNotNone(mapa_mil_exp_sul)
        self.assertIsNotNone(mapa_gdp_norte)
        self.assertIsNotNone(mapa_gdp_sul)
        self.assertIsNotNone(mapa_co2_norte)
        self.assertIsNotNone(mapa_co2_sul)

        # Verificar os títulos dos gráficos
        self.assertEqual(mapa_mil_exp_norte.layout.title.text, f"Dados do SIPRI - Norte ({year})")
        self.assertEqual(mapa_mil_exp_sul.layout.title.text, f"Dados do SIPRI - Sul ({year})")
        self.assertEqual(mapa_gdp_norte.layout.title.text, f"Dados do World Bank - Norte ({year})")
        self.assertEqual(mapa_gdp_sul.layout.title.text, f"Dados do World Bank - Sul ({year})")
        self.assertEqual(mapa_co2_norte.layout.title.text, f"Dados do GM CO2 e CDIAC - Norte ({year})")
        self.assertEqual(mapa_co2_sul.layout.title.text, f"Dados do GM CO2 e CDIAC - Sul ({year})")

if __name__ == '__main__':
    unittest.main()
