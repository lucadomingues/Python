from datetime import date
bigger = 0
minor = 0
for c in range(1, 8):
    year = int(input('Digíte seu ano de nascimento: '))
    current = date.today().year
    age = current - year
    if age >= 18:
        bigger += 1
    else:
        minor += 1
print('Dentre essas pessoas {} são de maiores e {} de menores.'.format(bigger, minor))