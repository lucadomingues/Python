def metade(valor=0, formato=False):
    meio = valor / 2
    return meio if formato is False else moeda(valor)

def dobro(valor=0, formato=False):
    d = valor * 2
    return d if formato is False else moeda(valor)

def aumento(valor=0, taxa=0, formato=False):
    aum = valor + (valor * (taxa/100))
    return aum if formato is False else moeda(valor)

def diminuir(valor=0, taxa=0, formato=False):
    dim = valor - (valor * (taxa/100))
    return dim if formato is False else moeda(valor)

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
