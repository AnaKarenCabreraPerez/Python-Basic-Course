# Actividad 5 - Números con 4 u 8 divisores

# Conjetura: entre 1 y N, hay más números con (exactamente) 4 divisores que números con 8 divisores

# Pregunta 1 #

def numero_de_divisores_1(n):
    """ Número de divisores de n (1 y n están incluidos) """
    nb = 0
    for d in range(1,n+1):
        if n % d == 0:
            nb = nb + 1
    return nb


def numero_de_divisores_2(n):
    """ Número de divisores de n (1 y n están incluidos) """    
    nb = 2  # ya contamos 1 y n
    for d in range(2,n//2+1):
        if n % d == 0:
            nb = nb + 1
    return nb


# Elegimos el mejor método
def numero_de_divisores(n):
    return numero_de_divisores_2(n)


# Prueba 
print("--- Número de divisores ---")
print(numero_de_divisores(100))

# Pregunta 2 #

def cuatro_y_ocho_divisores(Nmin, Nmax):
    nb_cuatro = 0 
    nb_ocho = 0
    for n in range(Nmin, Nmax):
        nb = numero_de_divisores(n)
        if nb == 4:
            nb_cuatro = nb_cuatro + 1
        if nb == 8:
            nb_ocho = nb_ocho + 1
    return nb_cuatro, nb_ocho

# Prueba 
print("--- Números con 4 y 8 divisores ---")
print(cuatro_y_ocho_divisores(1, 100))
