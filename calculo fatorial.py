'''
from math import factorial
n = int('digite um numero para saber seu fatorial:')
f = factorial(n)
print('o fatorial de {} é {}'.format(n, f))
lógica usando modulo
'''
n = int(input('digite um numero para saber seu fatorial:'))
x = n
f = 1
print('Calculando {}! = '.format(n), end='')
while x > 0:
    print('{}'.format(x), end='')
    print(' x ' if x > 1 else ' = ', end='')
    f = f * x
    x = x - 1
print('{}'.format(f))

