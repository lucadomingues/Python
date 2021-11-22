soma = 0
for c in range(1, 7):
    num = int(input('{}° number: '.format(c)))
    if num % 2 == 0:
        soma += num
print('Value of the sum of the numbers even: {}'.format(soma))