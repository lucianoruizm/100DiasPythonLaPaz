import math
numeros = [49, 4, 36, 16, 25]
raizCuadrada = list(map(lambda n: math.sqrt(n), numeros))
print(raizCuadrada)

# def raiz_cuadrada(n: list):
#     n2 = []
#     for i in n:
#         n2.append(math.sqrt(i))
#     print(n2)

# raiz_cuadrada([49, 4, 36, 16, 25])

# Solución Python La Paz
from math import sqrt
numeros = [49, 4, 36, 16, 25]
cuadrados = list(map(lambda x: sqrt(x), numeros))
print(cuadrados)