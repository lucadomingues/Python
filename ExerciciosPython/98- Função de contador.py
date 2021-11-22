from time import sleep

def contador(i, f, p):
    print('-='*15)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.5)
    if i > f:
        for c in range(i, f-p, -p):
            print(c, end=' ')
            sleep(0.5)
    print()

contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input('\n\nInício: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)