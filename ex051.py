termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
décimo = termo + 10 * razão
for cont in range(termo, décimo, razão):
    print('{} '.format(cont), end=' > ')
#    if cont == 0:
#       print(termo)
#   termo = razão + termo
print('ACABOU')

