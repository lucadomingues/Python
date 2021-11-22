phrase = str(input('Digíte uma frase: ')).strip().upper()
words = phrase.split()
together = ''.join(words)
reverse = together[::-1]

'''reverse = ''
for letter in range(len(together) - 1, -1, -1):
    reverse += together[letter]'''

print('O inverso de {} é {}'.format(together, reverse))
if together == reverse:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')