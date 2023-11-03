# Funciones

x = float("+1.234567")
print(x)

# Módulo de matemáticas

from math import *

x = sqrt(2)
print(x)
print(x**2)

# Seno y coseno

ángulo = pi/2
print(ángulo)
print(sin(ángulo))

# Número decimal a entero

x = 3.6
print(round(x))
print(floor(x))
print(ceil(x))

# Preguntas

# MCD
print(gcd(13*121, 13*122))

a = 101*103
b = 102*103
print(a, b)
mcm = a * b // gcd(a, b)
print(mcm)

# Valor absoluto
x = 3.85
print(abs(x**2-15))
print(round(2*x))
print(floor(3*x))
print(ceil(4*x))

# Ángulo
ángulo = pi/7
x = cos(ángulo)*2 + sin(ángulo)*2
print(x)