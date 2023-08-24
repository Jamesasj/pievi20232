import pandas as pd
import numpy as np

dados1 = pd.read_csv('dados/10-08-2023_NEGOCIOSAVISTA.txt',
                     header=0, 
                     sep=';', decimal=',')
#dados2 = pd.read_csv('dados/11-08-2023_NEGOCIOSAVISTA.txt')
print('############### dados 1 #####################')
print(dados1.head(5))
# print('############### dados 2 #####################')
#print(len(dados2))

#dados3 = pd.concat([dados1,dados2])
#print('############### dados 3 #####################')
#print(len(dados3))


# arquivo = open('dados/saida1.txt', 'w')
# arquivo.write(dados3.to_csv())
dadosx = dados1[['CodigoInstrumento','PrecoNegocio']]
codigos = dadosx.groupby('CodigoInstrumento').mean()
arquivo = open('dados/saida2.txt', 'w')
arquivo.write(codigos.to_csv())