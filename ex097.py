def escreva(txt):
    tam = len(txt) + 10
    print('-' * tam)
    print(f'{txt.center(tam)}')
    print('-' * tam)


escreva(input("Digite o texto: "))