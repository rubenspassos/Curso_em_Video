pares = []
impares = []
numeral = []
#numeral = [[],[]] poderia ser declarado dessa forma
for cont in range(1,8):
    num = (int(input(f"Digite o {cont}º valor: ")))
    if num % 2 == 0:
        pares.append(num)
        # numeral[0].append(num) : Receberia o valor dessa forma
    else:
        impares.append(num)
        # numeral[1].append(num)
numeral.append(pares)
numeral.append(impares)
print(f'Os nuemros digitados foram {numeral}')
(numeral)[0].sort()
print(f'Os Valores pares foram {numeral[0]}')
numeral[1].sort()
print(f'Os Valores impares foram {numeral[1]}')