cont = 0
while True:
    print('-' * 40)
    tabu = int(input('Quer ver a tabuada de que valor? '))
    print('-' * 40)
    if tabu < 0:
        break
    for cont in range(1,11):
        print(f'{cont} x {tabu} = {cont * tabu}')
# primeira tentativa -----------------------------
    '''while cont <= 10:
        resultado = tabu * cont
        print(f'{tabu} x {cont} = {resultado}')
        cont += 1'
    cont = 0'''
# ----------------------------------------------
print('-' * 40)
print('Fim do Programa')
print('-' * 40)



