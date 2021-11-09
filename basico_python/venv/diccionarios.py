persona = {
    "nombres": "Monica",
    "apellidos": "Reyes",
    "telefono": "3126752812"
}

print(persona["nombres"])
print(persona["apellidos"])

for llave in persona:
    print(f"{llave}: {persona[llave]}")

print(persona.keys())
print(persona.values())

#quiz Martes