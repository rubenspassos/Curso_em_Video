numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',\
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinzer',
           'dezesseis', 'dezessete', 'Dezoito','dezenove','vinte' )
while True:
    while True:
        valor_user = int(input('Digite um valor entre 0 e 20: '))
        if valor_user >=0 and valor_user <=20:
            break
        print('Tente novamente')
    print(f'Voce digitou o numero {numeros[valor_user]}')
    novamente = str(input('Deseja ir novamente: [S/N] ')).upper().strip()[0]
    if novamente == 'N':
        print('Obrigado')
        break
    if novamente != 'N' and novamente != 'S':
        print('Digite uma opção válida.')


