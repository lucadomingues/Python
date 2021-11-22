dados = dict()
dados['nome'] = str(input('Name: '))
nasc = int(input('Year of birth: '))
dados['idade'] = 2021- nasc
dados['ctps'] = int(input('Carteira de trabalho (0 caso não tenha): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Year of contraction: '))
    dados['salário'] = float(input('Wage R$ '))
for k, v in dados.items():
    print(f'{k} tem o valor de R$ {v}')