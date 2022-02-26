import numpy as np

#Matriz es filas columnas

#Declaración de matrices

#Declaración por variables

X = [['Kevin', 15,32,25],
    ['Melany', 30,38,1500],
    ['Luis', 28,32,-200]]

#X--> listas puedo llamar a una lista interna X[i], donde i es la posición del componene de lista
# i= 0,1,2,3,....n

#print(X) #---> devuelve la matriz por listas
#print(X[2]) #----> devuelve una lista de una fila en posición i

Xm= np.matrix(X)

print(X)
print(Xm)

