lista = []
while True:
    lista.append(int(input('Type a number: ')))
    resp = ''
    option = str(input('Would you like to continue? [S/N]: ')).strip().upper()[0]
    if option == 'N':
        break
print('=-'*20)
print(f'Typeds numbers: {len(lista)}')
lista.sort(reverse=True)
print(f'Order decreasing of list: {lista}')
if 5 in lista:
    print('The value 5 is in the list!')
else:
    print('The value 5 is not in the list!')