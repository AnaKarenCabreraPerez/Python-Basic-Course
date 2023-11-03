# Actividad 1 - Cuestionario de multiplicaciones

from random import *

a = randint(1, 10)
b = randint(1, 10)

print("¿Cuánto es el producto de", a, "por", b, "?")
respuesta_str = input("Tu respuesta: ")
respuesta_int = int(respuesta_str)

if respuesta_int == a * b:
    print("¡Bien hecho!")
else:
    print("¡Perdiste! La respuesta correcta era", a * b)
