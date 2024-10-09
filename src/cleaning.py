""" 
Módulo de limpeza dos datasets
"""

# TODO Fazer limpeza dos outros datasets

import pandas as pd
import os

# Criando os caminhos completos para os arquivos
hapiscore_path = os.path.join('data', 'hapiscore_whr_original.csv')
democracy_path = os.path.join('data', 'democracy_rate_EIU_original.xlsx')
aid_received_path = os.path.join('data', 'aid_received_total_us_inflation_adjusted.csv')
gdp_pcap_path = os.path.join('data', 'gdp_pcap.csv')
military_path = os.path.join("data", "military_expenditure_percent_of_gdp.csv")

# Carregando os arquivos
df_hapiscore_original = pd.read_csv(hapiscore_path)
df_democracy_original = pd.read_excel(democracy_path)
df_aid_received_original = pd.read_csv(aid_received_path)
df_gpd_pcap_original = pd.read_csv(gdp_pcap_path)
df_military_original = pd.read_csv(military_path)

df_democracy = df_democracy_original.copy()
df_hapiscore = df_hapiscore_original.copy()
df_aid_received = df_aid_received_original.copy()
df_gpd_pcap = df_gpd_pcap_original.copy()
df_military = df_military_original.copy()


# Igualando os nomes das colunas
df_democracy = df_democracy.rename(columns={"Economy Name": "country"})


# Excluindo anos de 2005, 2021 e 2021 pois o dataset de democracy não possui dados nesses anos
df_hapiscore = df_hapiscore.drop(columns=["2005", "2021", "2022"])


# Lista dos países que serão alterados nos datasets
alterar_paises = {
    'United Arab Emirates': 'UAE',
    'Cabo Verde': None,  
    'Czechia': 'Czech Republic',
    'Egypt, Arab Rep.': 'Egypt',
    'Eritrea': None,  
    'Fiji': None,  
    'United Kingdom': 'UK',
    'Gambia, The': 'Gambia',
    'Guinea-Bissau': None,  
    'Equatorial Guinea': None,  
    'Hong Kong SAR, China': 'Hong Kong, China',
    'Iran, Islamic Rep.': 'Iran',
    'Korea, Rep.': 'South Korea',
    'Lao PDR': 'Lao',
    'Papua New Guinea': None,  
    "Korea, Dem. People's Rep.": None,  
    'West Bank and Gaza': 'Palestine',
    'Russian Federation': 'Russia',
    'Syrian Arab Republic': 'Syria',
    'Timor-Leste': None,  
    'Turkiye': 'Turkey',
    'Taiwan, China': 'Taiwan',
    'United States': 'USA',
    'Venezuela, RB': 'Venezuela',
    'Yemen, Rep.': 'Yemen'
}

# Aplicando as correções de nomes no dataset de democracia
df_democracy["country"] = df_democracy["country"].replace(alterar_paises)

# Removendo os países que são 'None' (que não devem estar nos dois datasets)
df_democracy = df_democracy.dropna(subset=["country"])

# Aplicando as correções de nomes no dataset hapiscore
df_hapiscore["country"] = df_hapiscore["country"].replace(alterar_paises)

# Removendo os países que são 'None' do dataset hapiscore
df_hapiscore = df_hapiscore.dropna(subset=["country"])

# Filtrando os datasets para manter apenas os países presentes em ambos
paises_comuns = set(df_democracy["country"]).intersection(set(df_hapiscore["country"]))

# Criando datasets limpos com os valores extraídos
df_democracy_limpo = df_democracy[df_democracy["country"].isin(paises_comuns)].copy()
df_hapiscore_limpo = df_hapiscore[df_hapiscore["country"].isin(paises_comuns)].copy()


if __name__ == "__main__":
    print(df_democracy_limpo)
    print(df_hapiscore_limpo)

