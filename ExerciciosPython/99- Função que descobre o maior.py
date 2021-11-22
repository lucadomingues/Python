def maior(*num):
    print('-='*20)
    print('Analisando os valores passados...')
    print(num, end=' ')
    print(f'Foram informados {len(num)} números')
    print(f'O maior número informador foi {max(num)}')

maior(4, 3, 8)
maior(5, 1, 2, 0)
maior(2, 5, 3, 1, 1)
maior(5, 8, 9)