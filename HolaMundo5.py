# Preguntas

# Suma de los cuadrados
n = 20
mysum = 0
for i in range(n+1):
    mysum = mysum + i**2
print(mysum)

# Productos
n = 19
myproduct = 1
for i in range(1, n+1, 2):
    myproduct = myproduct * i
print(myproduct)

# Tablas de multiplicar
for a in range(11):
    for b in range(11):
        print(a, "x", b, "=", a * b)