distance = int(input('Distance of your travel (Km): '))
if distance <= 200:
    print('Value of ticket: R$ {:.2f}'.format(distance * 0.50))
else:
    print('Value of ticket: R$ {:.2f}'.format(distance * 0.45))
