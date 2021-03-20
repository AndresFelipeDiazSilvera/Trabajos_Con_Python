#AUTHOR: Andres Felipe Diaz Silvera
#DATE: 19/03/2021

#EJERCICIO 5

'''
  Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circuferencia
'''

import math

radio = float(input("radio -> "))

area = math.pi * radio**2

longitud = 2 * math.pi * radio

print(f"El area es: {area:.2f}")
print(f"La longitud de la Circuferencia es: {longitud:.2f}")

