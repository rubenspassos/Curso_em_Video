lista = []
while True:
    valor = int(input('Digite um valor '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado não vou adicionar...')

    escolha = str(input('Deseja continuar [S/N] ').upper().strip()[0])

    if escolha == "N":
        break
print('-=' * 20)
print(f'Você digitou os valores{sorted(lista)}')
