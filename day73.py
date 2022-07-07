import itertools

# lista = ["r", "i", "o"]
# permutaciones = tuple(itertools.permutations(lista))
# print(permutaciones)


# Solución Python La Paz: El resultado según el enunciado es una lista de tuplas, no solo tuplas.
data = ["r", "i", "o"]
resultado = list(itertools.permutations(data))
print(resultado)