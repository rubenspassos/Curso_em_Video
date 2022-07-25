def maior(* num):
    from time import sleep
    print('-=' * 30)
    c = len(num[0])
    for ind in num[0]:
        print(f'{ind}', end=' ')
        sleep(.3)
    print(f'Foram informados {c} valores ao todo')
    if len(num[0]) > 0:
        print(f'O maior valor foi {max(num[0])}')
    else:
        print(f'O maior valor foi {0}')



numero = [5,6,54,3,2,5,1,89,4]
maior(numero)
numero.clear()
numero = [6,3,5,9]
maior(numero)
numero.clear()
numero = [6]
maior(numero)
numero.clear()
numero = []
maior(numero)
numero.clear()