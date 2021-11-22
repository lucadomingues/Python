aluno = dict()
aluno['nome'] = str(input('Type your name: '))
aluno['media'] = float(input('Average: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Recuperação'
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')