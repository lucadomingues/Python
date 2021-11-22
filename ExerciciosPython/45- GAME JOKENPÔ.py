from random import choice
print('=-'*10)
print('GAME - JOKENPÔ')
print('=-'*10)
n1 = 'PEDRA'
n2 = 'PAPEL'
n3 = 'TESOURA'
print('''Escolha uma opção...
- PEDRA
- PAPEL
- TESOURA''')
option = str(input('Digite aqui sua opção: ')).upper()
list = [n1, n2, n3]
computer = choice(list)
print('=-'*10)
if option == 'PEDRA' or option == 'PAPEL' or option == 'TESOURA':
    if option == 'PEDRA' and computer == n3 or option == 'PAPEL' and computer == n1 or option == 'TESOURA' and computer == n2:
        print('PARABÉNS! GANHOU O JOGO!')
    elif computer == n1 and option == 'TESOURA' or computer == n2 and option == 'PEDRA' or computer == n3 and option == 'PAPEL':
        print('VOCÊ PERDEU! TENTE NOVAMENTE!')
    elif option == 'PEDRA' and computer == n1 or option == 'PAPEL' and computer == n2 or option == 'TESOURA' and computer == n3:
        print('EMPATE! JOGUE NOVAMENTE')
    print('Você escolheu {} e o computador {}'.format(option, computer))
else:
    print('ERRO! TENTE NOVAMENTE.')
print('=-'*10)