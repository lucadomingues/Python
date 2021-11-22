def area(l, c):
    a = l * c
    print(f'Área do terreno: {a:.2f} m²'.replace('.', ','))

l = float(input('Largura do terreno: '))
c = float(input('Comprimento do terreno: '))
area(l, c)