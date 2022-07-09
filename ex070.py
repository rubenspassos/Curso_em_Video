print('_-' * 20)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('_-' * 20)
total = maior_mil = menor_preço = 0
cont = 0
continuar = 'S'
menor_produto = ''
while True:
    if continuar == 'N':
        break
    produto = str(input('Digite o produto: '))
    preço = float(input('Informe o Preço do produto: R$ '))
    total += preço
    if preço > 1000:
        maior_mil += 1
    if cont == 0 or preço < menor_preço:
        menor_preço = preço
        cont += 1
        menor_produto = produto
        menor_preço = preço
    while True:
        continuar = str(input('Deseja continuar? [S/N]').upper().strip()[0])
        if continuar == 'S' or continuar == 'N':
            break
print('{:-^40}'.format('Fim do programa'))
print(f'O total da compra  foi R${total:.2f}')
print(f'Temos {maior_mil} produtos custando mais de R$ 1000.00')
print(f'O Produto mais barato foi {menor_produto} que custou R$ {menor_preço:.2f}')