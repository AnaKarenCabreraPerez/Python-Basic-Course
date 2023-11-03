# Actividad 2 - Funciones

# Pregunta 1 #
# Función con parámetro, con salida

def trinomio_1(x):
    """ Calcular 3x^2-7x+4 """

    resultado = 3*x**2 - 7*x + 4

    return resultado


# Prueba
print("--- Trinomio ---")
for i in range(10):
    print("El valor en x =", i, "es", trinomio_1(i))


def trinomio_2(a, b, c, x):
    """ Calcular ax^2+bx+c """

    resultado = a*x**2 + b*x + c

    return resultado

# Prueba
a = 2 ; b = -1 ; c = 0
print("Trinomio para a, b, c =", a, b, c)
for i in range(10):
    print("El valor en x =", i, "es", trinomio_2(a, b, c, i))

# Pregunta 2 #
# Función con parámetro, con salida

def conversion_dolares_a_euros(cantidad):
    """ Convertir una cantidad dada en dólares a euros """

    cantidad_euro = 0.89 * cantidad

    return cantidad_euro


# Prueba
print("--- Moneda ---")
x = 20
print(x, "dólares son", conversion_dolares_a_euros(x), "euros")

def conversion_dolares(cantidad, moneda):
    """ Convertir una cantidad dada en dólares a otra moneda """

    if moneda == "euro":
        tipo_de_cambio = 0.89
    if moneda == "libra":
        tipo_de_cambio = 0.77
    if moneda == "yen":
        tipo_de_cambio = 110
    cantidad_moneda = cantidad * tipo_de_cambio
    return cantidad_moneda

# Prueba
x = 100
for mi_moneda in ["yen", "euro", "libra"]:
    print(x, "dólares equivalen a", conversion_dolares(x, mi_moneda), mi_moneda)

# Pregunta 3 #

from math import *

# Calcular varios volúmenes

def volumen_cubo(a):         
    return a**3

def volumen_esfera(r):         
    return 4/3 * pi * r**3

def volumen_cilindro(r, h):
    return pi * r**2 * h

def volumen_caja(a, b, c):
    return a * b * c

# Prueba
print("--- Volúmenes ---")
print(volumen_cubo(3))
print(volumen_esfera(3))
print(volumen_cilindro(2, 5))
print(volumen_caja(3, 4, 5))

# Pregunta 4 #

def perimetro_area_rectángulo(a, b):
    """ Calcular el perímetro y el área 
    de un rectángulo de lados a y b """

    p = 2 * a + 2 * b
    A = a * b

    return p, A

def perimetro_area_círculo(r):
    """ Calcular el perímetro y el área 
    de un círculo de radio r """

    p = 2 * pi * r
    A = pi * r**2

    return p, A

print("--- Perímetros y áreas ---")
print(perimetro_area_rectángulo(4, 5))
print(perimetro_area_círculo(3))

# Investigación experimental: comparación de perímetro/área de un círculo

for R in range(0, 30):
    perímetro, área = perimetro_area_círculo(R/10)
    print(R/10, perímetro - área)
