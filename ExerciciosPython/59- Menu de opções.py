num1 = int(input('Type the first number: '))
num2 = int(input('Type the second number: '))
menu = int(input('''--- OPTIONS MENU ---
[ 1 ] SUM
[ 2 ] MULTIPLY
[ 3 ] BIGGER
[ 4 ] NEW NUMBERS
[ 5 ] EXIT
TYPE AN OPTION: '''))
while menu != 5:
    if menu == 1:
        soma = num1 + num2
        print('Sum of numbers typed: {}'.format(soma))
    elif menu == 2:
        mult = num1 * num2
        print('Multiplication of the numbers typed: {}'.format(mult))
    elif menu == 3:
        if num1 > num2:
            print('The bigger number typed: {}'.format(num1))
        else:
            print('The bigger number typed: {}'.format(num2))
    elif menu == 4:
        num1 = int(input('Type the first number: '))
        num2 = int(input('Type the second number: '))
    else:
        print('ERRO... TENTE NOVAMENTE!')
    menu = int(input('''--- OPTIONS MENU ---
    [ 1 ] SUM
    [ 2 ] MULTIPLY
    [ 3 ] BIGGER
    [ 4 ] NEW NUMBERS
    [ 5 ] EXIT
    TYPE AN OPTION: '''))
print('--- END PROGRAM ---')