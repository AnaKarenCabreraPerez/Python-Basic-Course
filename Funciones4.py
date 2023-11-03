# Actividad 4 - Funciones

# Pregunta 1 #

def reducción(edad): 
    """ Devolver el porcentaje de descuento con respecto a la edad """

    if edad < 10:
        disc = 50 
    elif edad <= 18:
        disc = 30
    elif edad >= 60:
        disc = 20
    else:
        disc = 0

    return disc

# Prueba
print("--- Descuento ---")
mi_edad = 16 
print("Tengo", mi_edad, "años y mi descuento es del", reducción(mi_edad), "%.")

def cantidad(tarifa_normal, edad):
    """ Calcular el monto a pagar con respecto a la tarifa normal y la edad """

    reduc = reducción(edad)
    tarifa = tarifa_normal * (100-reduc)/100

    return tarifa

# Prueba
print("--- Monto total a pagar ---")
monto_familia = cantidad(30,9) + 2*cantidad(20,16) + 2*cantidad(35,40)
print(monto_familia)

# Pregunta 2 #

def es_cálculo_correcto(a, b, respuesta):
    """ Comprobar si el resultado de a*b es correcto """

    if respuesta == a * b:
        return True
    else:
        return False

# Prueba
print("--- Prueba de respuesta de multiplicación ---")
print(es_cálculo_correcto(6,7,42))

def prueba_multiplicación(a, b, idioma):
    """ Hacer una multiplicación en inglés u otro idioma
    y mostrar si la respuesta es correcta """

    # Frase en inglés o francés
    if idioma == "english":
        pregunta = "How much is the product a x b? "
        respuesta_correcta = "Well done!"
        respuesta_incorrecta = "It's wrong!"

    if idioma == "french":
        pregunta = "Combien vaut le produit a x b ? "
        respuesta_correcta = "Bravo !"
        respuesta_incorrecta = "Ce n'est pas cela !"

    # Interrogación
    print("--- Pregunta ---")
    print("a =", a)
    print("b =", b)
    respuesta = int(input(pregunta))

    if es_cálculo_correcto(a, b, respuesta):
        print(respuesta_correcta)
    else:
        print(respuesta_incorrecta)

# Prueba
print("--- Cuestionario de multiplicación ---")
prueba_multiplicación(6, 7, "french")
