""" Módulo de limpeza dos datasets
"""

import pandas as pd

df_hapiscore = pd.read_csv("Projeto-A1-LP\data\hapiscore_whr.csv")
df_democracy = pd.read_excel("Projeto-A1-LP\data\democracy_rate_EIU.xlsx")
# df_democracy.to_csv("democracy_rate_EIU_2.csv", index = False)

# Decidi manipular df_democracy para usá-lo nos moldes de df_hapiscore, que é mais simples

# Igualando os nomes das colunas
df_democracy = df_democracy.rename(columns={"Economy Name": "country"})

# Excluindo colunas desnecessárias
df_democracy = df_democracy.drop(columns=["Economy ISO3", "Indicator ID", "Indicator", "Attribute 1", "Attribute 2", "Attribute 3", "Partner"])

# Excluindo dados do ano 2005 de df_hapiscore pois o índice de democracia EIU foi criado em 2006
df_hapiscore = df_hapiscore.drop(columns=["2005"])

if __name__ == "__main__":
    # visualizar datasets
    print(df_democracy.head(7), df_hapiscore.head(7))

