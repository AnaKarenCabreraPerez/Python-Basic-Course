# Activity 2 - Divisor, número primo - Bucle while

# Pregunta 1 #

def divisor_mas_pequeno(n):
    """ Encuentra el divisor más pequeño de n """
    d = 2
    while n % d != 0:
        d = d + 1
    return d

# Prueba 
print("--- Divisor más pequeño ---")
print(divisor_mas_pequeno(7*13))

# Pregunta 2 #

def es_primo_1(n):
    """ Comprueba si n es un número primo """

    d = 2    

    while n % d != 0:
        d = d + 1

    if d == n:
        return True    
    else:
        return False

# Prueba        
print("--- Es primo (1) ---")
print(es_primo_1(97))

# Pregunta 3 #
# Números de Fermat

def contraejemplo_fermat():
    for n in range(6): 
        fermat = 2**(2**n)+1
        print(n, fermat, es_primo_1(fermat))
    return  

# Prueba 
print("--- Prueba de la conjetura de números de Fermat ---")
contraejemplo_fermat()

# Pregunta 4 #

def es_primo_2(n):
    """ Comprueba si n es un número primo """

    if n < 2:
        return False

    d = 2    

    while (n % d != 0) and (d**2 <= n):
        d = d + 1

    if d** 2 > n:
        return True    
    else:
        return False

# Prueba        
print("--- Es primo (2) ---")
print(es_primo_2(97))

# Pregunta 5 #

def es_primo_3(n):
    """ Comprueba si n es un número primo """

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

# Prueba        
print("--- Es primo (3) ---")
print(es_primo_3(97))

# Pregunta 6 #
# Cálculo de los tiempos de ejecución de las diferentes funciones es_primo()

import timeit
print(timeit.timeit("es_primo_1(97)", setup="from __main__ import es_primo_1", number=100000))
print(timeit.timeit("es_primo_2(97)", setup="from __main__ import es_primo_2", number=100000))
print(timeit.timeit("es_primo_3(97)", setup="from __main__ import es_primo_3", number=100000))

# ¡Nos quedamos con la mejor función!

def es_primo(n):
    return es_primo_3(n)
