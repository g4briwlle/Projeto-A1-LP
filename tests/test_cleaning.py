import unittest
import pandas as pd
import sys
import os

# Adicionar o diretório src ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src import cleaning as cl

class TestCleaning(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicializar os DataFrames das versões "limpas"
        
        cls.df_democracy_limpo = cl.df_democracy_limpo
        cls.df_hapiscore_limpo = cl.df_hapiscore_limpo
        cls.df_gdp_total_limpo = cl.df_gdp_total_limpo
        cls.df_mil_exp_limpo = cl.df_mil_exp_limpo
        cls.df_co2_pcap_limpo = cl.df_co2_pcap_limpo

    def test_remocao_anos(self):
        # Testar se os anos foram removidos corretamente de df_hapiscore e df_gdp_total
        anos_removidos = ["2005", "2021", "2022"]
        for ano in anos_removidos:
            self.assertNotIn(ano, self.df_hapiscore_limpo.columns)
        
        self.assertNotIn("2023", self.df_gdp_total_limpo.columns)

    def test_substituicao_paises(self):
        # Testar se as substituições de países foram feitas corretamente em df_democracy e df_hapiscore
        paises_esperados = ['UAE']  # Por exemplo, 'United Arab Emirates' virou 'UAE'
        self.assertIn('UAE', self.df_democracy_limpo['country'].values)
        self.assertIn('UAE', self.df_hapiscore_limpo['country'].values)

    def test_remocao_paises(self):
        # Testar se os países removidos foram corretamente excluídos (Cabo Verde, Micronesia, Kosovo etc.)
        paises_removidos = ['Cabo Verde', 'Micronesia', 'Kosovo']
        
        for pais in paises_removidos:
            self.assertNotIn(pais, self.df_democracy_limpo['country'].values)
            self.assertNotIn(pais, self.df_hapiscore_limpo['country'].values)
            self.assertNotIn(pais, self.df_mil_exp_limpo['country'].values)

    def test_format_final_dfs(self):
        # Verificar se os DataFrames finais (limpos) possuem os países em comum esperados
        paises_comuns_hap_dem = set(self.df_democracy_limpo['country']).intersection(set(self.df_hapiscore_limpo['country']))
        paises_comuns_mil_exp_gdp = set(self.df_mil_exp_limpo['country']).intersection(set(self.df_gdp_total_limpo['country']))
        paises_comuns_co2_mil_exp = set(self.df_mil_exp_limpo['country']).intersection(set(self.df_co2_pcap_limpo['country']))

        # Verificar se os DataFrames limpos mantêm apenas os países em comum
        self.assertEqual(set(self.df_democracy_limpo['country']), paises_comuns_hap_dem)
        self.assertEqual(set(self.df_mil_exp_limpo['country']), paises_comuns_mil_exp_gdp)
        self.assertEqual(set(self.df_co2_pcap_limpo['country']), paises_comuns_co2_mil_exp)

if __name__ == '__main__':
    unittest.main()