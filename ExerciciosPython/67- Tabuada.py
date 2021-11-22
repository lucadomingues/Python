while True:
    print('\n--- MULTIPLICATION TABLE ---')
    num = int(input('Type a number integer: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{c} X {num} = {c*num}')
print('END PROGRAM')