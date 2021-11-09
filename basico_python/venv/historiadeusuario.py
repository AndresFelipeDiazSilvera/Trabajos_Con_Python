"""
Crear una lista con información de estudiantes. Un estudiante cuenta con
nombres,
código,
teléfono.

Historias de usuario
1. Como docente quiero imprimir la información de los estudiantes para conocerlos.
2. como docente quiero buscar un estudiante por teléfono para llamarlo
3. Como docente quiero buscar un estudiante por nombre para consultar su información
4. como docente quiero buscar todas las personas por nombre el resultado deseo imprimirlo en una nueva lista
5. como docente quiero eliminar de la lista la información de un estudiante por nombre
6. como docente quiero agregar a un nuevo estudiante en la lista para consultar su información mas adelante.
"""


def entrarNombre():

    while True:

        nombre = input("Ingrese el nombre del estudiante a añadir: ")

        if nombre == "":

            print("el nombre no puede estar vacio")

        else:

            return nombre


def entrarTelefono():

    while True:

        try:

            telefono = float(input("Ingrese el telefono del estudiante:"))
            return telefono



        except:

            print("el telefono tiene que ser un valor numerico")


def entrarCodigo():

    while True:

        try:

            codigo = float(input("Ingrese el codigo del estudiante:"))
            return codigo



        except:

            print("el codigo tiene que ser un valor numerico")


def devolverEstudiante():
    nombre = entrarTelefono()

    for el in estudiantes:

        if el[0] == nombre:
            print("el telefono del estudiante '{}' es {}".format(nombre, el[1]))

            return True

    print("No se encuentra el estudiante")

    return False


def devolverEstudiante_Telefono():
    telefono = entrarTelefono()

    for el in estudiantes:

        if el[1] == telefono:
            print("el nombre del estudiante '{}' es {}".format(telefono, el[0]))

            return True

    print("No se encuentra el telefono")

    return False


def listarEstudiantesNombre():
    estudiantes.sort()

    print("\n".join(i[0] + " - " + str(i[1]) + " - " + str(i[2]) for i in estudiantes))


def listarEstudiantesTelefono():

    estudiantes.sort(key=lambda x: x[1], reverse=True)

    print("\n".join(i[0] + " - " + str(i[1]) for i in estudiantes))


def borrarEstudiante():
    """ funcion para borrar un estudiante """

    nombre = entrarTelefono()

    indice = buscarEstudiante(nombre)

    if indice == -1:
        print("No se ha encontrado el estudiante '{}'".format(nombre))

        return False

    print("Se ha eliminado el estudiante '{}' con nota {}".format(nombre, estudiantes[indice][1]))

    del estudiantes[indice]

    return True


def buscarEstudiante(nombre):

    for i, e in enumerate(estudiantes):

        if e[0] == nombre:
            return i

    return -1


def Menú():
    print("---------------------------------------------------------------")

    print("Selecciona una opción...")

    print("\t1 - Listado de los estudiantes ordenados por el nombre")

    print("\t2 - Buscar estudiante por nombre")

    print("\t3 - Buscar estudiante por telefono")

    print("\t4 - Añadir estudiante")

    print("\t5 - Borrar un estudiante")

    print("\n\t0 - Salir")


# definimos la lista que contendra una lista con cada estudiante

estudiantes = []

while True:

    Menú()

    try:

        opcion = int(input("Ingrese el número de la opción escogida: "))

    except:

        opcion = -1

    if opcion == 1:

        # Listo
        listarEstudiantesNombre()

    elif opcion == 2:

        devolverEstudiante()

    elif opcion == 3:

        devolverEstudiante_Telefono()

    elif opcion == 4:
        estudiantes.append((entrarNombre(), entrarTelefono(), entrarCodigo()))

    elif opcion == 5:

        borrarEstudiante()

    elif opcion == 0:

        break

    else:

        print("La opción ingresada no es correcta, indica una opción correcta")