numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'

while True:
    valor_user = int(input('Digite um valor entre 0 e dez: '))
    if valor_user >=0 and valor_user <=10:
        break
    print('Tente novamente')
print(f'Voce digitou o numero {numeros[valor_user]}')