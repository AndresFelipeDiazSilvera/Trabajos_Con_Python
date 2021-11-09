#Segudnod Ejercico

producto1 = int(input("Ingrese el valor del primer producto"))
producto2 = int(input("Ingrese el valor del segundo producto"))
producto3 = int(input("Ingrese el valor del tercer producto"))

total_productos = producto1 + producto2 + producto3
iva = total_productos * 0.19
total_general = total_productos + iva
print("Valor neto: ", total_productos)
print("IVA: ", iva)
print("Total: ", total_general)