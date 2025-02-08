import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[4], [6],[7],[8],[9],[11]])
Y = np.array([9, 7, 6, 5, 3, 1])

model = LinearRegression()
model.fit(X, Y)

prediccion = model.predict([[2]])
print(f"Dueme: {prediccion[0]} %")
# Resultado: 11

prediccion = model.predict([[10]])
print(f"Dueme: {prediccion[0]} %")
# Resultado: 2
