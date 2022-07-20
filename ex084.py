# Iniciando as listas e váriaveis
nome = list()
dados = list()
maior = cont = menor = 0

while True:
    nome.append(str(input('Digite o nome: ').title().strip()))
    nome.append(float(input('Digite o peso: ')))
    dados.append(nome[:])
    nome.clear()
    while True:
        opção = str(input('Deseja Continuar? [S/N] ').upper().strip()[0])
        if opção == 'S' or opção == 'N':
            break
        else:
            print('Opção invalida digite novamente ')
    if opção == 'N':
        break
#print(dados)
print(f'Ao todo você cadastrou {len(dados)} pessoas')
nomemaior = []
nomemenor = []
# Confere o maior e menor peso, e guarda o nome na lista e o peso na variável
for p in dados:
    if cont == 0:
        maior = p[1]
        menor = p[1]
        cont += 1
    if p[1] >= maior:
        maior = p[1]
        nomemaior.append(p[0])
    if p[1] <= menor:
        menor = p[1]
        nomemenor.append(p[0])
if dados[0][1] > menor: # Resolve o problema do primeiro nome na lista nomemenor, quando não é o menor.
    del nomemenor[0]

print(f'O maior peso foi de {maior}Kg. Peso de ', end = '')
for c in range(0,len(nomemaior)):
    print(f'{nomemaior[c]} ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end = '')
for c in range(0,len(nomemenor)):
    print(f'{nomemenor[c]} ', end = '')
print()

