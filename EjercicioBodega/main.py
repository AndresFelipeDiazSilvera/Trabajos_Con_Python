"""
Author: Andres Felipe Diaz Silvera
Date: 29/04/2021
"""

def validar_peso(peso):
    if peso <= 100:
        print("El producto cumple con los requisitos de entrada")
        return
    print("El producto no puede pasar")


def almacenar(tipo_producto):
    if tipo_producto == "Arroz" or tipo_producto == "Frijol" or tipo_producto == "Lenteja" or tipo_producto == "Garbanzo":
        validar_peso(int(input("ingrese el peso del producto:")))
        return
    print("El producto no es valido")

almacenar(input("Ingrese el tipo de mercancia: "))