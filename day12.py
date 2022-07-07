# Día 12 - #100DíasDePython

# a = 3
# b = "Python -v"

# a, b = b, a

# print(id(a))
# print(id(b))

# Corrección 

numero = 3
nombre = "Python -v"

numero, nombre = nombre, numero

print(id(numero), id(nombre))