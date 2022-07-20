matriz = [] # Inicia a lista
for cont in range (0,3):
    matriz.append(int(input(f'Digite o valor [0,{cont}] ')))
cont = 0
for cont in range (0,3):
    matriz.append(int(input(f'Digite o valor [1,{cont}] ')))
cont = 0
for cont in range (0,3):
    matriz.append(int(input(f'Digite o valor [2,{cont}] ')))
print('=-' * 20)
acumulador = 0
maior = 0
soma = 0
for n in range(0,9):
    if n % 3 == 0 and n != 0:# Pula linha no 3º espaço da lista
        print()
    print(f'[  {matriz[n]}  ]', end='')
    if matriz[n] % 2 == 0:
        acumulador += matriz[n]
    if matriz[n] > maior and n > 2 and n < 6:
        maior = matriz[n]
    if n % 3 == 0:
        soma += matriz[n - 1]  # alimenta a soma caso o valor estiver na ultima coluna

print()
print('-=' * 20)
print(f'A soma dos Valores Pares é {acumulador}')
print(f'A Soma dos valores da Terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')

'''matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input("Digite um valor para [{l},{c}]: '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end ='')'''