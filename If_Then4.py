# Actividad 4 - Triángulos

# Pregunta 1 #

a = 4
b = 5
c = 8
print("Triángulo", a, b, c)

# ¿Tenemos a <= b <= c?

if a <= b and b <= c:
    print("Longitudes en el orden correcto.")
else:
    print("Longitudes en el orden incorrecto.")

# Pregunta 2 #

# ¿Podemos construir un triángulo con estas tres longitudes?

if a + b >= c:
    print("Existe un triángulo con esas longitudes.")
else:
    print("No es posible construir un triángulo con esas longitudes.")

# Pregunta 3 #
# ¿Es el triángulo rectángulo?

if a**2 + b**2 == c**2:
    print("El triángulo es rectángulo.")
else:
    print("El triángulo no es rectángulo.")

# Pregunta 3 #
# ¿Es el triángulo equilátero?

if (a == b) and (b == c) and (a == c):
    print("El triángulo es equilátero.")
else:
    print("El triángulo no es equilátero.")

# Pregunta 4 #
# ¿Es el triángulo isósceles?

if (a == b) or (b == c) or (a == c):
    print("El triángulo es isósceles.")
else:
    print("El triángulo no es isósceles.")

# Pregunta 5 #
# ¿Todos los ángulos son agudos?

cosalfa = (-a**2 + b**2 + c**2)/(2*b*c)
cosbeta = (a**2 - b**2 + c**2)/(2*a*c)
cosgamma = (a**2 + b**2 - c**2)/(2*a*b)

if (cosalfa >= 0) and (cosbeta >= 0) and (cosgamma >= 0):
    print("Todos los ángulos son agudos.")
else:
    print("No todos los ángulos son agudos. (Al menos uno de ellos es obtuso).")
