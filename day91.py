def generar_cuadrados(num):
    cuadrados = []

    for i in range(1, num + 1):
        cuadrados.append(i**2)
    
    yield cuadrados

num_cuadrado = next(generar_cuadrados(10))
print(num_cuadrado)

#Solución Python La Paz
def cuadrados(limite):
    i = 1
    while i <= limite:
        yield i * i
        i += 1

lista = list(cuadrados(10))
print(lista)
