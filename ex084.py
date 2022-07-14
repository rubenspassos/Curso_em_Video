nome = list()
dados = list()
while True:
    nome.append(str(input('Digite o nome: ')))
    nome.append(float(input('Digite o peso: ')))
    dados.append(nome[:])
    while True:
        opção = str(input('Deseja Continuar? [S/N] ').upper().strip()[0])
        if opção == 'S' or opção == 'N':
            break
        else:
            print('Opção invalida digite novamente ')
    if opção == 'N':
        break

print(f'Ao todo você cadastrou {len(dados)} pessoas')
maior = cont = 0
for p in dados:
    if cont == 0:
        maior = p[1]
        cont += 1
    if p[1] >= maior:
        print(f'{p[1]} é o maior peso, {p[0]}')
    print(p[1])