import re

correos = ["20200806", "JUN122022", "202204DD", "20221208", "22mar2022"]
patron = "[\d]{8}"
validos = [c for c in correos if re.search(patron, c)]
print(validos)