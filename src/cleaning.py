""" 
Módulo de limpeza dos datasets
"""

# TODO Fazer limpeza dos outros datasets

import pandas as pd

df_hapiscore_original = pd.read_csv("../data/hapiscore_whr_original.csv")
df_democracy_original = pd.read_csv("../data/demox_eiu.csv")
df_aid_received_original = pd.read_csv("../data/aid_received_per_person_current_us.csv")
df_gdp_pcap = pd.read_csv("../data/gdp_pcap.csv")
df_military_original = pd.read_csv("../data/military_expenditure_percent_of_gdp.csv")


df_democracy = df_democracy_original.copy()
df_hapiscore = df_hapiscore_original.copy()
df_gdp_pcap = df_gdp_pcap.copy()
df_mil_exp = df_military_original.copy()

# Igualando os nomes das colunas
df_democracy = df_democracy.rename(columns={"Economy Name": "country"})


# Excluindo anos que não estão na interseção dos datasets
df_hapiscore = df_hapiscore.drop(columns=["2005", "2021", "2022"])

anos_apagados = []
for year in range(1800, 1960):
    anos_apagados.append(str(year))
for year in range(2023, 2101):
    anos_apagados.append(str(year))
df_gpd_pcap = df_gdp_pcap.drop(columns=anos_apagados)

# Lista dos países que serão alterados nos datasets
alterar_paises_happiness_x_democracy = {
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

# Lista dos países que serão alterados nos datasets
alterar_paises_mil_exp_x_gdp = {
    'Micronesia': None,
    'Kosovo': None,
    'Andorra': None,
    'Antigua and Barbuda': None,
    'Bahamas': None,
    'Barbados': None,
    'Bhutan': None,
    'Comoros': None,
    'Costa Rica': None,
    'Dominica': None,
    'Micronesia, Fed. Sts.': None,
    'Grenada': None,
    'Hong Kong, China': None,
    'Iceland': None,
    'Kiribati': None,
    'St. Kitts and Nevis': None,
    'St. Lucia': None,
    'Monaco': None,
    'Maldives': None,
    'Marshall Islands': None,
    'Nauru': None,
    'Palau': None,
    'North Korea': None,
    'Palestine': None,
    'Solomon Islands': None,
    'San Marino': None,
    'Sao Tome and Principe': None,
    'Suriname': None,
    'Tonga': None,
    'Tuvalu': None,
    'Taiwan': None,
    'St. Vincent and the Grenadines': None,
    'Vanuatu': None,
    'Samoa': None,
}

# Aplicando as correções de nomes nos datasets
df_democracy["country"] = df_democracy["country"].replace(alterar_paises_happiness_x_democracy)
df_hapiscore["country"] = df_hapiscore["country"].replace(alterar_paises_happiness_x_democracy)

df_mil_exp["country"] = df_mil_exp["country"].replace(alterar_paises_mil_exp_x_gdp)
df_gdp_pcap["country"] = df_gdp_pcap["country"].replace(alterar_paises_mil_exp_x_gdp)

# Removendo os países que são 'None' (que não devem estar nos dois datasets)
df_democracy = df_democracy.dropna(subset=["country"])
df_gdp_pcap = df_gpd_pcap.dropna(subset=["country"])
df_mil_exp = df_mil_exp.dropna(subset=["country"])
df_hapiscore = df_hapiscore.dropna(subset=["country"])

# Filtrando os datasets para manter apenas os países presentes em ambos
paises_comuns_hap_dem = set(df_democracy["country"]).intersection(set(df_hapiscore["country"]))
paises_comuns_mil_exp_gdp = set(df_mil_exp["country"]).intersection(set(df_gdp_pcap["country"]))

# Criando datasets limpos com os valores extraídos
df_democracy_limpo = df_democracy[df_democracy["country"].isin(paises_comuns_hap_dem)].copy()
df_hapiscore_limpo = df_hapiscore[df_hapiscore["country"].isin(paises_comuns_hap_dem)].copy()
df_mil_exp_limpo = df_mil_exp[df_mil_exp["country"].isin(paises_comuns_mil_exp_gdp)].copy()
df_gdp_pcap_limpo = df_gdp_pcap[df_gdp_pcap["country"].isin(paises_comuns_mil_exp_gdp)].copy()


# Removendo o 'k' e multiplicando o número por 1000
def convert_k_to_numeric(value):
    if isinstance(value, str) and 'k' in value:
        return float(value.replace('k', '')) * 1000
    else:
        return pd.to_numeric(value, errors='coerce')
    
# Aplicando a função à coluna de PIB per capita do dataset
for year in range(1960, 2023):
    df_gdp_pcap_limpo[str(year)] = df_gdp_pcap_limpo[str(year)].apply(convert_k_to_numeric)
    

if __name__ == "__main__":
    # print(df_mil_exp_limpo)
    # print(df_gdp_pcap_limpo)
    # print(df_democracy_limpo)
    # print(df_hapiscore_limpo)
    print(df_mil_exp_limpo['1964'])
    print(df_mil_exp_limpo['1965'])

