#Solución Python la Paz
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplos = list(filter(lambda x: x % 3 == 0, lista))
print(multiplos)