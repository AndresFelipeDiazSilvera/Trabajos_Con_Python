

def suma(a, b):
    return a+b

print(suma(2,2))

def saludar (nombres="Mateo", apellidos="Calderon"):
    print(f"Hola desde construcción de software {nombres} {apellidos}")

def acceso(año_nacimiento):
    edad=2021-año_nacimiento
    if edad >=18:
        print("Bienvenido al establecimiento")
    else:
        print("No se le perimte el acceso ")

saludar(nombres="Jaime", apellidos="Giraldo")