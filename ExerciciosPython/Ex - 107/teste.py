import moeda

n = float(input('Digíte um preço R$ '))
print(f'A metada de {moeda.moeda(n)} é {(moeda.metade(n, True))}')
print(f'O dobro de {moeda.moeda(n)} é {(moeda.dobro(n, True))}')
print(f'Aumentado 10%, temos {(moeda.aumento(n, 10, True))}')
print(f'Diminuindo 10% temos {(moeda.diminuir(n, 10, True))}')
