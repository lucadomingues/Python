sum = 0
velho = 0
mnova = 0
for c in range(1, 5):
    print('\n-- {}ª PESSOA --'.format(c))
    name = str(input('Digíte seu nome: ')).strip().upper()
    age = int(input('Digíte sua idade: '))
    sexo = str(input('Digíte seu sexo: ')).strip().upper()
    sum += age
    if c == 1:
        velho == age
    else:
        if age > velho and sexo == 'MASCULINO':
            velho = age
            nomevelho = name

        if age < 20 and sexo == 'FEMININO':
            mnova += 1
media = sum / 4
print('A média das idades digitadas é de {:.1f}'.format(media))
print('O nome do homem mais velho é {}'.format(nomevelho))
print('Dessas pessoas {} mulher(es) tem menos de 20 anos'.format(mnova))