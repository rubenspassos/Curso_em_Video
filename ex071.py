print('=' * 40 )
print('{:^40}'.format('BANCO SÓ MONEY'))
print('=' * 40)
valor = int(input('Que valor você quer sacar? R$ '))
nota_cinq = nota_vinte = nota_dez = nota_um = 0
while True:
# Usei if e elif para printar apenas quantidade de cedulas maiores que zero
    if valor >= 50:
        nota_cinq = valor // 50
        valor = valor % 50
        print(f'Total de {nota_cinq:.0f} Cedulas de R$ 50')
    elif valor >= 20:
        nota_vinte = valor // 20
        valor = valor % 20
        print(f'Total de {nota_vinte:.0f} cedulas de R$ 20')
    elif valor >= 10:
        nota_dez = valor // 10
        valor = valor % 10
        print(f'Total de {nota_dez:.0f} cedulas de R$ 10')
    elif valor >= 1:
        nota_um = valor // 1
        valor = 0
        print(f'Total de {nota_um:.0f} cedulas de R$ 1')
    elif valor == 0:
        break
print('=' * 40)
print('Volte sempre ao BANCO SÓ MONEY! Tenha um otimo dia')