from random import randint
attempt = 0
print('--- DISCOVER THE NUMBER ---')
num = int(input('Type a number from 0 the 10: '))
computer = randint(0, 10)
while num != computer:
    if num > computer:
        num = int(input('MISSED... Try a value minor: '))
        attempt += 1
    else:
        num = int(input('MISSED... Try a value bigger: '))
        attempt += 1
print('CONGRATULATIONS! You guessed. Were wade {} attempt.'.format(attempt))