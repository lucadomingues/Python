def formata(txt):
    print('-'*30)
    print(txt.center(30))
    print('-'*30)

def situacao(s):
    arquivo.seek(0)
    for linha in arquivo.readlines():
        if s in linha:
            print(linha)

while True:
    with open('turma.txt', 'a+') as arquivo:
        formata('GERENCIADOR DA TURMA')
        #Menu de opções
        print('''- MENU INICIAL -
        [1] DEFINIR INFORMAÇÕES DA TURMA
        [2] INSERIR ALUNO E NOTAS
        [3] EXIBIR ALUNOS E MÉDIAS
        [4] EXIBIR ALUNOS APROVADOS
        [5] EXIBIR ALUNOS REPROVADOS
        [6] SAIR DO PROGRAMA''')
        opc = int(input('DIGÍTE AQUI -> '))
        #Adicionar informações
        if opc == 1:
            inf = str(input('Informações adicionais da turma: '))
            arquivo.write(f'INFORMAÇÕES DA TURMA -> {inf}\n')
        #Inserir alunos e notas
        elif opc == 2:
            nome = str(input('Nome do aluno: '))
            arquivo.write(f'ALUNO: {nome} | ')
            quant_notas = int(input('Quantidade de notas: '))
            soma_notas = cont_notas = 0
            arquivo.write('NOTAS: ')
            for c in range(1, quant_notas+1):
                nota = float(input(f'Nota {c}: '))
                arquivo.write(str(nota))
                arquivo.write(' - ' if c < quant_notas else ' | ')
                soma_notas += nota
                cont_notas += 1
            media = soma_notas / cont_notas
            arquivo.write(f'MÉDIA: {media:.2f} | ')
            if media > 6:
                arquivo.write('APROVADO\n')
            else:
                arquivo.write('REPROVADO\n')
        #Imprimir os alunos e suas respectivas médias
        elif opc == 3:
            arquivo.seek(0)
            for linha in arquivo.readlines():
                if 'TURMA' not in linha:
                    print(f'{linha.split(" | ")[0]} -> {linha.split(" | ")[2]}')
        #Imprimir os alunos aprovados
        elif opc == 4:
            situacao('APROVADO')
        #Imprimir os alunos reprovados
        elif opc == 5:
            situacao('REPROVADO')
        #Sair do sistema
        elif opc == 6:
            break