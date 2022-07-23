trabaiador = dict()
trabaiador['nome'] = str(input('Nome: '))
trabaiador['nascimento'] = int(input('Ano de Nascimento: '))
trabaiador['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabaiador['carteira'] != 0:
    trabaiador['admissão'] = int(input('Ano de Contratação: '))
    trabaiador['Salaraio'] = float(input('Salário: '))
    trabaiador['aposentadoria'] = (trabaiador['admissão'] - trabaiador['nascimento']) + 35
print(trabaiador)
for n,m in trabaiador.items():
    print(f'{n} tem o valor {m}')

