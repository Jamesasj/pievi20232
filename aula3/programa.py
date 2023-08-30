import pandas as pd
import numpy as np
import psycopg2

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

conn = psycopg2.connect("dbname=jbnkzhdn host=rajje.db.elephantsql.com user=jbnkzhdn password=bUyS24TieGTMFnp3N49sjlm3J_Zt6owy")

cur = conn.cursor()
idx = 0
for item in codigos.itertuples():
    ## print(item)
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(int(item[1]), item[0]))
    print(f'ta vivo {idx}')
    if(idx%10 == 0):
        conn.commit()
    idx = idx + 1

conn.commit()        
cur.close()
conn.close()