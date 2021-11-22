name = str(input('Enter your full name: ')).strip()
print('The full name with capital letters: {}'.format(name.upper()))
print('The full name with lowercase letters: {}'.format(name.lower()))
print('Total letters: {}'.format(len(name) - name.count(' ')))
'''print('Total letter have first name: {}'.format(name.find(' ')))'''
separacao = name.split()
print('Your first name is {} and has {} letters'.format(separacao[0], len(separacao[0])))