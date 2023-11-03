# Primera función (no muy inteligente)
def my_function_1(n):
    divis = False
    for k in range(n):
        if k * 7 == n:
            divis = True
    return divis

# Segunda función (más rápida)
def my_function_2(n):
    if n % 7 == 0:
        return True
    else:
        return False

# Medición de tiempos de ejecución
import timeit

# Mide el tiempo de ejecución de my_function_1
print(timeit.timeit("my_function_1(1000)", 
    setup="from __main__ import my_function_1", 
    number=100000))

# Mide el tiempo de ejecución de my_function_2
print(timeit.timeit("my_function_2(1000)", 
    setup="from __main__ import my_function_2", 
    number=100000))
