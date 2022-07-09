n1 = float(input('Entre com a nota do primeiro semestre: '))
n2 = float(input('Entre com a nota do segundo semestre: '))

media = (n1 + n2) / 2

if media < 5:
    print('O aluno esta \033[31mreprovado\033[m')
elif media >= 5 and media < 7:
    print('O aluno esta de \033[33mrecuperação\033[m')
else:
    print('O aluno esta \033[32maprovado\033[m')