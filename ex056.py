soma_idade = 0
idade_masc = 0
nome_masc = ''
cont_fem = 0
for cont in range(1,5):
    print('-----------{}º Pessoa -----------'.format(cont))
    nome = str.upper(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str.upper(input('Digite o sexo: ')).strip()
    soma_idade = soma_idade + idade
    if idade > idade_masc and sexo == 'MASCULINO':
        nome_masc = nome
        idade_masc = idade
    elif idade < 20 and sexo == 'FEMININO':
        cont_fem = cont_fem + 1
media_idade = soma_idade / cont
print('A idade média das idades é {} anos.'.format(media_idade))
print('O nome do Homem mais velho é {} '.format(nome_masc))
print('Existem {} mulheres com menos de 20 anos.'.format(cont_fem))

