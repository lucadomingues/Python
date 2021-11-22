from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
dado = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
for k, v in dado.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')