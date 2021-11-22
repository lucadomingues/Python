house = float(input('Type the value of house: '))
buyer = float(input('Type the salary of buyer: '))
year = int(input('In how many years will be paid: '))
installment = house / (year * 12)
print('For pay a house of R$ {:.2f} in {} years...'.format(house, year))
print('The value of installments will be R$ {:.2f}'.format(installment))
if installment > 0.30 * buyer:
    print('LOAN DENIED!')
else:
    print('Loan can be granted')