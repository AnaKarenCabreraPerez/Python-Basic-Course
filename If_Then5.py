# Actividad 5 - El número misterioso

# Pregunta 1 #

from random import *

# Clásico número misterioso

numero_misterioso = randint(0, 99)

for intento in range(7):
    print("¿Cuál es el número misterioso?")
    respuesta_str = input("Tu propuesta:")
    respuesta_int = int(respuesta_str) 
    if numero_misterioso == respuesta_int:
        print("¡Bravo!")
        break  # Detener el bucle

    if numero_misterioso < respuesta_int:
        print("No, el número a encontrar es más pequeño!")

    if numero_misterioso > respuesta_int:
        print("No, el número a encontrar es más grande!")

# Cuando termina:
if numero_misterioso != respuesta_int:
    print("¡Perdiste! El número misterioso era", numero_misterioso)


# Pregunta 2 #
# Variante: la computadora miente (1 vez de cada 4)

numero_misterioso = randint(0, 99)

for intento in range(7):
    print("¿Cuál es el número misterioso?")
    respuesta_str = input("Tu propuesta:")
    respuesta_int = int(respuesta_str) 

    # 1 vez de cada 4 (aproximadamente) la computadora miente
    dice_verdad = True
    chance = randint(1, 4)
    if chance == 4:
        dice_verdad = False 

    if numero_misterioso == respuesta_int:
        print("¡Bravo!")
        break  # Detener el bucle
    
    if numero_misterioso < respuesta_int:
        if dice_verdad == True:
            print("No, el número a encontrar es más pequeño!")    
        else:
            print("No, el número a encontrar es más grande!")   

    if numero_misterioso > respuesta_int:
        if dice_verdad == True:
            print("No, el número a encontrar es más grande!")
        else: 
            print("No, el número a encontrar es más pequeño!")

# Cuando termina:
if numero_misterioso != respuesta_int:
    print("¡Perdiste! El número misterioso era", numero_misterioso)

# Pregunta 3 #
# Variante: el número misterioso cambia un poco

numero_misterioso = randint(0, 99)
print(numero_misterioso)
for intento in range(7):
    print("¿Cuál es el número misterioso?")
    respuesta_str = input("Tu propuesta:")
    respuesta_int = int(respuesta_str) 

    # Modificación del número misterioso
    cambio = randint(-3, 3)
    numero_misterioso = numero_misterioso + cambio
    if numero_misterioso < 1:
        numero_misterioso = 1
    if numero_misterioso > 99:
        numero_misterioso = 99

    if numero_misterioso == respuesta_int:
        print("¡Bravo!")
        break  # Detener el bucle
    
    if numero_misterioso < respuesta_int:
        print("No, el número a encontrar es más pequeño!")   

    if numero_misterioso > respuesta_int:
        print("No, el número a encontrar es más grande!")

# Cuando termina:
if numero_misterioso != respuesta_int:
    print("¡Perdiste! El número misterioso era", numero_misterioso)
