var = input('Type something: ')
print('Tipo primitivo: ', type(var))
print('Só tem espaços: ', var.isspace())
print('É um número: ', var.isnumeric())
print('É alfabético: ',var.isalpha())
print('É alfanumérico: ',var.isalnum())
print('Está em maiúsculas: ',var.isupper())
print('Está em minusculas: ',var.islower())
print('Está capitalizada: ',var.istitle())