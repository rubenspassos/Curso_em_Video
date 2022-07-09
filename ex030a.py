km = float(input('Digite a distancia da viagem em km: '))
'''if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45'''
valor = km * 0.50 if km <= 200 else km * 0.45
print('O valor da viagem será de R${:.2f}'.format(valor))