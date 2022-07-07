import itertools

lista = [(2, 4, 6), (7, 8, 5, 6), (5, 10)]
lista_max = list(itertools.starmap(max, lista))
print(lista_max)