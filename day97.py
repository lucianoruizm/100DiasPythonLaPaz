def perimetro_triangulo(**numeros):
     perimetro = 0
     for x in numeros.values():
       perimetro += x
     return float(perimetro)

print(perimetro_triangulo(numero=9, numero_2=11, numero_3=10))