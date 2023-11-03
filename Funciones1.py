# Actividad 1 - Introducción a las funciones

# Pregunta 1 #
# Función sin parámetros, sin salida

def imprimir_tabla_de_7():
    """ Mostrar la tabla del 7 """

    print("--- Tabla del 7 ---")
    for i in range(1, 11):
        print(i, "x 7 =", str(i * 7))

# Prueba
imprimir_tabla_de_7()

def imprimir_saludo():
    """ Decir hola """

    nombre = input("¿Cuál es tu nombre? ")
    print("Hola", nombre)

# Prueba
imprimir_saludo()

# Pregunta 2 #
# Función con parámetro, sin salida

def imprimir_tabla(n):
    """ Imprimir la tabla de n """

    print("--- Tabla del", n, "---")
    for i in range(1, 11):
        print(i, "x", n, "=", str(i * n))

# Prueba
imprimir_tabla(5)

def decir_saludo(frase):
    """ Decir hola, hola, adiós... """

    nombre = input("¿Cuál es tu nombre? ")
    print(frase, nombre)

# Prueba
decir_saludo("Adiós")

# Pregunta 3 #
# Función sin parámetros, con salida

def preguntar_nombre():
    """ Preguntar y devolver el primer y apellido """

    nombre = input("¿Cuál es tu primer nombre? ")
    apellido = input("¿Cuál es tu apellido? ")

    nombre_completo = nombre + " " + apellido.upper()

    return nombre_completo

# Prueba
identidad = preguntar_nombre()
print("Identidad:", identidad)
