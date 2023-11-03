# Actividad 5 - Igualdad experimental

from math import *

# Pregunta 1 #

def valor_absoluto(x):
    if x >= 0:
        return x
    else:
        return -x

def raíz_de_cuadrado(x):
    return sqrt(x**2)

def igualdad_experimentale_1(f, g):
    """ Prueba si dos funciones son igualdad experimental """
    for i in range(-100, 101):
        if f(i) != g(i):
            return False
    return True

# Prueba
print("--- Igualdad experimental, una variable ---")
# print(igualdad_experimentale_1(valor_absoluto, valor_absoluto_menos))  # True
print(igualdad_experimentale_1(valor_absoluto, raíz_de_cuadrado))       # True

# Pregunta 2 ##

def F1(a, b):
    return (a+b)**2

def F2(a, b):
    return a**2 + 2*a*b + b**2

def F3(a, b):
    return (a-b)**3

def F4(a, b):
    return a**3 - 3*a**2*b  - 3*a * b**2 + b**3

def F5(a, b):
    return a**3 - 3*a**2*b  + 3*a * b**2 - b**3

def igualdad_experimentale_2(F, G):
    """ Prueba si dos funciones de dos variables son igualdad experimental """

    for i in range(-100, 101):
        for j in range(-100, 101):
            if F(i, j) != G(i, j):
                return False
    return True

# Prueba
print("--- Igualdad experimental, dos variables ---")
print(igualdad_experimentale_2(F1, F2))   # True
print(igualdad_experimentale_2(F3, F4))   # False
print(igualdad_experimentale_2(F3, F5))   # True

# Pregunta 3 #

def sincos(x):
    return sin(x)**2 + cos(x)**2

def uno(x):
    return 1

precisión = 0.00001   # = 10**-5  

def igualdad_experimentale_3(f, g):
    """ Prueba si dos funciones son igualdad experimental
    con un margen de error """   

    for i in range(-100, 101):
        if abs(f(i) - g(i)) > precisión:
            return False
    return True

# Prueba
print("--- Igualdad experimental aproximada ---")
print(igualdad_experimentale_1(sincos, uno))  # False !! Pero debería ser True !
print(sin(3)**2+cos(3)**2)         # Explicación: Python no devuelve exactamente 1 
print(igualdad_experimentale_3(sincos, uno))  # True !

# Una igualdad incorrecta pero experimentalmente cierta

def g1(x):
    return sin(pi*x)

def g2(x):
    return 0

print("--- Una igualdad incorrecta pero experimentalmente cierta ---")
print(igualdad_experimentale_3(g1, g2))  # True (siempre tenemos igualdad para todos los enteros i)
print(g1(1/2))  # sin embargo, g1(0.5) no es cero, por lo tanto, la igualdad no es cierta en general
