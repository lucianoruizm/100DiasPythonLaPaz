import re

ips = ["192.08.001.5", "10.120.023.001", "192.160.2.1"]
validos = [re.sub("\.[0]*", ".", ip) for ip in ips]
print(validos)