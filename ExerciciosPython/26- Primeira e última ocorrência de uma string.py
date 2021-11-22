phrase = str(input('Type a phrase: ')).strip().upper()
print('The letter "A" appears {} times'.format(phrase.count('A')))
print('The first letter "A" appears in position {}'.format(phrase.find('A')))
print('The last letter "A" appears in position {}'.format(phrase.rfind('A')))