import itertools 

data = [0, 1, 1, 2, 3, 5, 8]
resultado = {}
data = sorted(data)
for k, g in itertools.groupby(data):
    resultado[k] = len(list(g))
print(resultado)