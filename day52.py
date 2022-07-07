# Solución Python La Paz
def binario(num: int):
    # Convierte un número entero en binario

    #Args:
        #num (int): numero entero a convertir

    #Returns:
        #str: valor del numero en binario
    
    if num <= 0:
        return "0"
    binario = ""
    while num > 0:
        residuo = int(num % 2)
        num = int(num / 2)
        binario = str(residuo) + binario
    return binario
print(binario(52))