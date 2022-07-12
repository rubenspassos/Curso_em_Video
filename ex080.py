lista = []
for cont in range (1,6):
    valor = int(input('Digite um Valor: '))
    #if valor >= lista[cont] and valor < lista[cont+ 1]:
       # lista.insert(cont,valor)
    if valor not in lista:
        if cont == 1:
            lista.append(valor)
            print('Valor inserido no final da lista...')
        if valor > lista:
            lista[cont] = valor

    print(cont)
print(lista)
