tupla = ('borracha', 'abacate', 'limao' ,
         'cenoura', 'pomar', 'ilixir',
         'mulher tetuda', 'teste', 'finalizar')
# Como eu pensei
'''cont = 0
while cont < len(tupla):
    print(f'Na Palavra {tupla[cont]} temos ', end='')
    if tupla[cont].count('a') > 0:
        print('a', end=' ' )
    if tupla[cont].count('e') > 0:
        print('e',end=' ')
    if tupla[cont].count('i') > 0:
        print('i', end=' ')
    if tupla[cont].count('o') > 0:
        print('o', end=' ')
    if tupla[cont].count('u') > 0:
        print('u', end=' ')
    print('')
    cont += 1'''
for p in tupla:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


