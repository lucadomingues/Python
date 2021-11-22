from datetime import date
year = int(input('Digíte em que ano nasceu: '))
current = date.today().year
age = current - year
if age <= 9:
    category = 'MIRIM'
elif age > 9 and age <= 14:
    category = 'INFANTIL'
elif age > 14 and age <= 19:
    category = 'JUNIOR'
elif age > 14 and age <= 25:
    category = 'SÊNIOR'
else:
    category = 'MASTER'
print('O atleta nasceu no ano de {} e hoje está com {} anos'.format(year, age))
print('Classificação: {}'.format(category))