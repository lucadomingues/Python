dados = dict()
pessoas = list()
mul = list()
c = somaidade = 0
while True:
    dados['nome'] = str(input('Name: '))
    dados['sexo'] = str(input('Gender: ')).strip().upper()[0]
    dados['idade'] = int(input('Age: '))
    somaidade += dados['idade']
    pessoas.append(dados.copy())
    c += 1
    if dados['sexo'] == 'F':
        mul.append(dados['nome'])
    resp = str(input('Gostaria de continuar?: ')).strip().upper()[0]
    if resp == 'N':
        break
media = somaidade/c
print(f'{c} peoples were registered')
print(f'Média de idade: {media}')
print(f'Women registered: {mul}')
print('Peoples with age above of average... ', end='')
for c in pessoas:
    if c['idade'] > media:
        print(c['nome'], end=' ')
