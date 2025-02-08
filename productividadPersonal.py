import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [35, 1, 3],
    [40, 2, 5], 
    [45, 3, 7], 
    [50, 4, 10],
    [55, 4, 12],
    [60, 5, 15],
    [65, 5, 18],
    [70, 6, 20]
    ])
Y = np.array([60, 75, 85, 95, 100, 110, 120, 130])

model = LinearRegression()
model.fit(X, Y)

prediccion = model.predict([[52, 3, 19]])
print(f"El personal es productivo: {prediccion[0]} %")
# Resultado: 90