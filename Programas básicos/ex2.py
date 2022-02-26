import matplotlib.pyplot as plt
import numpy as np

a= np.linspace(0,20,100)

b= np.sin(a)**2 - 0.5

#print(a)
plt.plot(a,b)
plt.show()

#Ejercicio 1
#Programa con input pidiendo información al usuario.
nombre= input('¿Cómo se llama?')
edad= input('¿Qué edad tiene?')
ciudad= input('¿En cúal ciudad vive?')
celular= input('¿Cuál es su celular?')

print('Hola' , nombre , ', tu tienes' ,edad, 'años' ,'. Vives en la ciudad de', ciudad, 'y tu celular es' ,celular, end='.')



#Ejercicio 2
#Programa para pedir al usuario el número de hora y la tarifa por hora para calcular el salario bruto.
Horas= float(input('Introduzca horas:'))
Precio= float(input('Introduzca tarifa:'))
Salario= Horas*Precio

print('Salario:' ,Salario)



#Ejercicio 3
#Comando except-try
#Programa que pida al usuario una temperatura en °C y convertir a °F.

T_C= input('Ingrese la temperatura en °C:')
try:
    T_F= float(T_C) *9/5+32
    print('Ingrese temperatura en °F:', T_F)

except:
    print('Ingrse una temperatura válida')

    

#Tarea de refuerzo
#Programa que pida al usuario dos números;
#los sume, reste, multiplique, los eleve al cuadrado, saque raíz cuadrada cada uno, los divida(tres signos)
a= input('Ingrese el primer término:')
b= input('Ingrese el primer término:')

sumando1= int(a)
sumando2= int(b)

minuendo= float(a)
sustraendo= float(b)

mult1= float(a)
mult2= float(b)

base1= float(a)
exp1= float(2)

base2= float(b)
exp1= float(2)

Raiz1=float(a)**0.5
Raiz2=float(b)**0.5

div1= float(a)
div2= float(b)

print('Suma:' , sumando1+sumando2)
print('Resta:' , minuendo-sustraendo)
print('Multiplicación:' ,mult1*mult2)
print('Pot1:' ,base1**exp1 ,'Pot2:' ,base2**exp1)
print('Raz1:' ,round(Raiz1, 3) ,'Raz2:' , round(Raiz2, 3))
print('División:', round(div1/div2,2),)
print('Parte entera:' , div1//div2)
print('Residuo:' , div1%div2)