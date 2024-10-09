""" Módulo de limpeza dos datasets
"""

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
# df_democracy.to_csv("democracy_rate_EIU_2.csv", index = False)

df_democracy = df_democracy_original.copy()
df_hapiscore = df_hapiscore_original.copy()
df_aid_received = df_aid_received_original.copy()
df_gpd_pcap = df_gpd_pcap_original.copy()
df_military = df_military_original.copy()

# Decidi manipular df_democracy para usá-lo nos moldes de df_hapiscore, que é mais simples

# Igualando os nomes das colunas
df_democracy = df_democracy.rename(columns={"Economy Name": "country"})

# Excluindo colunas desnecessárias
df_democracy = df_democracy.drop(columns=["Economy ISO3", "Indicator ID", "Indicator", "Attribute 1", "Attribute 2", "Attribute 3", "Partner"])

# Excluindo dados do ano 2005 de df_hapiscore pois o índice de democracia EIU foi criado em 2006
df_hapiscore = df_hapiscore.drop(columns=["2005"])

# Analisando países divergentes (a diferença da amostra de países analisados em cada dataset):
# Printei esse resultado para fazer comparações e adicionei as modificações necessárias em listas e dicionários
pais_fora_da_intersecao_ida = [pais for pais in list(df_democracy["country"]) if pais not in list(df_hapiscore["country"])]
pais_fora_da_intersecao_volta =[pais for pais in list(df_hapiscore["country"]) if pais not in list(df_democracy["country"])]

# Tratando países com nomes diferentes :
alterar_em_democracy = {
    'Egypt, Arab Rep.' : 'Egypt',
    'Gambia, The' : 'Gambia',
    'Hong Kong SAR, China' : 'Hong Kong, China',
    'Iran, Islamic Rep.' : 'Iran',
    'Korea, Rep.' : 'South Korea',
    'Lao PDR' : 'Lao',
    'West Bank and Gaza' : 'Palestine',
    'Russian Federation' : 'Russia',
    'Syrian Arab Republic' : 'Syria',
    'Taiwan, China' : 'Taiwan',
    'Venezuela, RB' : 'Venezuela',
    'Yemen, Rep.' : 'Yemen'
}

alterar_em_hapiscore = {
    "Czech Republic" : "Czechia",
    'UK' : 'United Kingdom',
    'Turkey' : 'Turkiye',
    'USA' : 'United States'
}

# Tratando países que estão em uma base mas não estão em outra:
apagar_em_democracy = [
    "Cabo Verde",
    'Eritrea', 
    'Fiji',
    'Guinea-Bissau',
    'Equatorial Guinea',
    'Papua New Guinea',
    "Korea, Dem. People's Rep.",
    'Timor-Leste'
]

apagar_em_hapiscore = [
    'Belize',
    'Somalia', 
    'South Sudan'
]

# Alterar os nomes de países que divergem (ex: EUA e Estados Unidos)
df_democracy["country"] = df_democracy["country"].replace(alterar_em_democracy)
df_hapiscore["country"] = df_hapiscore["country"].replace(alterar_em_hapiscore)

# Filtrar as linhas que correspondem a países que estão em uma base de dados e não estão em outra,
# para isso se verifica as interseções
linhas_para_mover_hapiscore = df_hapiscore[df_hapiscore['country'].isin(apagar_em_hapiscore)]
linhas_para_mover_democracy = df_democracy[df_democracy['country'].isin(apagar_em_democracy)]

# Converter essas linhas para uma lista de dicionários para armazenar esses dados em df_hapiscore
# e df_democracy. Teremos os dfs limpos sem esses países fora da interseção.
dict_linhas_removidas_hapiscore = linhas_para_mover_hapiscore.to_dict(orient='records')
dict_linhas_removidas_democracy = linhas_para_mover_democracy.to_dict(orient='records')

df_hapiscore_limpo = df_hapiscore.copy()
df_democracy_limpo = df_democracy.copy()

# Remover essas linhas do DataFrame
df_hapiscore_limpo = df_hapiscore_limpo[~df_hapiscore['country'].isin(apagar_em_hapiscore)]
df_democracy_limpo = df_democracy_limpo[~df_democracy['country'].isin(apagar_em_democracy)]


if __name__ == "__main__":
    # visualizar datasets
    #print(df_democracy.head(15), df_hapiscore.head(15))
    print(len(df_hapiscore.index))
    print(pais_fora_da_intersecao_ida, "#",  pais_fora_da_intersecao_volta, sep="\n")
    print("Dados movidos para a lista:")
    print(dict_linhas_removidas_hapiscore)