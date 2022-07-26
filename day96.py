def nombre_apellido(**kwargs):
     return(kwargs)

print(nombre_apellido(nombre="Juan", apellido="Perez", edad=26))

# Solución Python La Paz
def persona(**atributos):
     resultado = dict()
     for key, value in atributos.items():
          resultado[key] = value
     return resultado

print(persona(nombre="Pepe", apellido="Hernandez", edad=35))