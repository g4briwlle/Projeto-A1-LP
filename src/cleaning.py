""" 
Módulo de limpeza dos datasets
"""

# TODO Fazer limpeza dos outros datasets

import pandas as pd

df_hapiscore_original = pd.read_csv("../data/hapiscore_whr_original.csv")
df_democracy_original = pd.read_csv("../data/demox_eiu.csv")
df_aid_received_original = pd.read_csv("../data/aid_received_per_person_current_us.csv")
df_gdp_total_original = pd.read_csv("../data/total_gdp_us_inflation_adjusted.csv")
df_military_original = pd.read_csv("../data/military_expenditure_percent_of_gdp.csv")
df_co2_pcap_original = pd.read_csv("../data/co2_pcap_cons.csv")
df_arms_exports_original = pd.read_csv("../data/arms_exports_us_inflation_adjusted.csv")

df_democracy = df_democracy_original.copy()
df_hapiscore = df_hapiscore_original.copy()
df_gdp_total = df_gdp_total_original.copy()
df_mil_exp = df_military_original.copy()
df_co2_pcap = df_co2_pcap_original.copy()

# Igualando os nomes das colunas
df_democracy = df_democracy.rename(columns={"Economy Name": "country"})


# Excluindo anos que não estão na interseção dos datasets
df_hapiscore = df_hapiscore.drop(columns=["2005", "2021", "2022"])
df_gpd_total = df_gdp_total.drop(columns=["2023"])

anos_removidos = []
for ano in range(1800, 1960):
    anos_removidos.append(str(ano))
df_co2_pcap = df_co2_pcap.drop(columns=anos_removidos)


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

alterar_paises_co2_pcap_x_mil_exp = {
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
    'Liechtenstein': None,
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
    'Venezuela': None,
    'Samoa': None,
}


# Aplicando as correções de nomes nos datasets
df_democracy["country"] = df_democracy["country"].replace(alterar_paises_happiness_x_democracy)
df_hapiscore["country"] = df_hapiscore["country"].replace(alterar_paises_happiness_x_democracy)

df_mil_exp["country"] = df_mil_exp["country"].replace(alterar_paises_mil_exp_x_gdp)
df_gdp_total["country"] = df_gdp_total["country"].replace(alterar_paises_mil_exp_x_gdp)

df_co2_pcap["country"] = df_co2_pcap["country"].replace(alterar_paises_co2_pcap_x_mil_exp)

# Removendo os países que são 'None' (que não devem estar nos dois datasets)
df_democracy = df_democracy.dropna(subset=["country"])
df_hapiscore = df_hapiscore.dropna(subset=["country"])
df_gdp_total = df_gdp_total.dropna(subset=["country"])
df_mil_exp = df_mil_exp.dropna(subset=["country"])
df_co2_pcap = df_co2_pcap.dropna(subset=["country"])

# Filtrando os datasets para manter apenas os países presentes em ambos
paises_comuns_hap_dem = set(df_democracy["country"]).intersection(set(df_hapiscore["country"]))
paises_comuns_mil_exp_gdp = set(df_mil_exp["country"]).intersection(set(df_gdp_total["country"]))
paises_comuns_co2_mil_exp = set(df_mil_exp["country"]).intersection(set(df_co2_pcap["country"]))

# Criando datasets limpos com os valores extraídos
df_democracy_limpo = df_democracy[df_democracy["country"].isin(paises_comuns_hap_dem)].copy()
df_hapiscore_limpo = df_hapiscore[df_hapiscore["country"].isin(paises_comuns_hap_dem)].copy()
df_mil_exp_limpo = df_mil_exp[df_mil_exp["country"].isin(paises_comuns_mil_exp_gdp)].copy()
df_gdp_total_limpo = df_gdp_total[df_gdp_total["country"].isin(paises_comuns_mil_exp_gdp)].copy()
df_co2_pcap_limpo = df_co2_pcap[df_co2_pcap["country"].isin(paises_comuns_co2_mil_exp)].copy()


# Removendo as medidas de grandeza e multiplicando o número pelo fator de 10 adequado
def convertendo_grandezas_para_numerico(value):
    if isinstance(value, str) and "k" in value:
        return float(value.replace("k", "")) * 1000
    elif isinstance(value, str) and "M" in value:
        return float(value.replace("M", "")) * 1000000
    elif isinstance(value, str) and "B" in value:
        return float(value.replace("B", "")) * 1000000000
    elif isinstance(value, str) and "TR" in value:
        return float(value.replace("TR", "")) * 1000000000000
    else:
        return pd.to_numeric(value, errors="coerce")
    
# Aplicando a função à coluna de PIB per capita do dataset
for year in range(1960, 2023):
    df_gdp_total_limpo[str(year)] = df_gdp_total_limpo[str(year)].apply(convertendo_grandezas_para_numerico)
    

if __name__ == "__main__":
    print(df_mil_exp_limpo)
    print(df_co2_pcap_limpo)
    print(df_mil_exp_limpo)
    print(df_democracy_limpo)
    print(df_hapiscore_limpo)

