lista = []
for c in range(0,5):
    lista.append(int(input(f'Type the value for the position {c}: ')))
bigger = max(lista)
minor = min(lista)
print('=-'*20)
print(f'You typed the values {lista}')
print(f'The bigger value typed was {bigger} in postion ',end='')
for i, v in enumerate(lista):
    if v == bigger:
        print(f'{i}...',end='')
print()
print(f'The minor value typed was {minor} in position ',end='')
for i, v in enumerate(lista):
    if v == minor:
        print(f'{i}...',end='')