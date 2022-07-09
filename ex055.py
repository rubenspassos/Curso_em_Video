for cont in range(0,5):
    peso = float(input('Qual o peso da pessoa: '))
    if cont == 0:
        menor_peso = peso
        maior_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
print('''O maior peso é {}
e o menor é {}'''.format(maior_peso, menor_peso))

