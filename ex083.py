expressão = str(input('Digite uma expressão matemática: '))
if expressão.count('(') == expressão.count(')'):
    print("Sua expressão é válida")
else:
    print('Sua expressão não é valida')

