import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4],[5]])
Y = np.array([3, 4.4, 5, 5.3, 6])

modelo = LinearRegression()
modelo.fit(X,Y)

coef = modelo.coef_[0]
intercepto = modelo.intercept_
print(f"Pendiente: {coef}")
print(f"Intercepto: {coef}")

horas_nuevas = np.array([[6],[7],[10],])
predicciones = modelo.predict(horas_nuevas)

for horas, prediccion in zip(horas_nuevas, predicciones):
    print(f"Para {horas} la prediccion es: {prediccion}")
    
# Pendiente: 0.6900000000000002
# Intercepto: 0.6900000000000002
# Para [6] la prediccion es: 6.8100000000000005
# Para [7] la prediccion es: 7.500000000000001
# Para [10] la prediccion es: 9.570000000000002