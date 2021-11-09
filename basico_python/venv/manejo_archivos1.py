import random
import time

with open("personajes.txt", mode="r", encoding="utf-8") as archivo:
    print(next(archivo))
    print(next(archivo))


def get_encabezado(ruta_archivo):
    with open(ruta_archivo, mode="r", encoding="utf-8")  as archivo:
        encabezado = next(archivo)
    array_encabezado = encabezado.split(",")
    for index in range(len(array_encabezado)):
        array_encabezado[index] = array_encabezado[index].strip()
    return array_encabezado


def get_personajes(ruta_archivo):
    archivo = open(ruta_archivo, mode="r")
    lineas = archivo.readlines()
    archivo.close()
    lista_personajes = []
    for index, linea in enumerate(lineas):
        fila = linea.split(",")
        personaje = {"tipo": fila[0].strip(), "Vida": fila [1].strip(), "Ataque": fila [2].strip(), "Defensa": fila [3].strip(), "Alcance": fila[4].strip() }
        lista_personajes.append(personaje)

    del lista_personajes[0]
    return lista_personajes

def imprimirPersonajes(lista):
    for index, personaje in enumerate(lista):
        print(index, " ", personaje["tipo"])

def combatir(personaje):
    puntaje = random.choice([1, -1])
    caracteristica = random.choice(["Vida", "Ataque", "Defensa", "Alcance"])
    print("Se está combatiendo")
    time.sleep(3)
    valor = int(personaje.get(caracteristica))+puntaje
    personaje.update({caracteristica: str(valor)})
    print(valor)
    return personaje


def update():
    for personaje in  lista:
        print(personaje.values())
        #print(f" {personaje['tipo']}, {personaje['Vida']}, {personaje['Ataque']}, {personaje['Defensa']}, {personaje['Alcance']}")
    #with open(ruta_archivo, mode= "w", encoding="utf-8") as archivo:
        #print(lista)
        #archivo.write('')
        #archivo.write('')
        #archivo.close()

def combetir():
    new_content = []
    keys = []
    for key in lista[0].keys():
        keys.append(key)
    for personaje in lista:
        line = ""
        for i in  keys:
            line = line + f'{personaje[i]},'
            new_content.append(line)

     return new_content



lista = get_personajes("personajes.txt")
print("Seleccione uno de los siguientes personajes")
imprimirPersonajes(lista)

seleccion = int(input("Personaje: "))
print(lista[seleccion])
personaje = lista[seleccion]
combatir(personaje)
print(lista[seleccion])

