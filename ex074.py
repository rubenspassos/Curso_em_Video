from random import randint
while True:
    for cont in range (0,5):
        aleatorio = randint(0,100)
        if cont == 0:
            n1 = aleatorio,
            menor = aleatorio
            maior = aleatorio
        elif cont == 1:
            n2 = aleatorio,
        elif cont == 2:
            n3 = aleatorio,
        elif cont == 3:
            n4 = aleatorio,
        elif cont == 4:
            n5 = aleatorio,
        if aleatorio > maior:
            maior = aleatorio
        if menor > aleatorio:
            menor = aleatorio
        cont += 1
    tupla = n1+n2+n3+n4+n5
    break
print(f'Os valores sorteados foram {tupla}')
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')

