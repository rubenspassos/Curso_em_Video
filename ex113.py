def leiaInt(num):
    while True:
        try:
            num = int(input(num))
            break
        except ValueError:
            print('\033[31mERRO!!!! Digite um número inteiro\033[m')
        except KeyboardInterrupt:
            print('O Usuário preferiu não digitar o valor')
            num = 0
            break
    return num

def leiaFloat(num):
    while True:
        try:
            num = float(input(num))

        except (ValueError, TypeError):
            print('\033[31mERRO!!!! Digite um número real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('O Usuário preferiu não digitar o valor')
            return 0
        else:
            return num


# Programa Principal
n = leiaInt("Digite um Numero Inteiro: ")
m = leiaFloat('Digite um numero Real: ')
print(f'Os valores digitados foram {n} e {m}')