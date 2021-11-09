
lista_estudiantes = []

def agregar(nombres, apellidos, telefono, codigo):
    estudiante = { "nombres":nombres, "apellidos":apellidos, "telefono":telefono, "codigo":codigo}
    lista_estudiantes.append(estudiante)

def buscar(codigo):
    cont=0
    for estudiante in lista_estudiantes:
        if estudiante["codigo"]