#Quntiavo Ejercicio

"""
Escriba un algoritmo que sume los números ingresados por el usuario hasta que el usuario ingrese el número 0
(detener las preguntas ante este escenario).
"""
suma = 0
numero = int(input(u"Ingrese un número"))
while numero!=0:
    suma += numero
    numero = int(input(u"Ingrese un número"))
    if (numero==0):
        break
print (u"Suma total:",suma)