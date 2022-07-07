def listaAlCuadrado(lista):
    for i in range(0, len(lista)):
        lista[i] = lista[i]**2
    return lista

print(listaAlCuadrado([2, 3, 5, 7, 11]))