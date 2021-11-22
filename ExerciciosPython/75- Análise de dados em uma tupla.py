num = (int(input('Type the first number: ')),
       int(input('Type the second number: ')),
       int(input('Type the third number: ')),
       int(input('Type the fourth number: ')))
print(f'You typed the values {num}')
print(f'The value 9 appeared {num.count(9)} times')
if 3 in num:
       print(f'The value 3 appeared at {num.index(3)+1}ª position')
else:
       print('The value 3 not was typed')
print('Values pairs - ',end='')
for n in num:
    if n % 2 == 0:
           print(n, end=' ')