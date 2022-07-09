'''from math import factorial
num = int(input('Digite o valor para calcular seu fatorial: '))
print('O fatorial do numero é: {} '.format(factorial(num)))'''

num = int(input('Digite o valo para calcular seu fatorial: '))
cont = num
factor = 1
print('Calculando {}!'.format(num), end=' ')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    factor *= cont
    cont -= 1
print(factor)
print('O fatorial é igual a {}'.format(factor))