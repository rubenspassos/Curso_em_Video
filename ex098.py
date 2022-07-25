def conta(a,b,c):
    from time import sleep
    if c == 0:
        c = 1
    if c < 0:
        c *= (-1)
    print(f'Contagem de {a} a {b} de {abs(c)} em {abs(c)}')# Não há necessidade do abs(),
    # ele serve para imprimir o numero sempre maior, conforme solicitado no exercicio,
    # porem o if anterior já esta tratando isto.

    if a > b:
        b = b - 1
        c = c * -1
    if a < b:
        b = b + 1
    for d in range(a,b,c):
        print(f'{d}', end=' ')
        sleep(.1)
    print('Fim')


conta(1,10,1)
conta(b=0,a =10,c = -2)
conta(a = int(input('Inicio: ')), b = int(input('Fim: ')), c = int(input('Passo: ')))
