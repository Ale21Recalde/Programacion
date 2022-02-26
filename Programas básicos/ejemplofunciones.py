import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import average

#1. def ---definiendo una función que parar el caso de prg la enfocamos en parte matemàtica
#2. def ff ---definir un nombre el que desee para llamar a la funciòn, se recomenda este nombre sea acorde al requerimiento
#3. def ff(a,b)---definir los paràmetros a considerar dentro de la funciòn
#4.    zz= a + np.exp(b)---operaciòn usando los paràmetros que ingrese
#5.1   print(zz)--- outlet imprimir el resultado
#5.2   return zz---retornando el valor de la operación

def ff (a,b):
    zz= a + np.exp(b)
    #print(zz)
    return zz

def ff2 (a,b,c) :
    zz=np.sin(a-b) + np.log(c)
    return zz

def ave(X):
    zz= np.sum(X)/len(X)
    return zz

a1, a2, a3= np.pi/4, np.pi/8, 2*np.pi/3
A1=[21, np.pi/3 , 28, 65]
   
ale= ff(a1,a2) #aplicaciòn de la primera f
ale2= ff2(a1,a2,a3) #aplicaciòn de la segunda f
ale3= ale + ale2 #sum de las 2 funciones

ale4= ave(A1)
ale5= np.average(A1)

print(ale4)
print(ale5)

