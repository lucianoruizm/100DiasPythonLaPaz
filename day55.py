def cuentaRegresiva (numero: int):
    for i in range(1, numero+1):
        print(numero-i)

cuentaRegresiva(5)

# Solución Python La Paz
def atras(num:int):
    print(num)
    num = num - 1
    if num >= 0:
        atras(num)
    pass

atras(5)