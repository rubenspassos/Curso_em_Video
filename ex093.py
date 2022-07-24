jogador = dict()
partidas = 0
gols = list()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1} ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for n,m in jogador.items():
    print(f'O {n} tem o valor {m}')
print('-=' * 30)
print(f'O Jogaodor {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for c, d in enumerate(jogador["gols"]):
    print(f'=> Na partida {c}, ele fez {d} gols')
print(f'Foi um total de {jogador["total"]} gols')
