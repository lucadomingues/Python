from datetime import date
year = int(input('Digíte em que ano nasceu: '))
current = date.today().year
age = current - year
print('Quem nasceu em {} tem hoje {} anos'.format(year, age))
if age < 18:
    rest = 18 - age
    print('Ainda faltam {} anos para se alistar'.format(rest))
    alis = rest + current
    print('Seu alistamento deverá ser feito em {}'.format(alis))
elif age == 18:
    print('Você tem que se alistar imediatamente')
else:
    rest = age - 18
    print('Você ja deveria ter se alistado a {} ano(s)'.format(rest))
    alis = current - rest
    print('Você deveria ter feito seu alistamento em {}'.format(alis))