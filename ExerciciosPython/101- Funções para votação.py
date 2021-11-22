def voto(nasc):
    idade = 2021 - nasc
    if idade >= 18:
        return f'Com {idade} anos seu voto é OBRIGATÓRIO.'
    elif idade < 16:
        return f'Com {idade} anos seu voto é NEGADO.'
    else:
        return f'Com {idade} anos seu voto é OPCIONAL.'

ano = int(input('Ano de nascimento: '))
print(voto(ano))