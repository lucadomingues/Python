def fatorial(num, show=False):
    '''
    Calcula fatorial de um número.
    :param num: Valor a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: Mostrar o resultado do fatorial de 'num'
    '''
    res = 1
    while num >= 1:
        if show:
            print(num, end='')
            if num > 1:
                print(' x ', end='')
            elif num == 1:
                print(' = ', end='')
        res *= num
        num -= 1
    return res

print(fatorial(5, show=True))