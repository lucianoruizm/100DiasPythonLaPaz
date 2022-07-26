def fibonacciGenerator(limite):
    num2 = 1
    num3 = 1
    while limite > 0:
        num1 = num2
        yield num1
        num2 = num3
        num3 = num1 + num2
        limite -= 1

lista = list(fibonacciGenerator(10))
print(lista)

# Solución Python La Paz
def fibonacci(limite):
    ultimo, actual = 0, 1
    while limite > 0:
        yield actual
        ultimo, actual = actual, ultimo + actual
        limite -= 1

serie = list(fibonacci(10))
print(serie)