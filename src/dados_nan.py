import pandas as pd
import cleaning
import json


# Lista anos de 2006 a 2022 (lembrando que a primeria coluna é o nome do país)
anos_hapiscore_democracy = list(cleaning.df_hapiscore.columns[1:]) 

nan_info_hapiscore_democracy = {}

for index, row in cleaning.df_hapiscore.iterrows():
    pais = row[0]  # O nome do país está na primeira coluna
    anos_com_nan = []
    contagem_dados_nan = 0
    

    # Verificar se há NaN nos índices de 2006 a 2022
    for ano in anos_hapiscore_democracy:
        if pd.isna(row[ano]):
            anos_com_nan.append(ano)
            contagem_dados_nan += 1
        
    # Se a lista de anos_com_nan tiver conteúdo, ou seja, o país tem dados Nan,
    # adiciona as informações ao dicionário
    if anos_com_nan:
        nan_info_hapiscore_democracy[pais] = {}
        nan_info_hapiscore_democracy[pais]["anos_nan"] = anos_com_nan
        nan_info_hapiscore_democracy[pais]["contagem_anos_nan"] = contagem_dados_nan


if __name__ == "__main__":
    # visualizar dicionario:
    json_object = json.dumps(nan_info_hapiscore_democracy, indent = 4) 
    print(json_object)