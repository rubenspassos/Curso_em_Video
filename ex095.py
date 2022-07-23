inf_jog = dict()
part = list()
jogadores = list()
cod = soma = dados = 0
while True:
    inf_jog['cod'] = cod
    cod += 1
    inf_jog['nome'] = str(input('Qual o nome do jogador? ').title().strip())
    jogos = int(input('Quantas partidas ele jogou? '))
    for c in range(1,jogos+1):
        part.append(int(input(f'Quantos gols na partida {c}? ')))
    inf_jog['partidas'] = part[:]
    soma = sum(part)
    inf_jog['soma'] = soma
    jogadores.append(inf_jog.copy())
    part.clear()
    while True:
        opçao = str(input('Deseja continuar? [S/N] ').upper().strip()[0])
        print('-' * 40)
        if opçao == 'N' or opçao == 'S':
            break
        else:
            print('Opção inválida, digite novamente.')
    if opçao == 'N':
        break
print('-=' * 20)
print(f'{"cod":<5}{"nome":<8}{"gols":<20}{"total":>4}')
print('-' * 40)
for c in jogadores:
    print(f'{c["cod"]:<5}', end='')
    print(f'{c["nome"]:<8}', end ='')
    print(f'{c["partidas"]}', end='')
    print(f'{c["soma"]:>5}')
print('-' * 40)
print(jogadores[0]['partidas'])
while True:
    dados = int(input('Mostrar dados de qual jogador? '))
    if dados == 999:
        break
    elif dados < len(jogadores):
        print(f'--- LEVANTAMENTO DO JOGADOR: {jogadores[dados]["nome"]}')
        cont = 1
        for val in jogadores[dados]['partidas']:
            print(f'No jogo {cont} fez {val} gols')
            cont += 1
    elif dados >= len(jogadores):
        print(f'ERRO! Não exite jogador com código {dados}! Tente novamente ')
