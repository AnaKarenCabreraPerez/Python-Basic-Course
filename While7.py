# Actividad 7 - Raíz cuadrada

# Pregunta 1

from math import *

def raiz_cuadrada_1(n):
    """ Calcula la raíz cuadrada entera de n
    Entrada: un número entero
    Salida: su raíz cuadrada entera """

    raiz_real = sqrt(n)
    raiz = floor(raiz_real)

    return raiz

# Prueba
print("--- Raíz cuadrada (1) ---")
print(raiz_cuadrada_1(10))
print(raiz_cuadrada_1(36))
print(raiz_cuadrada_1(56892))

# Pregunta 2

def raiz_cuadrada_2(n):
    """ Calcula la raíz cuadrada entera de n
    Entrada: un número entero
    Salida: su raíz cuadrada entera """

    raiz = 0
    while raiz * raiz <= n:
        raiz = raiz + 1

    return raiz - 1

# Prueba
print("--- Raíz cuadrada (2) ---")
print(raiz_cuadrada_2(10))
print(raiz_cuadrada_2(36))
print(raiz_cuadrada_2(56892))

# Pregunta 3

def raiz_cuadrada_3(n):
    """ Calcula la raíz cuadrada entera de n
    Entrada: un número entero
    Salida: su raíz cuadrada entera """

    a = 1
    b = n
    while abs(a - b) > 1:
        a = (a + b) // 2
        b = n // a
    return min(a, b)

# Pruebas
print("--- Raíz cuadrada (3) ---")
print(raiz_cuadrada_3(10))
print(raiz_cuadrada_3(36))
print(raiz_cuadrada_3(56892))

def mostrar_raiz_cuadrada_3(n):
    """ Muestra los pasos del cálculo de la raíz cuadrada por el último método
    Entrada: un número entero
    Salida: su raíz cuadrada entera
    Acción: muestra los pasos """

    a = 1
    b = n
    i = 0
    print("--- Raíz cuadrada de", n, "---")
    print("i =", i, " ;  a = ", a, " ;  b = ", b)

    while abs(a - b) > 1:
        a = (a + b) // 2
        b = n // a
        i = i + 1
        print("i =", i, " ;  a = ", a, " ;  b = ", b)
    print("La raíz cuadrada entera de", n, "es", min(a, b))

    return min(a, b)

# Pruebas
mostrar_raiz_cuadrada_3(10)
mostrar_raiz_cuadrada_3(1664)

# Variante de la Pregunta 3

def raiz_cuadrada_4(n):
    """ Calcula la raíz cuadrada entera de n
    Entrada: un número entero
    Salida: su raíz cuadrada entera """     

    un = n
    un1 = (un + n // un) // 2

    while un1 < un:
        un = un1
        un1 = (un + n // un) // 2

    return un

# Prueba
print("--- Raíz cuadrada (4) ---")
print(raiz_cuadrada_4(10))
print(raiz_cuadrada_4(36))
print(raiz_cuadrada_4(56892))
