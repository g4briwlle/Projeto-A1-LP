import unittest
import pandas as pd
import sys
import os

# Adicionar o diretório src ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src import cleaning as cl

class TestCleaning(unittest.TestCase):
    
    def setUp(self):
        # Exemplo de dados que serão usados nos testes
        self.df_demo = pd.DataFrame({
            'Economy Name': ['Country1', 'Country2', 'United Arab Emirates'],
            '2005': [50, 60, 70],
            '2021': [55, 65, 75],
            '2022': [56, 66, 76],
            '2006': [57, 67, 77]
        })
        self.df_hap = pd.DataFrame({
            'country': ['Country1', 'Country2', 'Cabo Verde'],
            '2005': [40, 50, 60],
            '2021': [45, 55, 65],
            '2022': [46, 56, 66],
            '2006': [47, 57, 67]
        })
        
    def test_renomear_colunas(self):
        # Testar se a renomeação da coluna foi feita corretamente
        df_renomeado = self.df_demo.rename(columns={"Economy Name": "country"})
        self.assertIn("country", df_renomeado.columns)
        self.assertNotIn("Economy Name", df_renomeado.columns)

    def test_exclusao_anos(self):
        # Testar se os anos foram excluídos corretamente
        df_hap_clean = self.df_hap.drop(columns=["2005", "2021", "2022"])
        self.assertNotIn("2005", df_hap_clean.columns)
        self.assertIn("2006", df_hap_clean.columns)

    def test_substituicao_paises(self):
        # Testar a substituição de países
        alterar_paises = {'United Arab Emirates': 'UAE', 'Cabo Verde': None}
        df_substituido = self.df_hap.copy()
        df_substituido['country'] = df_substituido['country'].replace(alterar_paises)
        
        self.assertIn('UAE', df_substituido['country'].values)
        self.assertNotIn('Cabo Verde', df_substituido.dropna()['country'].values)
    
    def test_convertendo_grandezas_para_numerico(self):
        # Testar a conversão de grandezas para numéricos
        valores = ['10k', '5M', '2B', '3TR', 'NaN']
        valores_convertidos = [cleaning.convertendo_grandezas_para_numerico(v) for v in valores]
        
        self.assertEqual(valores_convertidos[0], 10000)
        self.assertEqual(valores_convertidos[1], 5000000)
        self.assertEqual(valores_convertidos[2], 2000000000)
        self.assertEqual(valores_convertidos[3], 3000000000000)
        self.assertTrue(pd.isna(valores_convertidos[4]))

if __name__ == '__main__':
    unittest.main()