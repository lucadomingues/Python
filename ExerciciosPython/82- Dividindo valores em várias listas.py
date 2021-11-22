lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Type a number: ')))
    resp = str(input('Would you like to continue? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=-'*20)
print(f'List complete: {lista}')
print(f'Even numbers from the list: {pares}')
print(f'Odd numbers from the list: {impares}')