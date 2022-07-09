valor = int(input('Entre com um valor: '))
soma = numeros = 0
while valor != 999:
    soma += valor
    numeros += 1
    valor = int(input('Entre com um novo valor: '))
print('Você digitou {} valores'.format(numeros), end='')
print('e a soma destes valores é {}'.format(soma))
print('Acabou')