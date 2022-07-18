from datetime import datetime

# actual = datetime.now()
# inicio = datetime(2022, 4, 20)
# diferencia = actual - inicio
# resultado = diferencia.total_seconds()
# print(resultado)

#Solución Python La Paz
inicio = datetime.strptime("20/04/2022", "%d/%m/%Y")
dia86 = datetime.strptime("14/07/2022", "%d/%m/%Y")
segundos = (dia86 - inicio).total_seconds()
print(segundos)