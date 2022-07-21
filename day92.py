# Solución Python la Paz
def sube_baja(limite):
    i = j = 1
    k = 3
    while limite > 0:
        yield i
        i = i + j
        j = -1 if i >= k else 1 if i <= 1 else j
        limite -= 1

lista = list(sube_baja(9))
print(lista)