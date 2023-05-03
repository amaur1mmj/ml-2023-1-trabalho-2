from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


df = pd.read_excel('nepossivelNEH.xlsx')

# separar variáveis dependentes e independentes
X = df.drop('SARS-Cov-2 exam result', axis=1)
y = df['SARS-Cov-2 exam result']

# dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# criar modelo KNN com k=5
knn = KNeighborsClassifier(n_neighbors=5)

# treinar modelo com dados de treino
knn.fit(X_train, y_train)

# fazer previsões em dados de teste
y_pred = knn.predict(X_test)

# calcular acurácia do modelo
acc = accuracy_score(y_test, y_pred)
print(f'Acurácia: {acc:.2f}')