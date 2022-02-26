import numpy as np

print("Buen día")
#Programa con input pidiendo información al usuario acerca del pago de materia.
#Datos:
nombre= input('Nombre y apellido del estudiante:')
CI= input('Inserte número de cédula:')
Facultad= input('Ingrese a que facultad pertenece:')
semestre= input('¿A qué semestre va?:')

#Se considera que por cada materia se paga $65 sin tomar en cuenta su quintil.

print('Estimado/a' , nombre , ',con CI:' ,CI, 'estudiante de la Escuela Politécnica Nacional', 'de la Facultad de' , Facultad, 'cursando el', semestre ,'semestre', 'realiza el respectivo pago de materias' ,end='.')

Materias= float(input('\nInserte números de materia a repetir:'))

print('Total a pagar:' ,Materias*65)

print('Se solicita el pago inmediato para inscribirse al nuevo periodo.')