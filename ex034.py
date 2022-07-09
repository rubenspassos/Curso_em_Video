from time import sleep
# Firulagem no programa
print('-*' * 23)
print('Digite os valores para calcular um triangulo')
print('-*' * 23)
# Inserindo os valores
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
print('CALCULANDO...')
sleep(3)
# Calculando a possibilidade de formação do triangulo
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('É possível formar um triangulo com os valores digitados.')
else:
    print('Não é possível formar um triangulo com os valores digitados.')