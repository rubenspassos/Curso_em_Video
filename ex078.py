lista = []
for cont in range(0,5):
    lista.append(int(input('Digite um valor: ')))
print(f'Você digitou os valores{lista}')
print(f'O maior valor digitado foi {max(lista)} na posição',end='')

for c, l in enumerate(lista):
    if max(lista) == lista[c]:
        print(f' {c}...', end='')

print(f'\nO menor valor digitado foi {min(lista)} na posição', end='')
for c , l in enumerate(lista):
    if min(lista) == lista[c]:
        print(f' {c}...', end='')

