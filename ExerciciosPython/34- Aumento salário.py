from time import sleep
salary = float(input('Type your salary: '))
print('calculating your increase...')
sleep(2)
if salary > 1250:
    increase = salary * 0.10 + salary
else:
    increase = salary * 0.15 + salary
print('Salary updated: R$ {:.2f}'.format(increase))