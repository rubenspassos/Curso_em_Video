# Criar a função
def ficha(nome,gol):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '': # Na resolução do Guana, ele tratou melhor o retorno
                  # do gol, caso algo fosse digitado o valor
                  # de retorno seria 0
        gol = 0
    return nome, gol


# Solicitar o nome do jogador
r1 = ficha(nome=str(input('Nome do jogador: ')),
           gol=input("Gol do Jogador: "))

# imprimir informação solicitadas acima
print(f'O jogador {r1[0]} fez {r1[1]} gol(s) no campeonato.')



# Resolução do Guana
def ficha(jog = "<desconhecido>", gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')
# Programa principal
n = str(input(('Nome do Jogador: ')))
g = str(input('Numero de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)
