expressão = str(input('Digite uma expressão matemática: '))
abre = expressão.count('(')
fecha = expressão.count(')')
if abre % 2 == 0 and fecha % 2 == 0:
    print("Sua expressão é válida")
else:
    print('Sua expressão não é valida')

