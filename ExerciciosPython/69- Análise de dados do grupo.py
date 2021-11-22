bigger = male = feminine = 0
while True:
    age = int(input('\nType your age: '))
    gender = str(input('Type your gender: ')).strip().upper()[0]
    option = str(input('Would you like to continue S/N: ')).strip().upper()[0]
    if age >= 18:
        bigger += 1
    if gender == 'M':
        male += 1
    if gender == 'F' and age < 20:
        feminine += 1
    if option == 'N':
        break
print('-='*15)
print(f'Biggers of age: {bigger}')
print(f'Number of men: {male}')
print(f'Women under 20 years: {feminine}')
print('END PROGRAM')