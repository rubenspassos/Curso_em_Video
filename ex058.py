from random import randint
sorte = randint(0,10)
print('\033[31mOlá sou a CPU'.ljust(50))
print('Vou pensar em um numero de 0 a 10 '.ljust(50))
print('-' * 50)
somador = 0
valor = 0
while valor != sorte:
    valor = int(input('Qual valor eu pensei? '.ljust(50)))
    if valor > 10:
        print('valor inválido, digite novamente.')
    elif valor > sorte:
        print('Menos...Tente mais uma vez')
    elif valor < sorte:
        print('Mais...Tente mais uma vez')
    somador += 1
print('Acertou com {} tentativas. Parabéns'.format(somador))
2