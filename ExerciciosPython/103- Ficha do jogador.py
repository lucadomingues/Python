def ficha(nome='<desconhecido>', gols=0):
    print(f'The player {nome} did {gols} in championchip.')

n = str(input('Name of player: '))
g = str(input('Quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)