lista = []
cont = 1
for cont in range (1,6):
    valor = int(input('Digite um Valor: '))
    if cont == 1:
        lista.append(valor)
        print('Valor inserido no final da lista...')
        cont += 1
    if valor < lista:
        lista [b -1] = valor
    elif valor >= b:
        lista [b + 1] = valor



print(lista)
