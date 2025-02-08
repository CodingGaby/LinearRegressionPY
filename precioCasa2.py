import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[50, 2, 10],[60, 2, 15], [70, 3, 5], [80, 3, 10], [90, 4, 8], [100, 4, 6], [110, 5, 3], [120, 5, 1]])
Y = np.array([150, 180, 210, 240, 270, 300, 330, 360])

model = LinearRegression()
model.fit(X, Y)

prediccion = model.predict([[105, 3, 7]])
print(f"El precio estimado es: {prediccion[0]} miles de dólares")
# Resultado: 315