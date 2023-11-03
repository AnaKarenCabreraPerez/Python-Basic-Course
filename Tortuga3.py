# Actividad 3 - Gráfico de una función

from turtle import *
from math import *

speed("fastest")
width(2)
color('azul')
up()

for x in range(-200, 200):
    if x == -199:
        down()
    # y = 1/100 * x ** 2   # Parábola
    y = 100 * sin(1/20 * x)  # Seno
    goto(x, y)

exitonclick()
