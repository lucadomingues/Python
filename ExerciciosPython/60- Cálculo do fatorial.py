'''from math import factorial
num = int(input('Digíte um número para calcular seu fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))'''

num = int(input('Digíte um número para calcular seu fatorial: '))
cont = num
f = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' X ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))