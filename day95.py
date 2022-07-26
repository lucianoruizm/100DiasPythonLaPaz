def menor_mayor(*numeros):
    mayor = max(numeros)
    menor = min(numeros)
    return {"mayor": mayor, "menor": menor}

print(menor_mayor(1, -3, 5, 8, -6, 8, 10))