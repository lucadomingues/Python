matriz = ([0,0,0], [0,0,0], [0,0,0])
par = terceira = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Type a value for [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
print('=-'*15)
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-'*15)
print(f'Sum of even values: {par}')
for l in range(0,3):
    terceira += matriz[l][2]
print(f'Sum from values of third column: {terceira}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'Bigger value of second line: {maior}')