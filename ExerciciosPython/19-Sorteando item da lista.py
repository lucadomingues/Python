from random import choice
n1 = str(input('First student: '))
n2 = str(input('Second student: '))
n3 = str(input('Third student: '))
n4 = str(input('Fourth student: '))
list = [n1, n2, n3, n4]
drawn = choice(list)
print('Student draw was {}'.format(drawn))