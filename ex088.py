
from random import randint
from time import sleep
le = []
print('-' * 40)
print(f'{"JOGA NA MEGA SENA": ^40}')
print('-' * 40)
op = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=' * 3, f'SORTEANDO {op} JOGOS', '=-' * 3)
for c in range(0,op):
    li = []
    while True:
        r = randint(1,60)
        if r not in li:
            li.append(r)
        if len(li) == 6:
            break
    le.append(li[:])
for p in range(0,op):
    print(f'Jogo {p+1}: {sorted(le[p])}')
    sleep(1)
print(f'{"BOA SORTE!":=^30}')



