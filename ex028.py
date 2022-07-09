import random
from time import sleep
from random import randint

n = random.randint(1,5)
print('-=-' * 18)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-' * 18)
n2 = int(input('Qual número eu pensei: '))
print('PROCESSANDO...')
sleep(3)
print(" Parabuens você acertou" if n == n2 else 'Você errou, tente novamente')

