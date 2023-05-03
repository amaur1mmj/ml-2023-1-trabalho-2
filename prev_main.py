import pandas as pd
import matplotlib.pyplot as pyplot 
#import seaborn as sns
#import numpy as np

pd.options.display.max_rows = 99

dataframe = pd.read_excel('dataset.xlsx')


def drop_columns(data):

    for i in data.columns:
        percentual=(data[i].isnull().sum() / len(data['Patient ID'])) *100

        if percentual > 92: 
            
            new_data = data.drop(i, axis='columns')
            data = new_data    
    new_data = data
    
    return new_data
    
new_data = drop_columns(dataframe)

def relativando_dados_flutuantes(data): 
    dado_tratado = data
    trat = data.select_dtypes(include='float64')
    for i in trat.columns:
    
        dado_tratado[i] = dado_tratado[i].fillna((dado_tratado[i].median()))
        #print(dado_tratado[i])
    
    return dado_tratado



def relativando_dados_objects(data):
    dado_tratado = data
    trat = data.select_dtypes(include=['object'])
    
    for i in trat.columns:
        #print(i)
        dado_tratado[i] = dado_tratado[i].fillna(0)
        dado_tratado[i] = dado_tratado[i].replace('negative', '-1.0').replace('positive', '1.0').replace('not_detected', '-1.0').replace('detected', '1.0')
        
    
    return dado_tratado

data_tratado_float = relativando_dados_flutuantes(new_data)

data_frame_tratado = relativando_dados_objects(data_tratado_float)
#(data_tratado_float)

data_frame_tratado = data_frame_tratado.drop('Patient ID', axis=1)
print(data_frame_tratado)

saida = pd.DataFrame(data = data_frame_tratado)
print('--------------kkk-----------------')

#print(saida)
saida.to_excel('nepossivelNEH.xlsx')


percen_newdata = (new_data.isnull().sum() / len(new_data['Hematocrit'])) *100
percen = (data_frame_tratado.isnull().sum() / len(data_frame_tratado['Hematocrit'])) *100

print('-------------------------------')
print(percen_newdata)
print('-------------------------------')
