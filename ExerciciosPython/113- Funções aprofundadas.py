def leiaInt(num):
    while True:
        try:
            inteiro = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digíte um número inteiro válido...\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar o número.\033[m')
            return 0
        else:
            return inteiro

def leiaFloat(num):
    while True:
        try:
            real = float(input(num))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digíte um número inteiro válido...\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar o número.\033[m')
            return 0
        else:
            return real

inteiro = leiaInt('Digíte um número inteiro: ')
real = leiaFloat('Digíte um número real: ')
print(f'O valor inteiro digitado foi {inteiro}')
print(f'O valor real digitado foi {real}')