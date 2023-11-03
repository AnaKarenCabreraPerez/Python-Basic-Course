# Activity 3 - Divisor, números primos - Bucle while (continuación)

# Recordatorio de la actividad 2

def es_primo(n):
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

# Pregunta 1 #

def numero_primo_despues(n):
    """ Busca el primer número primo después de n """
    p = n
    while not es_primo(p):
        p = p + 1
    return p

# Prueba        
print("--- Primer número primo después de un entero ---")
print(numero_primo_despues(60))
print(numero_primo_despues(100000))

# Pregunta 2 #

def primo_gemelo_despues(n):
    """ Encuentra primos gemelos después de n """
    p = n
    q = p + 2
    while (not es_primo(p)) or (not es_primo(q)):
        p = p + 1
        q = p + 2
    return p, q

# Prueba    
print("--- Primeros primos gemelos después de un entero ---")
print(primo_gemelo_despues(60))
print(primo_gemelo_despues(100000))

# Pregunta 3 #

def primo_germain_despues(n):
    """ Encuentra dos primos Germains después de n """
    p = n
    q = 2*p + 1
    while (not es_primo(p)) or (not es_primo(q)):
        p = p + 1
        q = 2*p + 1
    return p, q

# Prueba    
print("--- Primeros primos Germains después de un entero ---")
print(primo_germain_despues(60))
print(primo_germain_despues(100000))
