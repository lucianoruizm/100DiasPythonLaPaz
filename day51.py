def cylinderVolume(base, h):
    pi = 3.1416
    radio = base / 2
    baseArea = pi * radio**2
    volume = baseArea * h
    print(volume) 

cylinderVolume(5, 7)


# Solución Python La Paz
from math import pi

def volumen_cilindro(base: float, altura: float):
    # Función que calcula el volumen de un cilindro
    # Args:
       # base (float): diametro del cilindro
       # altura (float): altura del cilindro

    # Returns:
       # float: volumen calculando del cilindro
    radio = base / 2
    volumen = pi * (radio**2) * altura
    return volumen

volumen = volumen_cilindro(5, 7)
print(volumen)
