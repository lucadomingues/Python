cont = soma = 0
while True:
    print('For finish program type the number 999')
    num = int(input('Type a number integer: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Quantity of numbers typed: {cont}')
print(f'Sum of values: {soma}')
print('END PROGRAM')