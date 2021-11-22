total = mais1 = menor = cont = 0
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Digíte o valor do produto: '))
    total += preço
    cont += 1
    if preço > 1000:
        mais1 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Gostaria de Continuar S/N?: ')).strip().upper()[0]
    if resp == 'N':
        break
print('- FIM DO PROGRAMA -')
print(f'Total gasto da compra: {total:.2f}')
print(f'Produtos que custam mais de R$ 1.000,00: {mais1}')
print(f'Nome do produto mais barato: {barato}')