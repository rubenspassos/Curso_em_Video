primo = int(input('Digite um numero: '))
soma = 0
for cont in range(1,primo + 1):
    if primo % cont == 0:
        soma = soma + 1
if soma == 2:
    print('O numero {} é primo'.format(primo))
else:
    print('O numero {} não é primo'.format(primo))