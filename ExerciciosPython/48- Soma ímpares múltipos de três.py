soma = 0
for c in range(1, 501,2):
    if 0 == c % 3:
        soma += c
print('The sum of all requested values is {}'.format(soma))