from math import hypot
'''
co = float(input('Digite o tamanho do Cateto Oposto: '))
ca = float(input('Digeite o tamanho do Cateto adjacente: '))
print('{}'.format(hypot(co, ca)))'''

co = float(input('Digite o tamanho do Cateto Oposto: '))
ca = float(input('Digeite o tamanho do Cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))