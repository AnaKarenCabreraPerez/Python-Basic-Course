# Actividad 3 - Digitos de un entero

# pregunta 1 #

for t in range(10):
    for u in range(10):
        n  = 10*t + u
        print(n)

# Pregunta 2 #

for h in range(10):
    for t in range(10):
        for u in range(10):
            n  = 100*h + 10*t + u
            if u == 3 and (h+t+u >= 15) and (t == 0 or t == 2 or t == 4 or t == 6 or t == 8):
                print(n)

# Pregunta 3 #

count = 0

for h in range(10):
    for t in range(10):
        for u in range(10):
            n  = 100*h + 10*t + u
            if u == 3 and (h+t+u >= 15) and (t == 0 or t == 2 or t == 4 or t == 6 or t == 8):
                count = count + 1

print("Numero total de soluciones:",count)