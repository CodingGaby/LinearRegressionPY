import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[50, 2],[60, 3], [70, 3], [80, 4], [90, 4]])
Y = np.array([150, 180, 210, 240, 270])

model = LinearRegression()
model.fit(X, Y)

prediccion = model.predict([[85, 3]])
print(f"El precio estimado es: {prediccion[0]} miles de dólares")
# Resultado: 255


prediccion = model.predict([[120, 5]])
print(f"El precio estimado es: {prediccion[0]} miles de dólares")
# Resultado: 360
