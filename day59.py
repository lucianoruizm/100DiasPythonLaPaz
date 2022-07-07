list_tuple = [("Fisica", 90), ("Quimica", 88), ("Lenguaje", 97)]
# Se toma como referencia el valor numerico, es decir, el segundo elemento.
list_tuple.sort(key = lambda x: x[1])
print(list_tuple)