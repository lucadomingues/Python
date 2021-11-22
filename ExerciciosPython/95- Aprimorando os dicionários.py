jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Name of player: '))
    partidas = int(input(f'{jogador["nome"]} jogou quantas partidas?: '))
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols foram feitos na partida {c}?: ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    resp = str(input('Gostaria de continuar?: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*30)
for k, v in enumerate(jogador):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(jogador):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' - Levantamento do jogador {jogador[busca]["nome"]}')
        for i, g in enumerate(jogador[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-'*30)
print('End of program')