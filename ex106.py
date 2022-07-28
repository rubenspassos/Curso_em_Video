# menu=[]
# menu.append('SISTEMA DE AJUDA PYHELP')
# tam = len(menu[0]) + 6
# print(f'\033[45m'+ '~' * tam)
# print(f'{menu[0].center(tam)}')
# print(f'~' * tam)
# print(f'\033[m', end='')
# lista = list()
# while True:
#
#     lista.append("Acessando o manual do comando")
#     lista.append(str(input('Função ou Biblioteca ou Fim para sair ').lower().strip()))
#     if lista[1] not in "fim":
#         tam = len(lista[0]) + len(lista[1]) + 6
#         print(f'\033[41m' + '~' * tam)
#         print(f'   {lista[0]} {lista[1]}')
#         print(f'~' * tam)
#         print(f'\033[m', end='')
#         print(f'\033[47m')
#         print(help(lista[1]))
#         print(f'\033[m')
#         lista.clear()
#     else:
#         break
# print('ATÉ LOGO')
from time import sleep      # REsolução do Guana - Muito mais organizada do quem a minha resolução

c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m')     # 6 - preto


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor],end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#Programa principal

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!', 1)
