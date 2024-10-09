""" Módulo de funções

"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from cleaning import *
from statsmodels.tsa.seasonal import seasonal_decompose

# Decompor a série temporal
result = seasonal_decompose(df_hapiscore_limpo['2022'], model='additive')

# Plotar os resultados
result.plot()
plt.show()