matriz = []
for cont in range (0,3):
    matriz.append(int(input(f'Digite o valor [0,{cont}] ')))
cont = 0
for cont in range (0,3):
    matriz.append(int(input(f'Digite o valor [1,{cont}] ')))
cont = 0
for cont in range (0,3):
    matriz.append(int(input(f'Digite o valor [2,{cont}] ')))
print(matriz)
print('=-' * 20)
acumulador = 0
maior = 0
soma = 0
for n in range(0,9):
    if n % 3 == 0 and n != 0:
        print('')
    print(f'[  {matriz[n]}  ]', end='')
    if matriz[n] % 2 == 0:
        acumulador += matriz[n]
    if n > 5:
        soma += matriz[n]
    if matriz[n] > maior and n > 2 and n < 6:
        maior = matriz[n]
print()
print('-=' * 20)
print(f'A soma dos Valores Pares é {acumulador}')
print(f'A Soma dos valores da Terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')

