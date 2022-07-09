from random import randint
from time import sleep
print('-=' * 40)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 40)
cont = cont_cpu = 0
while True:
    cpu = randint(1,10)
    play_valor = int(input('Digite um valor: '))
    play_opção = str(input('Par ou Ímpar? [P/I] ').upper().strip()[0])
    resultado = (play_valor + cpu) % 2
    if resultado == 0 and play_opção == 'P' or resultado == 1 and play_opção == 'I':
        print('Voce VENCEU!')
        cont += 1
        print(f'Voce jogou {play_valor} e o computador {cpu}. Total de {play_valor+cpu}', 'DEU PAR.' if resultado == 0 else 'DEU ÍMPAR.')
        print('-=' * 40)
        print('Jogar Novamente')
        sleep(1)
    else:
        print(f'Você PERDEU! Você jogou {play_valor} e o computador {cpu}. Total de {play_valor+cpu}','DEU PAR.' if resultado == 0 else 'DEU ÍMPAR.')
        break
print('-=' * 40)
print(f'GAME OVER! Voce Venceu {cont} vezes')
print('-=' * 40)
