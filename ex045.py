from random import choice
from time import sleep
#Boas vindas ao usuário
print('{:=^40}'.format('='))
print('{:=^40}'.format(' VINDO AO JOGO JOKENPÔ '))
print('{:=^40}'.format('='))
print('{: ^40}'.format( 'PEDRA , PAPEL, TESOURA'))
print('{:=^40}'.format('='))
cont1 = 0
cont2 = 0
for cont in range(0,3):
      print('pontuação player: {}'.format(cont1))
# Insere um valor randomico
      lista = ['PEDRA','PAPEL','TESOURA']
      cpu = choice(lista)
# Recebe valor inserido pelo usuário
      player = str.upper(input('Digite um valor: '))
      sleep(0.1)
      print('JO', end=(''))
      sleep(.3)
      print('KEN', end=(''))
      sleep(.3)
      print('PÔ')
      sleep(.2)
      print('{:=^40}'.format('='))
# Imprime resultado
      if player == 'PEDRA' and cpu == 'TESOURA' or player == 'PAPEL' and cpu == 'PEDRA' or player == 'TESOURA' and cpu == 'PAPEL' :
            print('Player is {} and CPU {} \n\33[32mPlayer is WIN!!!!\33[m'.format(player,cpu))
            cont1 += 1
      elif player == 'PEDRA' and cpu == 'PAPEL' or player == 'PAPEL' and cpu == 'TESOURA' or player == 'TESOURA' and cpu == 'PEDRA' :
            print('Player is {} and CPU {} \n\33[31mPlayer is LOSE!!!!\33[m'.format(player,cpu))
            cont2 += 1
      elif player == 'PEDRA' and cpu == 'PEDRA' or player == 'TESOURA' and cpu == 'TESOURA' or player == 'PAPEL' and cpu == 'PAPEL':
            print('Player is {} and CPU {} \n\33[90mTIED GAME!!!\33[m'.format(player,cpu))
      else:
            print('Digite um valor válido')
print('=' * 40)
print('''Resultado final 
Player = {}
CPU = {}'''. format(cont1,cont2))
print('=' * 40)