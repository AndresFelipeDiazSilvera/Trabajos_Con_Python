#Catorceavo Ejercicio

"""
En una empresa trabajan n empleados cuyos sueldos oscilan entre 100 y 1000 Dolares.
Realizar un programa que informe de cuantos empleados cobran menos de 500 y cuantos más de 500.
Informar también del total que gasta la empresa en pagar a sus empleados.
"""

sueldos = [456,560,345,670,300,590,910,450,960]
sueldos_mayores_500 = 0
sueldos_menores_500 = 0
total=0

for sueldo in sueldos:
    if sueldo > 500:
        sueldos_mayores_500 += 1
    else:
        sueldos_menores_500 += 1
    total += sueldo

print(f"El numero de empleados que ganan mas de 500 es {sueldos_mayores_500}")
print(f"El numero de empleados que ganan menos de 500 es {sueldos_menores_500}")
print(f"El total gasto de la empresa es de:{total} ")

