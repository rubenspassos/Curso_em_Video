print('Gerador de PA')
print('-*' * 20)
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
inter = termo
for cont in range(0,11):
    # meti um if para não printar ">" no ultimo valor
    print(' {} >'.format(inter) if cont < 10 else ' {} '.format(inter), end='')
    inter += termo + razao
    cont += 1

