n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print('O \033[31mprimeiro valor\033[m é o \033[34mmaior\033[m')
elif n2 > n1:
    print('O \033[31msegundo valor\033[m é o \033[34mmaior\033[m')
else:
    print('\033[31mNão existe \033[mvalor maior, os dois são \033[34miguais \033[m')