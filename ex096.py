def prt():
    print(f'{"CONTROLE DE TERRENOS":^40}')
    print(f'-' * 40)


def area():
    a = float(input('LARGURA (m): '))
    b = float(input('COMPRIMENTO (m): '))
    area = a * b
    print(f'A área de um terreno {a} x {b} e de {area}')


prt()
area()