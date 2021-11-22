par = list()
impar = list()
for c in range(0,7):
    num = int(input('Type a number: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print('=-'*20)
print(f'Even values: {sorted(par)}')
print(f'Odd values: {sorted(impar)}')