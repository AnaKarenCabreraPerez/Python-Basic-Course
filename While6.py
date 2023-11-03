# Actividad 6 - Conjetura errónea: 1211111... nunca es primo

# Desde la actividad 2

def es_primo(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    d = 3    
    while (n % d != 0) and (d**2 <= n):
        d = d + 2

    if d**2 > n:
        return True    
    else:
        return False

# Pregunta 1 #

def uno_dos_uno(k):
    """ Calcula un entero 121111... """
    u = 12
    for i in range(k):
        u = 10 * u + 1
    return u


# Prueba 
print("--- 121111.... ---")
u = uno_dos_uno(10)
print(u) 

# Pregunta 2 #
# Conjetura 1211111... nunca es primo

def prueba_primo_uno_dos_uno(kmax):
    """ Prueba si 121111... es primo o no """
    for k in range(kmax):
        uk = uno_dos_uno(k)
        print(k,"  ",uk,"¿es primo?",es_primo(uk))      
    return


# Prueba 
print("--- Prueba conjetura 121111.... nunca primo ---")
prueba_primo_uno_dos_uno(21)

# No conducirá a un contraejemplo
# Porque los cálculos son demasiado largos

# Pregunta 3 #

def es_casi_primo(n, r):
    """ Prueba si n no tiene divisores <= r """

    if n < 2: return False
    if n == 2: return True    
    if n % 2 == 0: return False

    d = 3    
    while (n % d != 0) and (d**2 <= n) and (d <= r):
        d = d + 2

    if (d**2 > n) or (d > r):
        return True    
    else:
        return False

# Prueba 
print("--- Prueba casi primo ---")
print(es_casi_primo(101, 13))

# Pregunta 4 #

def prueba_casi_uno_dos_uno(kmax):
    """ Prueba si 121111... es casi primo """

    n = 12
    for k in range(kmax):
        if es_casi_primo(n, 1000000):
            print(k,"  ",n,'es casi primo')
        n = 10 * n + 1
    return

# Prueba 
print("--- Prueba conjetura 121111.... nunca casi primo ---")
prueba_casi_uno_dos_uno(151)
