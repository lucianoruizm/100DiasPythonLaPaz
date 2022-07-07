import re

string = "abholaaaaabaaabbpythonistaaaaaabbbbb"
patron = "a+b"
substrings = re.findall(patron, string)
print(substrings)