soma = cont = average = bigger = minor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Type a number integer: '))
    soma += num
    cont += 1
    if cont == 1:
            bigger = minor = num
    else:
       if num > bigger:
           bigger = num
       if num < minor:
            minor = num
    resp = str(input('Would you like to continue? [S/N] ')).strip().upper()[0]
average = soma / cont
print('Average from numbers typed: {}'.format(average))
print('Bigger number: {}'.format(bigger))
print('Minor number: {}'.format(minor))
print('END PROGRAM')