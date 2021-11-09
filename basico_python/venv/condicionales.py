#Noveno Ejercio

claveBD = "123456789"

print("Login ")
nombre = input("Nombre: ")
clave = input("Clave: ")

if clave == claveBD:
    print("Bienvenido a la plataforma")
else:
    print("Usuario o Contraseña no validos")