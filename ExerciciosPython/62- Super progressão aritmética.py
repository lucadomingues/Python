print('=' * 20)
print('TERMOS DE UMA P.A.')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Digíte quantos dígitos gostaria de mostrar a mais: '))
print('Programa Finalizado!')