lista = ('Lapis', 1.75 , 'Borracha', 2.00 ,
         'Caderno' , 15.90 , 'Estojo' , 25.00,
         'Transferidor' , 4.20, 'Compasso', 9.99)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
cont = 0
while cont < len(lista):
    print(f'{lista[cont]:.<32}R${lista[cont+1]:>6.2f}')
    cont += 2
print('-' * 40)