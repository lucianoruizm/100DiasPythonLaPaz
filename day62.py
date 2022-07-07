import re

emails = ["pythonlapaz@gmail.com", "dias.com", "comidita@.com", "programando@outlook.com"]
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
validation = [e for e in emails if re.search(regex, e)]
print(validation)