from sklearn.linear_model import LinearRegression
from os import system as System

#Datos de de entrenamiento
X_trian = [[1],[2],[3],[4],[5],[6],[7],[8]] #kilometros en este caso
#Etiquetas:
Y_train = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]#Equivalente en metros 
#Crear y entrenar el modelo de regresion lineal
model=LinearRegression()
model.fit(X_trian, Y_train)

#Limpiar la consola
System("cls")
#pedir el valor en kilometros 
km = int(input("ingrese el valor en kilometros:"))

#Realizar predicciones 
km_to_convert = [[km]]
predicted_m = model.predict(km_to_convert)

#imprimir resultado 
print(f"{km} kilometros equivalen aproximadamente a {predicted_m[0]}metros")
