n1 = int(input('Digite um valor: ')), int(input('Digite um valor: ')),\
     int(input('Digite um valor: ')), int(input('Digite um valor: '))
acumulador = 0
if 9 not in n1:
    print('O valor 9 não foi digitado')
else:
    print(f'O valor 9 foi digitado {n1.count(9)} vezes')
if 3 not in n1:
    print('O valor 3 não foi digitado')
else:
    print(f'O valor primeiro valor 3 aparece na {n1.index(3)} posição')
print('Valores Pares: ', end='')
for cont in range(0,4):
   if n1[cont] % 2 == 0:
        print(f'{n1[cont]} ', end='')
