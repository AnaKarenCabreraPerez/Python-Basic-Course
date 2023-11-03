# Lección - Entrada (Input)

nombre = input("¿Cuál es tu nombre? ")
print("Hola", nombre)

edad_str = input("¿Cuántos años tienes? ")
edad = int(edad_str)

if edad >= 18:
    print("¡Eres un adulto!")
else:
    print("¡Eres un menor!")
