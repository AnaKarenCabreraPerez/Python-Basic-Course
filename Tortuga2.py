# Actividad 2 - Bucle "for"

from turtle import *

# Pregunta 1
# Un pentágono

width(5)
color('azul')

for i in range(5):
    forward(100)
    left(72)

# Pregunta 2
# Otro pentágono

color('rojo')

longitud = 200
ángulo = 72
for i in range(5):
    forward(longitud)
    left(ángulo)

# Pregunta 3
# Un dodecágono (12 lados)

color("morado")
n = 12
ángulo = 360/n
for i in range(n):
    forward(100)
    left(ángulo)

# Pregunta 4
# Una espiral

color("verde")
longitud = 10
for i in range(25):
    forward(longitud)
    left(40)
    longitud = longitud + 10

exitonclick()
