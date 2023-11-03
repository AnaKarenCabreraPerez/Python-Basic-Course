# Actividad 4 - Conjetura de Goldbach

from math import *

# Desde la actividad 2

def es_primo(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    d = 3    
    while (n % d != 0) and (d**2 <= n):
        d = d + 2

    if d ** 2 > n:
        return True    
    else:
        return False

# Pregunta 1 #

# Conjetura de Goldbach (1742): 
# cualquier número par mayor que 3 es la suma de dos números primos

def numero_soluciones_goldbach(n):
    """ Calcula el número de descomposiciones n = p + q con
    n par; p, q primos y q >= p """

    # Si n es impar, se termina
    if n % 2 == 1:
        print("¡Atención! Número entero no es par.")
        return None

    nb_sol = 0

    for p in range(2,n//2+1):
        q = n - p
        if (q>=p) and (es_primo(p)) and (es_primo(q)):
            print("n =",n,"suma de p =",p,", q = ",q)
            nb_sol = nb_sol + 1

    return nb_sol

# Prueba    
print("--- Conjetura de Goldbach ---")
print(numero_soluciones_goldbach(100))


def test_conjetura_goldbach(nmax):
    """ Comprueba la validez de la conjetura de Goldbach
    para enteros pares de 4 a nmax """

    print("Comienzo de la prueba")
    for n in range(4,nmax,2):
        if numero_soluciones_goldbach(n) == 0:
            print("Problema con n =",n)
    print("Fin de la prueba")
    return

# Prueba    
print("--- Conjetura de Goldbach ---")
test_conjetura_goldbach(10000)

# Pregunta 2 #

# Conjetura de Goldbach 1752: 
# cualquier número impar se puede escribir como
# n = p + 2k^2
# con p primo y k un número entero (k puede ser 0)

def es_descomposicion_goldbach(n):
    """ Comprueba si el número impar n se puede escribir n = p + 2k^2
    con p primo y k entero """

    maxk = ceil(sqrt(n/2))+1
    for k in range(maxk):
        p = n - 2 * k**2
        if es_primo(p):
            # print(n,p,k,n-p-2*k**2)
            return True    
    return False

def contraejemplo_goldbach(nmax):
    """ Busca un contraejemplo a la segunda conjetura de Goldbach """
    print("--- Comienzo de la búsqueda ---")
    for m in range(1,nmax):
        n = 2 * m + 1
        if es_descomposicion_goldbach(n) == False:
            print("Contraejemplo:",n)

    print("--- Fin de la búsqueda ---")
    return

# Prueba 
print("--- Prueba de la conjetura incorrecta de Goldbach ---")
print("Con 5777:", es_descomposicion_goldbach(5777))
contraejemplo_goldbach(10000)
