import re

phones = ["+54 11 1234 5678", "+591 68754321", "+56 9 8765 4321"]
limpio = [re.sub("\+[0-9]* ", "", ip) for ip in phones]
print(limpio)