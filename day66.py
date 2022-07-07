import re

cadenas = ["Python3.10", "Python3", "ProgramandoAndo", "jun2022", "#100diasdecodigo", "Felicidades!"]
validos = [re.sub("[^A-Za-z0-9]+", "", c) for c in cadenas]
print(validos)