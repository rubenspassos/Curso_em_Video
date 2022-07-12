lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    while True:
        opção = str(input('Deseja continuar? [S/N]').upper().strip()[0])
        if opção == 'N' or opção == 'S':
            break
        else:
            print('Opção invalida digite novamente')
    if opção == 'N':
        break
print(f'Voce digitou {len(lista)}  números')
print(f'Os numeros digitados em ordem descrescente é {sorted(reverse=True)}')
if 5 in lista:
    print('O valor 5 foi digitado na lista')