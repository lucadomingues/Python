import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
print('O seno do ângulo {}° é {:.2f}'.format(angulo, seno))
cos = math.cos(math.radians((angulo)))
print('O cosseno do ângulo {}° é {:.2f}'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('A tangente do ângulo {}° é {:.2f}'.format(angulo, tan))