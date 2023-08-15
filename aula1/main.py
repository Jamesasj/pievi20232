import pandas as pd
import numpy as np

dt = pd.read_csv('dados.csv')  

dt['ano.nascimento2'] = np.where(dt['ano.nascimento'] > 23,1900,2000) + dt['ano.nascimento'] 
dt['idade'] = 2023 - dt['ano.nascimento2'] 
fileO = open('saida.txt',"w")
fileO.write(dt.to_csv())
fileO.close
print(dt)

