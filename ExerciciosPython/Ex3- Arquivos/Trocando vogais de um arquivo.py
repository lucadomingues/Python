#Receber arquivo
with open('texto.txt', 'r') as arq1:
    #Crie um arquivo texto
    with open('vogais.txt', 'wt+') as arq2:
        arq1.seek(0)
        #Inserir texto do arquivo 1 no arquivo criado e trocar as vogais por "*"
        for letra in arq1.read():
            if letra in 'AaEeIiOoUu':
                letra = '*'
            arq2.write(letra)
        arq2.seek(0)
        print(arq2.read())