from random import choice
#Boas vindas ao usuário
print('-*' * 16)
print('BEM VINDO AO JOGO JOKENPÔ')
print('-*' * 16)
print('PEDRA , PAPEL, TESOURA')
# Insere um valor randomico
lista = ['PEDRA','PAPEL','TESOURA']
cpu = choice(lista)
# Recebe valor inserido pelo usuário
player = str.upper(input('Digite um valor: '))
# Imprime resultado
if player == 'PEDRA' and cpu == 'TESOURA' or player == 'PAPEL' and cpu == 'PEDRA' or player == 'TESOURA' and cpu == 'PAPEL' :
      print('Player is {} and CPU {} \n\33[32mPlayer is WIN!!!!\33[m'.format(player,cpu))
elif player == 'PEDRA' and cpu == 'PAPEL' or player == 'PAPEL' and cpu == 'TESOURA' or player == 'TESOURA' and cpu == 'PEDRA' :
      print('Player is {} and CPU {} \n\33[31mPlayer is LOSE!!!!\33[m'.format(player,cpu))
elif player == 'PEDRA' and cpu == 'PEDRA' or player == 'TESOURA' and cpu == 'TESOURA' or player == 'PAPEL' and cpu == 'PAPEL':
      print('Player is {} and CPU {} \n\33[90mTIED GAME!!!\33[m'.format(player,cpu))
else:
      print('Digite um valor válido')