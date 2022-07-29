def perimetro_triangulo(**numeros):
     perimetro = 0
     for x in numeros.values():
       perimetro += x
     return float(perimetro)

print(perimetro_triangulo(numero=9, numero_2=11, numero_3=10))

#Solución Python La Paz
def perimetro(**atributos):
    a = atributos["a"]
    b = atributos["b"]
    c = atributos["c"]
    return float(a + b + c)

print(perimetro(a=3, b=4, c=4))