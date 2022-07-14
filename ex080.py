lista = []
cont = 1
for cont in range (1,6):
    valor = int(input('Digite um Valor: '))
    if cont == 1 or valor > lista[-1]:
        lista.append(valor)
        print('Valor inserido no final da lista...')
        cont += 1
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print('Adicionado na primeira posição da lista' if pos == 0 else f'Adicionado '
                                                                                 f'na posição {pos} da lista')
                break
            pos += 1
print('-=' * 20)
print(f'Os Valores digitados em orfem foram {lista}')
