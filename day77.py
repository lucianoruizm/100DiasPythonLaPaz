import itertools

lista = [1, 5, 10, 23, 3, 555, 11, 10]
multiplos_cinco = list(itertools.filterfalse(lambda x: x % 5 != 0, lista))
print(multiplos_cinco)

#Solución Python La Paz
# lista = [1, 5, 10, 23, 3, 555, 11, 10]
# predicado = lambda x: x % 5 != 0
# multiplos = list(itertools.filterfalse(predicado, lista))
# print(multiplos)