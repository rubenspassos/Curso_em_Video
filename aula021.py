print('-=' * 20)
print('Função Help')
print('-=' * 20)
# Função Help

help(print)

# Outra forma de acessar o help

print(input.__doc__)

print('-=' * 20)
print('Docstrings')
print('-=' * 20)
# Docstrings

def contador(i, f, p):
    """
    -> Faz uma contagem e mosta na tela.
    :param i:valor inicial
    :param f:valor final
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c +=p
    print('Fim')

help(contador)

print('-=' * 20)
print('Parâmetros opcionais')
print('-=' * 20)
# Parâmetro Opcionais


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de tres valores e mostra resultado na tela,
    caso o valor não seja atribuído recebera o valor padrão 0
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(3,2)
somar(3)
somar()

print('-=' * 20)
print('Escopo de variável')
print('-=' * 20)
# Escopo de variável

def teste(b):
    global a # nao criará nova variavel, vai substituir valor da global
    a = 8 # cria variavel local != da variavel global
    b += 4
    c = 2
    print(f'"A" dentro vale {a}')
    print(f'"B" dentro vale {b}')
    print(f'"C" dentro vale {c}')

a = 5
teste(a) # variavel global
print(f'"A" fora(bolsonaro) vale {a}')
# print(f'"B" fora vale {b}') Esses prints comentados so funcionariam dentro da função
# print(f'"C" fora vale {c}') pois as variáveis são locais e não globais


print('-=' * 20)
print('Retono de Valores')
print('-=' * 20)
# Retorno de valores

def somar(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus cálculos dera {r1}, {r2} e {r3}')