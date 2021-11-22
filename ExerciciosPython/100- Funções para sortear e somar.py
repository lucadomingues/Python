from random import randint

def sorteia(num):
    for c in range(0, 5):
        num.append(randint(0, 10))
    print(f'Valores sorteados... {num}')

def somaPar(soma):
    par = 0
    for valor in soma:
        if valor % 2 == 0:
            par += valor
    print(f'A soma dos valores pares sorteados é de {par}')

numeros = list()
sorteia(numeros)
somaPar(numeros)