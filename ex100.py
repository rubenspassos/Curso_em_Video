def sorteio(* num):
    from random import randint
    from time import sleep
    print(f'Sorteando os 5 valores da lista: ', end='')
    for c in range(0,len(num[0])):
        numeros[c] = randint(1,100)
        print(f'{numeros[c]}', end=' ')
        sleep(.3)
    print('Pronto!')


def somaPar(lista):
    par = 0
    for ind in numeros:
        if ind % 2 == 0:
            par += ind
    print(f'Somando os valores pares de {numeros}, temos {par}')

numeros=[0,0,0,0,0]
sorteio(numeros)
somaPar(numeros)
