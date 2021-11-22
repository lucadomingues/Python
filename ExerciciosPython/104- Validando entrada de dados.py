def leiaInt(num):
    while True:
        n = str(input(num))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('Erro! Digíte um número inteiro')
    return n

n = leiaInt('Type a number: ')
print(f'The number typed was {n}')