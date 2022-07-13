lista = []

while True:
    lista.append(int(input("Digite um valor: ")))
    while True:
        opção = str(input('Deseja continuar? [S/N] ').upper().strip()[0])
        if opção == 'N' or opção == 'S':
            break
        else:
            print('Opção invalida digite novamente')
    if opção == 'N':
        break
lista.sort(reverse=True)
print(f'Voce digitou {len(lista)}  números')
print(f'Os numeros digitados em ordem descrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado na lista nas posições', end='')
    for c, l in enumerate(lista):
        if 5 == lista[c]:
            print(f' {c}...', end='')
else:
    print('O valor 5 não foi digitado')