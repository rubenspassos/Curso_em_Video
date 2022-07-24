aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: ').capitalize().strip())
aluno['média'] = float(input(f'Digite a média do aluno {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
#print(f'Nome é igual a {aluno["nome"]}')
#print(f'A média é igual a {aluno["Média"]}')
#print(f'Situação é igual a {aluno["Situação"]}')

for ind, val in aluno.items():
    print(f'{ind} é igual a {val}')