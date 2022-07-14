lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um valor:')))
    while True:
        opção = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if opção == 'N' or opção == 'S':
            break
        else:
            print('Opção inválida, digite novamente: ')
    if opção == 'N':
        break
for n in lista:
    if n % 2 == 0:
        listapar.append(n)
    elif n % 2 == 1:
        listaimpar.append(n)
print('-=' * 20)
print(f'A lista compra é {lista}')
print(f'A lista dos valores pares é {listapar}')
print(f'A lista dos valores impares é {listaimpar}')