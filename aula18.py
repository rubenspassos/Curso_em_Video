teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

#--------------------------------------------------------------------
print('-=' * 20)

galera1 = [['joão',19], ['Ana', 17], ['Pedro', 17],['Maria', 45]]
print(galera1)
print('-' * 20)
print(galera1[0])
print('-' * 20)
print(galera1[0][0])
print('-' * 20)
print(galera1[1][1])
print('-' * 20)

for p in galera1:
    print(p)
    print(f'{p[0]} tem {p[1]} anos')
#-------------------------------------------------------------------
print('-' * 20)

galera2 = list()
dado = list()
maior = menor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade ')))
    galera2.append(dado[:])
    dado.clear()
print(galera2)
print(dado)

for p in galera2:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores')
