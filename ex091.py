from random import randint
from time import sleep
#from operator import itemgetter
jogadores = dict()
ranking = list()
cont = 1
for g in range(1,5):
    jogadores[f'Player {g}'] = randint(1,6)

for m,n in jogadores.items():
    print(f'O {m} tirou {n}')
    sleep(1)

print(f'{"RANKING DOS JOGADORES":=^30}')
for i in sorted(jogadores, key=jogadores.get, reverse=True): #Organizando o dicionario por ordem crescente do valores
   print(f'O {cont}º lugar: {i} com {jogadores[i]} ')
   sleep(1)
   cont += 1

#Este modo també funciona, foi proposto na resolução do exercício
# importando operador e itemgetter para criar lista ordenada.

#ranking = sorted(jogadores.items() ,key=itemgetter(1), reverse=True)
#for ind, val in enumerate(ranking):
#    print(f'{ind+1}º lugar: {val[0]} com {val[1]}')