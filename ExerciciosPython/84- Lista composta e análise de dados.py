dados = list()
geral = list()
mai = men = 0
while True:
    dados.append(str(input('Type a name: ')))
    dados.append(int(input('Weight: ')))
    if len(geral) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    geral.append(dados[:])
    dados.clear()
    resp = str(input('Would you like to continue? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-'*20)
print(f'Amount of people registered: {len(geral)}')
print(f'Weight bigger: {mai} Kg -- Weight of ',end='')
for p in geral:
    if p[1] == mai:
        print(f'{p[0]} ',end='')
print()
print(f'Weight minor: {men} Kg -- Weight of ',end='')
for p in geral:
    if p[1] == men:
        print(f'{p[0]} ',end='')