# Actividad 3 - Turtle

from turtle import *
width(5)    # Ancho del lápiz

# Pregunta 1 #

def triángulo():
    color('rojo')
    forward(200)
    left(120)
    forward(200)
    left(120)
    forward(200)

# Prueba
# triángulo()
# exitonclick()

# Pregunta 2 #

def cuadrado():
    color('verde')
    for i in range(4):
        forward(200)
        left(90)

# Prueba
# cuadrado()
# exitonclick()

# Pregunta 3 #

def hexágono(longitud):
    color('azul')
    for i in range(6):
        forward(longitud)
        left(60)

# Prueba
# hexágono(100)
# exitonclick()

# Pregunta 4 #

def polígono(n, longitud):
    color('morado')
    ángulo = 360/n
    for i in range(n):
        forward(longitud)
        left(ángulo)

# Prueba
# polígono(10, 70)
# exitonclick()

# Probar todo
up()
goto(-450, 0)
down()
triángulo()
up()
goto(-200, 0)
setheading(0)
down()
cuadrado()
up()
goto(100, 0)
setheading(0)
down()
hexágono(100)
up()
goto(320, 0)
setheading(0)
down()
polígono(8, 70)
up()
exitonclick()
