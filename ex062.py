c = 1
n1 = int(input('Entre com o termo: '))
razão = int(input('Entre com a razão: '))
décimo = n1 + 10 * razão
for cont in range(n1, décimo, razão):
    print('{} '.format(cont))
c = int(input('Quantas vezes mais? '))
while c != 0:
    décimo = (cont + razão) + c * razão
    for cont in range(cont + razão, décimo, razão):
        print('{} '.format(cont))
    c = int(input('Quantas vezes mais? '))
    if c == 0:
        print('Acabou')
