from datetime import datetime
trabaiador = dict()
trabaiador['nome'] = str(input('Nome: '))
nasc = int(input('Ano nascimento: '))
trabaiador['idade'] = datetime.now().year - nasc
trabaiador['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabaiador['carteira'] != 0:
    trabaiador['admissão'] = int(input('Ano de Contratação: '))
    trabaiador['salaraio'] = float(input('Salário: R$ '))
    trabaiador['aposentadoria'] = trabaiador['idade'] + (trabaiador['admissão'] + 35) - datetime.now().year
print(trabaiador)
for n,m in trabaiador.items():
    print(f'{n} tem o valor {m}')

