# Universidad del valle - Inteligencia Artificial 
# Tema: Aprendisaje inductivo 
# Autor: 
# Importar las biblioteca nesesaria
from sklearn.linear_model import LinearRegression

# Datos de entrenamiento: kilobytes (KB)
X_train = [[1024], [2048], [3072], [4096], [5120], [6144], [7168], [8192]]

# Etiquetas: Megabytes (MB)
y_train = [1, 2, 3, 4, 5, 6, 7, 8]

# Crear y entrenar el modelo de regresion lineal
model = LinearRegression()
model.fit(X_train, y_train)


# Pedir el valor de kb
kb = int(input("Ingrese el valor en kb:"))

# Realizar predicciones 
kb_to_convert = [[kb]]
predicted_mb = model.predict(kb_to_convert)

#imprimir resultado 
print(f"{kb} kb equivale aproximadamente a {predicted_mb[0]} MB")