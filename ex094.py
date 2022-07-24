pessoas = dict()
geral = list()
opção = ''
soma = media = 0
while True:
    pessoas['nome'] = str(input('Nome: ').title().strip())
    while True:
        pessoas['sexo'] = str(input('Sexo: ').upper().strip()[0])
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, figite apenas M ou F. ')
    pessoas['idade'] = int(input('Idade: '))
    geral.append(pessoas.copy())
    while True:
        opção = str(input('Deseja continuar? [S/N]: ').upper().strip()[0])
        if opção in 'SN':
            break
        print('Opção inválida, digite novamente')
    if opção == "N":
        break
print('-=' * 30)
print(f'- Foram cadastradas {len(geral)} pessoas')
for c in geral:
    for ind, val in c.items():
        if ind == 'idade':
            soma += val
media = soma / len(geral)
print(f'- A média das idades cadastradas é de {media:.2f}')
print('- As mulheres cadastradas foram: ' , end='')
for c in geral:
    if c['sexo'] in "F":
        print(c['nome'], end=' ')
print()
print('- Lista de Pessoas que estão acima da média: ')
for c in geral:
    for ind, val in c.items():
        if c['idade'] > media:
            print(f'{ind} = {val}; ', end='')
    print()





