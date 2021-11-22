car = int(input('Car speed (km/h): '))
if car > 80:
    print('FINED! You have exceeded the speed limit of 80 km/h')
    fined = (car - 80) * 7
    print('Value of fined: {:.2f}'.format(fined))
print('Have a Good Morning! Drive safely.')