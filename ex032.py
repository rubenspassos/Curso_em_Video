n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terciero numero: '))
'''if n1 > n2 and n1 > n3:
    print('o Maior numero é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print ('O maior numero é {}'.format(n2))
if n3 > n2 and n3 > n1:
    print('O maior numero é {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor numero é {}' .format(n1))
if n2 < n1 and n2 < n3:
    print('O menor numero é {}'.format(n2))
if n3 <n1 and n3 < n2:
    print('O menor numero é {}'.format(n3))'''
#Verificando o maior numero
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#verificando o menor numero
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior valor digitado foi {}'. format(maior))
print('O menor valor digitado foi {}'.format(menor))