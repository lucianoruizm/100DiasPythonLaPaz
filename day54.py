# Solución Python La Paz
def vocales(cadenas: list):
    # Función que cuenta la cantidad de vocales
    # en una lista de cadenas

    # Args: cadenas (list): lista de cadenas

    # Returns: dict: diccionario con la cantidad de vocales de 
    # cada cadena

    salida = {}
    cadenas = [c.lower() for c in cadenas]
    for cadena in cadenas:
        contador = 0
        for vocal in "aeiou":
            contador += cadena.count(vocal)
        salida[cadena] = contador
    return salida

ejemplo = ["Python", "es", "cool"]
print(vocales(ejemplo))