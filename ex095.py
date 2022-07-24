inf_jog = dict()
part = list()
jogadores = list()
cod = dados = 0
while True:
    #inf_jog['cod'] = cod
    #cod += 1
    inf_jog['nome'] = str(input('Qual o nome do jogador? ').title().strip())
    jogos = int(input('Quantas partidas ele jogou? '))
    for c in range(1,jogos+1):
        part.append(int(input(f'Quantos gols na partida {c}? ')))
    inf_jog['partidas'] = part[:]
    inf_jog['soma'] = sum(part)
    jogadores.append(inf_jog.copy())
    part.clear()
    while True:
        opçao = str(input('Deseja continuar? [S/N] ').upper().strip()[0])
        print('-' * 40)
        if opçao in "SN":
            break
        print('Opção inválida, digite novamente.')
    if opçao == 'N':
        break
print('-=' * 20)
print('cod ', end='')
#print(f'{"cod":<5}{"nome":<8}{"gols":<20}{"total":>4}')
for ind, val in enumerate(inf_jog.keys()):
    #if para formatação especifica por linha
    if ind == len(inf_jog)-3:
        print(f'{val:<10}', end='')
    if ind == len(inf_jog)-2:
        print(f'{val:<20}', end='')
    if ind == len(inf_jog)-1:
        print(f'{val:>5}', end='')
print()
for ind, val in enumerate(jogadores):
    print(f'{ind:>3} ', end='')
#print('-' * 40)
for ind, val in enumerate(inf_jog.values()):
    if ind == len(inf_jog)-3:
        print(f'{val:<10}', end='')
    if ind == len(inf_jog)-2:
        print(f'{str(val):<20}', end='')
    if ind == len(inf_jog)-1:
        print(f'{str(val):>5}', end='')
print()
    #print(f'{c["cod"]:<5}', end='')
    #print(f'{c["nome"]:<8}', end ='')
    #print(f'{c["partidas"]}', end='')
    #print(f'{c["soma"]:>5}')
print('-' * 40)
#print(jogadores[0]['partidas'])
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    elif dados < len(jogadores):
        print(f'--- LEVANTAMENTO DO JOGADOR: {jogadores[dados]["nome"]}')
        for ind, val in enumerate(jogadores[dados]['partidas']):
            print(f'No jogo {ind+1} fez {val} gols')
    elif dados >= len(jogadores):
        print(f'ERRO! Não exite jogador com código {dados}! Tente novamente ')
    print('--' * 20)
print(f'{"VOLTE SEMPRE":=^20}')