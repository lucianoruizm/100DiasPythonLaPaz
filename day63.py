import re

cadenas = ["Python3.10", "Python3", "ProgramandoAndo", "jun2022", "#100diasdecodigo", "Felicidades!"]
patron = '^[a-zA-Z0-9]+$'
validation = [c for c in cadenas if re.search(patron, c)]
print(validation)