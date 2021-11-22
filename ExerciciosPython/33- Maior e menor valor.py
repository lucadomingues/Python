n1 = int(input('First number: '))
n2 = int(input('Second number: '))
n3 = int(input('Third number: '))

'''
list = [n1, n2, n3]
print('The bigger value typed was {}'.format(max(list)))
print('The smaller value typed was {}'.format(min(list)))
'''

# Verificando maior valor
bigger = n1
if n2 > n1 and n2 > n3:
    bigger = n2
if n3 > n1 and n3 > n2:
    bigger = n3
# Verificando menor valor
smaller = n1
if n2 < n1 and n2 < n3:
    smaller = n2
if n3 < n1 and n3 < n2:
    smaller = n3
print('The bigger value typed was {}'.format(bigger))
print('The bigger value typed was {}'.format(smaller))