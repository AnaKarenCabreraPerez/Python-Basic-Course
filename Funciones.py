# Lección 1

def decir_hola():
    print("¡Hola mundo!")
    return

# Llamar
decir_hola()
decir_hola()

def imprimir_cuadrados():
    for i in range(20):
        print(i**2)
    return

# Llamar
imprimir_cuadrados()


# Lección 2

def mostrar_mes(numero):
    if numero == 1:
        print("Estamos en enero.")
    if numero == 2:
        print("Estamos en febrero.")
    if numero == 3:
        print("Estamos en marzo.")
    # etc.
    return

# Llamar
mostrar_mes(2)


def calcular_cubo(a):
    cubo = a * a * a  # o a**3
    return cubo

# Llamar
x = 3
y = 4
z = calcular_cubo(x) + calcular_cubo(y)
print(z)


# Lección 2

def suma_producto(a, b):
    """ Calcula la suma y el producto de dos números. """
    s = a + b
    p = a * b
    return s, p

# Llamar
mi_suma, mi_producto = suma_producto(6, 7)
print(mi_suma, mi_producto)

# Lección - Variable local

x = 7

def sumar_uno(x):
    x = x + 1
    return x

def duplicar(x):
    x = 2 * x
    return x

print(x)
print(sumar_uno(x))
print(duplicar(x))
print(x)
