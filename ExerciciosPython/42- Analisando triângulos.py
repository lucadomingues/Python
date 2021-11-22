n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float (input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        print('Os seguimentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif n1 == n2 != n3 or n2 == n3 != n1 or n1 == n3 != n2:
        print('Os seguimentos acima PODEM FORMAR um triângulo ISÓSCELES!')
    else:
        print('Os seguimetos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo!')