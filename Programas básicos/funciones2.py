import numpy as np
import matplotlib.pyplot as plt
from perro import prr, fun2
#from funexp import fun2

#archivo principal

a,b= [1 ,2, 3] , [6, 7, 8] #def listas #np.array hace arreglos
h=np.array([26,12,8])

c,d= 1,6
f,g= 2,7

res0= prr(a,b) #aplicando funciones a listas
res1= prr(c,d)
res2= prr(f,g)

res3= fun2(a,b,h)

#print(res0)
#print(res1)
#print(res2)

#print(res0 [0])
print(res3)

