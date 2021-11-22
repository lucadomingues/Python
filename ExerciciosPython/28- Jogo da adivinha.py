from random import choice
from time import sleep
print('The computer will think of a number between 0 and 5')
num = [0, 1, 2, 3, 4, 5]
comp = choice(num)
user = int(input('Enter a number between 0 and 5: '))
print('PROCESSING...')
sleep(2)
if comp == user:
    print('Congratulations! You won!')
    print('The computer thought of the number {}'.format(comp))
else:
    print('What a pity! You lost.')
    print('The computer thought of the number {}'.format(comp))