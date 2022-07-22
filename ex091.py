from random import randint
from time import sleep
jogadores = dict()
rank = list()
cont = 1
for g in range(1,5):
    jogadores[f'Player {g}'] = randint(1,6)

for m,n in jogadores.items():
    print(f'O {m} tirou {n}')
    sleep(1)

print(f'{"RANKING DOS JOGADORES":=^30}')
for i in sorted(jogadores, key=jogadores.get, reverse=True): #Organizando o dicionario por ordem crescente do valores
   print(f'O {cont}º lugar: {i} com {jogadores[i]} ')
   cont += 1

