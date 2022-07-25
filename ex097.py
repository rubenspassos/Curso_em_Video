def prt(txt):
    tam = len(txt) + 10
    print('-' * tam)
    print(f'{txt.center(tam)}')
    print('-' * tam)


prt(input("Digite o texto: "))