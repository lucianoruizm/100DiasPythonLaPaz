# Solución Python La Paz
def saludos(*nombres):
    resultado = ["Hola " + n for n in nombres]
    return resultado

lista = saludos("Max", "Nancy", "Steve")
print(lista)