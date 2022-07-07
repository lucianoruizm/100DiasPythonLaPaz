import re


import re

string = "Llevas programando 70 dias seguidos"
patron = "\w*a.\w*"
substrings = re.findall(patron, string)
print(substrings)