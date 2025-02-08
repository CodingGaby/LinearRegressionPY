import numpy as np
from sklearn.linear_model import LinearRegression

# Relacionar la superficie - Precio venta

X = np.array([[182], [230], [168], [74], [278], [287], [224], [53], 
              [284], [40], [235], [90], [206], [158], [71], [127]])
Y = np.array([[1057784], [1421860], [1426992], [579716], [1537062], 
              [2851058], [1294048], [249418], [1457488], [321680], 
              [957625], [568620], [1605564], [1438748], [686996], [983234]])

model = LinearRegression()
model.fit(X, Y)

prediccion = model.predict([[240]])
print(f"El precio seria: ${prediccion[0]}")
# Resultado: 1587000