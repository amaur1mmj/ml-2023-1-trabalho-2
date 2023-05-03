from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Carregando o dataset
df = pd.read_excel('nepossivelNEH.xlsx')

# Separando as variáveis preditoras (X) e a variável target (y)
X = df.drop('SARS-Cov-2 exam result', axis=1)
y = df['SARS-Cov-2 exam result']

# Dividindo o dataset em conjunto de treino e conjunto de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Criando o modelo de árvore de decisão
clf = DecisionTreeClassifier()

# Treinando o modelo com o conjunto de treino
clf.fit(X_train, y_train)

# Realizando previsões no conjunto de teste
y_pred = clf.predict(X_test)

# Calculando a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print("Acurácia:", accuracy)