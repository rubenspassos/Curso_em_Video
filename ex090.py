aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: ').capitalize().strip())
aluno['Média'] = float(input(f'Digite a média do aluno {aluno["nome"]}: '))
if aluno['Média'] >= 5:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print(f'Nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["Média"]}')
print(f'Situação é igual a {aluno["Situação"]}')