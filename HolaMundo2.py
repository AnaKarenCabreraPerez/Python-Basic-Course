# Variables
a = 3  # Una variable
b = 5  # Otra variable

print("La suma es", a + b)   # Mostrar la suma
print("El producto es", a * b)  # Mostrar el producto

c = b**a     # Nueva variable...
print(c)     # ... que se muestra

# Area de un triángulo

base = 8
altura = 3
area = base * altura / 2
print(area)
# print(Area)  # ¡¡Error!!

# Reasignación

S = 1000
S = S + 100
S = S + 200
S = S - 50
print(S)

# Preguntas

# Áreas - Volúmenes
# Trapecio: nombre correcto

B, b, h = 7, 4, 3
area = (B + b) * h / 2
print("El área es", area)

# Caja
L, l, h = 10, 8, 3
volumen = L * l * h
print(volumen)

# Disco
PI = 3.14
R = 10
area = PI * R**2
print(area)

# Reordena las líneas para que al final x tenga el valor 46.
x = 7
y = 2 * x
y = y - 1
x = x + 3 * y
print(x)

# Interés del 10%
S = 1000
S = S * 1.1
S = S * 1.1
S = S * 1.1

# Buena forma de intercambiar los valores de a y b
# Correcto
a = 11
b = 9
c = a
a = b
b = c
print(a, b)