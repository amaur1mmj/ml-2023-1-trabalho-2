import pandas as pd
import matplotlib.pyplot as pyplot 
import seaborn as sns

pd.options.display.max_rows = 99
# pd.options.display.max_columns = 9

dataframe = pd.read_excel('dataset.xlsx')

dataframe.describe()
print(dataframe)

# Vendo os valores para tratamento do dataframe 

# def dt_results(dataframe,columns=50): 
#     k = 0
#     for i in range(columns):
#         test = pd.isnull(dataframe[dataframe.columns[i]])
#         for j in range(len(dataframe[dataframe.columns[i]])):
#             if test[j] != True:
#                 valor = dataframe[dataframe.columns[i]].values[j]
#                 # print(valor)
#                 k += 1
#     return k


# excluindo colunas desnecessárias
def drop_columns(data):   
    new_data = data.drop(data.columns[59:], axis=1)

    return new_data
    
new_data = drop_columns(dataframe)
#new_data.to_excel('sem_valores_NaN2.xlsx')
#print(dt_results(new_data,59))
print(new_data)
print(new_data.describe())

sns.boxplot(data=new_data, x= "Patient age quantile", y = "SARS-Cov-2 exam result")
pyplot.show()


 

    

