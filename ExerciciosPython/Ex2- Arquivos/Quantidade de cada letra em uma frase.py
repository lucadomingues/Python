def letra_alf(letra, arq):
    arq.seek(0)
    print(f'{letra} = {arq.read().lower().count(letra)}')

with open('texot.txt', 'wt+') as arquivo:
    text = str(input('Texto -> '))
    arquivo.write(text)

    for c in ('abcdefghijklmnopqrstuvwxyz'):
        letra_alf(c, arquivo)