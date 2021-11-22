weight = float(input('Digíte seu peso (Kg): '))
height = float(input('Digíte sua altura: '))
imc = weight / height**2
print('Seu Índice de Massa Corporal (IMC) está com {:.4f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você atingiu a obesidade!')
else:
    print('Você está com obesidade mórbida!')