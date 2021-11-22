print('Type the number 999 for finish the program')
num = int(input('Type an integer: '))
soma = 0
cont = 0
while num != 999:
    soma += num
    cont += 1
    print('Type the number 999 for finish the program')
    num = int(input('Type an integer: '))
print('Were typed {} numbers'.format(cont))
print('The sum from numbers {}'.format(soma))
print('END PROGRAM')