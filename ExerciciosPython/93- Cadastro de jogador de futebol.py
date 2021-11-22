jogador = dict()
gols = list()
jogador['nome'] = str(input('Name of player: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols foram feitos na partida {c}?: ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print(jogador.items())
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for k, v in enumerate(jogador['gols']):
    print(f' => Na partida {k+1}, fez {v} gol(s)')