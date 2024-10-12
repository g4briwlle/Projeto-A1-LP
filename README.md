# Projeto-A1-LP
Integrantes:
- Gabrielle Scherer Mascarelo
- Helouise Mattjie
- Sofia Monteiro
- Vinicio Deusdará

Projeto de análise de dados em Python usando conceitos trabalhados em aula. As principais bibliotecas usadas serão NumPy e Pandas.

Utilizando bases de dados com índices sociais, econômicos e políticos de países ao redor do mundo ao longo do tempo, buscamos explorar as seguintes quatro propostas de análise. Para responder as questões, comparamos os índices referentes das analises dos países ao longo dos anos e usamos recursos estatísticos para averiguar as relações, em principal o R-quadrado.

# Proposta 1:
- Existe uma correlação entre o índice de democracia e o índice de felicidade populacional de um país ao longo do tempo? (Dado o período de 2006 a 2022)

# Proposta 2:
- Existe uma correlação entre as despesas militares e o valor do PIB de um país ao longo do tempo? (Dado o período de 1960 a 2022)

# Proposta 3:
- Existe uma correlação entre as emissões de gás carbônico e as despesas militares de um país ao longo do tempo? (Dado o período de 1960 a 2022)
  
# Proposta 4:
- Existe uma correlação entre cada um dos índices coletados por região mundial? (Dado a classificação entre Norte e Sul global, e os períodos de cada análise)

# Como rodar o código:
1. Para obter as visualizações:
- Digitar "pip install streamlit", "pip install statsmodels" e "pip install plotly" no terminal
- Navegar até a pasta 'src' e digitar 'streamlit run main.py' no terminal. A aba aberta no navegador contém todas as visualizações, basta selecionar a desejada.
2. Para rodar os unittests:
- Navegar até a pasta raiz do repositório e digitar: 'python -m unittest tests.test_cleaning' no terminal para rodar o teste do módulo cleaning. Para os outros módulos, basta alterar o nome do arquivo 'test_cleaning' para o desejado.

