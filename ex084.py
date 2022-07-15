nome = list()
dados = list()
maior = cont = menor = 0
while True:
    nome.append(str(input('Digite o nome: ')))
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
print(f'Ao todo você cadastrou {len(dados)} pessoas')
nomemaior = ''
nomemenor = ''
for p in dados:
    if cont == 0:
        maior = p[1]
        menor = p[1]
        cont += 1
    if p[1] >= maior:
        maior = p[1]
        nomemaior = p[0]
    if p[1] <= menor:
        menor = p[1]
        nomemenor = p[0]
print(f'O maior peso é {maior} de {nomemaior}')
print(f'O menor peso é {menor} de {nomemenor}')
