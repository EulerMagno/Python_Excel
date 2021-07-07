import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

arquivo_excel_1 = 'pedido1.xlsx'
arquivo_excel_2 = 'pedido2.xlsx'

df_419A = pd.read_excel(arquivo_excel_1)
df_420A = pd.read_excel(arquivo_excel_2)  

df_todas = pd.concat([df_419A,df_420A])
df_todas.to_excel('concatenado.xlsx')

print(df_todas)
aluminio = df_todas.groupby(['alumínio']).sum()

print(aluminio)

aluminio.plot(kind='bar')

plt.show()
