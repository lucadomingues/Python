from random import randint
s = (randint(0,10), randint(0,10), randint(0,10),
    randint(0,10), randint(0,10))
print(f'Values drawn: ', end='')
for n in s:
    print(f'{n} ', end='')
print(f'\nThe bigger value drawn was {max(s)}')
print(f'The minor value drawn was {min(s)}')