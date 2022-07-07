import itertools 

numeros = (78, 100)
cadenas = ("Dias", "Python")
lista = list(itertools.chain(numeros, cadenas))
resultado = [type(x) for x in lista]
print(lista)