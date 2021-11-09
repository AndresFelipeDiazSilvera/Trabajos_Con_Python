"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones
múltiplos de 3 y 5, y muestre por pantalla la lista resultante.
"""
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(alfabeto), 1, -1):
    if i % 3 == 0:
        if 5 != 0:
            continue
    alfabeto.pop(i-1)
print(alfabeto)