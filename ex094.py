pessoas = dict()
geral = list()
opção = ''
soma = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: ').upper().strip()[0])
    pessoas['idade'] = int(input('Idade: '))
    geral.append(pessoas.copy())
    opção = str(input('Deseja continuar? [S/N]: ').upper().strip()[0])
    while True:
        if opção == "S" or opção == "N":
            break
        else:
            print('Opção inválida, digite novamente')
    if opção == "N":
        break
print(geral)
print(f'Foram cadastradas {len(geral)} pessoas')
val = 0
for c in geral:
    for val in c.keys():
        if val == 'idade':
            print(c.values())
            #soma += val
soma = soma / len(geral)
print(soma)
print(f'A média das idades cadastradas é de {soma}')
'''for c in geral:
    for m,n in c.items():
        if c.items('sexo') == 'F':
            print(c)'''



