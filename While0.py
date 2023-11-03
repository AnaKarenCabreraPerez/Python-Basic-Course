# Lección 2 - break

# Ejemplo 1

# Cuenta regresiva
n = 10
while True:     # Bucle infinito
    print(n)
    n = n - 1
    if n < 0:
        break   # Detención inmediata

# Mejor (con una bandera)
n = 10
terminado = False
while not terminado:
    print(n)
    n = n - 1   
    if n < 0:
        terminado = True

# Aún mejor (tras reformulación)
n = 10
while n >= 0:
    print(n)
    n = n - 1

# Ejemplo 2

# Raíz cuadrada entera
n = 777
for i in range(100):
    if i**2 > n:
        break
print(i-1)

# Mejor
n = 777
i = 0 
while i**2 <= n:
    i = i + 1
print(i-1) 

# Ejemplo 3

from math import *

# Raíz cuadrada de los elementos de una lista
mi_lista = [3,7,0,10,-1,12]
for elemento in mi_lista:
    if elemento < 0:
        break
    print(sqrt(elemento))

# Mejor con try/except
mi_lista = [3,7,0,10,-1,12]
for elemento in mi_lista:
    try: 
        print(sqrt(elemento))
    except:
        print("Advertencia, no sé cómo calcular la raíz cuadrada de", elemento)
