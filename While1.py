# Activity 1 - Divisibility, quotient, remainder

# Pregunta 1 #

def cociente_resto(a, b):
    """ Muestra el cociente y el resto y verifica la validez de la división euclidiana """

    q = a // b
    r = a % b
    print("División de a =", a, "por b =", b)
    print("El cociente es q =", q)
    print("El resto es r =", r)

    if (r >= 0) and (r < b):
        verificar_resto = True
    else:
        verificar_resto = False
    print("Verificar el resto: 0 <= r < b ?", verificar_resto)

    if a == b * q + r:
        verificar_igual = True
    else:
        verificar_igual = False
    print("Verificar a = bq + r ?", verificar_igual)

    return q, r

# Prueba
print("--- Cociente y resto ---")
cociente_resto(100, 7)

# Pregunta 2 #

def es_par(n):
    """ Comprueba si el entero n es par o no (devuelve verdadero o falso) """
    resto = n % 2
    if resto == 0:
        return True
    else:
        return False

def es_par_bis(n):
    """ Comprueba si el entero n es par o no (devuelve verdadero o falso) """
    unidad = n % 10
    if (unidad == 0) or (unidad == 2) or (unidad == 4) or (unidad == 6) or (unidad == 8):
        return True
    else:
        return False

# ¡Con dos líneas!
def es_par_ter(n):
    return (n % 2) == 0

# Prueba
print("--- Par/impar  ---")
print(es_par(1023))

# Pregunta 3 #

def es_divisible(a, b):
    """ Comprueba si a es divisible por b """
    if a % b == 0:
        return True
    else:
        return False

# Prueba
print("--- Divisibilidad  ---")
print(es_divisible(125, 5))
