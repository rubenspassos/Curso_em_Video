ln = []
lnota = []
lt = []
cont = 0
while True:
    ln.append(str(input('Digite o nome do aluno: ').capitalize().strip()))
    lnota.append(float(input('Digite a primeira nota do aluno: ')))
    lnota.append(float(input('Digite a segunda nota do aluno: ')))
    lt.append([ln[:],lnota[:]])
    ln.clear()
    lnota.clear()
    cont += 1
    while True:
        op = str(input('Deseja Continuar: [S/N] ')).upper().strip()[0]
        if op == 'S' or op == 'N':
            break
        else:
            print('Opção invalida digite novamente')
    if op == 'N':
        break
print('-' * 30)
print(f'{"Nº":<4}{"Nome":<15}{"Média":>11}')
print('-' * 30)
acum = 0
acum2 = 0
for c in range(0,cont):
    print(f'{c:<4}{lt[acum2][acum][0]:<15}', end = '')
    acum += 1
    print(f'{(lt[acum2][acum][0]+lt[acum2][acum][1])/2:>11.1f}')
    acum = 0
    acum2 += 1
while True:
    c = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if  c < cont:
        print(f'Notas do {lt[c][0][0]} são {lt[c][1]}')
    elif c >= cont and c != 999:
        print('Opção invalida, digite novamente: ')
    else:
        break
print(f'{"Fim Programa!!!":=^30}')
