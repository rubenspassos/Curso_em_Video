jogador = dict()
partidas = soma = 0
gols = list()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))
for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1} ')))
    soma += gols[c]
jogador['gols'] = gols
jogador['total'] = soma
print('-=' * 30)
print(jogador)
print('-=' * 30)
for n,m in jogador.items():
    print(f'O {n} tem o valor {m}')
print('-=' * 30)
print(f'O Jogaodor {jogador["nome"]} jogaou {partidas} partidas')
for c, d in enumerate(gols):
    print(f'=> Na partida {c}, ele fez {d} gols')
print(f'Foi um total de {soma} gols')
