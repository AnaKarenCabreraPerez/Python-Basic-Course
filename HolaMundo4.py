from math import *

# Bucle "for"

for i in range(10):
    print(i*i)

# Bucle "for"

mysum = 0
for i in range(20):
    mysum = mysum + i
print(mysum)

print(list(range(10)))
print(list(range(10,20)))
print(list(range(10,20,2)))

# Anidamiento de bucles

for x in [10,20,30,40,50]:
    for y in [3,7]:
        print(x+y)

# Preguntas

# Cubos
for i in range(101):
    print(i**3)

for i in range(10,21):
    print(i**4)

for i in range(0,101,5):
    print(sqrt(i))

# Q2
# Potencias de 2
for k in range(1,11):
    print(2**k)

# Mínimo de una función escaneando
for i in range(101):
    x = i/100
    y = x*3 - x*2 - 1/4*x + 1
    print("x =", x, "y =", y)

# Volumen de una esfera igual a 100
for i in range(50):
    R = i/10
    V = 4/3 * 3.14 * R**3
    print("R =", R, "V =", V)