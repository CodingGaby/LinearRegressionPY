import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[15], [18], [20], [22], [25], [28], [30], [32], [35]])
Y = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180])

model = LinearRegression()
model.fit(X, Y)

prediccion = model.predict([[38]])
print(f"Consume: {prediccion[0]} kWh")
# Resultado: 192
