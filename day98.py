import timeit

code = '''
def lazy():
    suma = 0
    for i in range(0, 50000000):
        suma += i
'''
print(timeit.timeit(stmt = code))

#Solución Python La Paz
def lazy():
    suma = 0
    for i in range(0, 50000000):
        suma += i

start = timeit.default_timer()
lazy()
end = timeit.default_timer()
print(end - start)