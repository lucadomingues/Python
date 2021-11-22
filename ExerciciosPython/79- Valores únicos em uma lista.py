lista = []
while True:
    num = int(input('Type a number: '))
    if num in lista:
        print('Value double! Not added...')
    else:
        print('Value added succesfully...')
        lista.append(num)
    option = str(input('Wouldo you like to continue? [S/N]: ')).upper().strip()[0]
    if option == 'N':
        break
print(f'Typeds values: {sorted(lista)}')