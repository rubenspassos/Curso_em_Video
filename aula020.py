# Aprendendo sobre Função
def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


def linha():
    print('*' * 40)


def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1


def somav(* valores):
    s = 0
    for num in valores:
        s+=1
    print(f'Somando os valores {valores} temos {s}')



# Programa Principal
soma(4,5)

linha()

contador(2,3,5,8,5,2)
contador(2,1)
contador(1)

linha()

valores = [3,6,5,2,5,8,2]
dobra(valores)
print(valores)

linha()

# Desempacotamento
somav(3,2,3,2)
somav(3,2,3,2)

