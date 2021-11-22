from random import randint
cont = 0
print('EVEN OR ODD / PAR OU ÍMPAR')
while True:
    esc = str(input('Even or Odd E/O: ')).strip().upper()[0]
    num = int(input('Type a number: '))
    comp = randint(0,10)
    print(f'The number chosen by computer was {comp}')
    print(f'Value total: {num+comp}')
    if esc == 'E' and (num+comp) % 2 == 0 or esc == 'O' and (num+comp) % 2 == 1:
        print('-='*15)
        print('CONGRATULATION! YOU WON.')
        print('-='*15)
        cont += 1
    elif esc == 'E' and (num+comp) % 2 == 1 or esc == 'O' and (num+comp) % 2 == 0:
        print('-='*15)
        print('YOU LOST!')
        break
    else:
        print('-='*15)
        print('ERRO... TENTE NOVAMENTE!')
        print('-='*15)
    print('Let play again...\n')
print('-='*15)
print(f'Total of victorys: {cont}')
print('END OF THE GAME')