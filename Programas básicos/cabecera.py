import numpy as np #librerias, funciones, clases y objetos
import matplotlib.pyplot as plt

a= np.linspace(1,100,4)
#1..........99 divisiones........100
#0................................98 contadores
#a, b= 5.5, 8.5  #cabecera de variables fijas

#b= [1,2,5,7] #arrg. mat. siempre prevalece sobre la lista
m= np.array([1.5, 2.5, 5.5, 7.5])  
n=([1.5, 2.5, 5.5, 7.5])
d= np.array(n) 

f1=m**2 + np.sin(np.pi/4)
#f2=n**2
f3=d**3 - np.cos(np.pi/3)

plt.plot(f1,f3)
plt.show()


#print(f1)
#print(f2)
#print(f3)
#print(m)
#print(n)
#print(d)



