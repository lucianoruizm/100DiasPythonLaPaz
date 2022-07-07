import re

fechas = ["20221205", "19930612", "20050126", "20211008"]
cambio_formato = [re.sub("(\d{4})(\d{1,2})(\d{1,2})", "\\1-\\2-\\3", f) for f in fechas]
print(cambio_formato)