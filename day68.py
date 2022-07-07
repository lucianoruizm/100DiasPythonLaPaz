import re

fechas = ["2022-12-05", "1993-06-12", "2005-01-26", "2021-10-08"]
patron = "(\d{4})-(\d{2})-(\d{2})"
reemplazo = "\\3\\1\\2"
validos = [re.sub(patron, reemplazo, f) for f in fechas]
print(validos)