import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
 
arquivo_excel_1 = 'Estofado.xlsx' 
arquivo_excel_2 = 'concatenado.xlsx'

df_novo1 = pd.read_excel(arquivo_excel_1)
df_novo2 = pd.read_excel(arquivo_excel_2)

filtro = (df_novo2['estofado'] != 0)

df_novo2[filtro].to_excel('filtroEstofado.xlsx')

print(df_novo2[filtro])


