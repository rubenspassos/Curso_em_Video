# Criar função    OBS: GOSTEI MAIS DA MINHA RESOLUÇÃO..
def leiaInt(num):
    print('-' * 30)
    while True:
        try:
            num = int(input(num))
            break
        except ValueError:
            print(f'\033[31mERRO! Digite um numero inteiro válido.\033[m')
    return num


# Soicitar um numero
n = leiaInt("Digite um numero: ")
# Imprimir valor caso seja inteiro
print(f'Você acabou de digitar um numero {n}')

# Resolução do Guana

# def leiaInt(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print(f'\033[31mERRO! Digite um numero inteiro válido.\033[m')
#         if ok:
#             break
#     return valor
#
# # Programa Principal
# n = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')