#Ler arquivo com nomes de cidades
with open('cidades.txt', 'r') as arq1:
    # Gerar arquivo apresentando cidade mais populosa
    with open('maispopulosa.txt', 'wt+') as arq2:
        maior = 0
        cidades = dict()
        for c in arq1.readlines():
            cidades['nome'] = c.split(',')[0]
            cidades['popu'] = int(c.split(',')[1])
            if cidades['popu'] > maior:
                maior = cidades['popu']
                cid = cidades['nome']
        arq2.write(f'Cidade mais populosa:\n{cid} -> {maior}')