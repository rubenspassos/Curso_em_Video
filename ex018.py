d = int(input('Digite a quantidade de dias '))
km = float(input('Digite a quantidade de Quilometros percorrido '))
total = (d * 60) + (km * 0.15)
print(' O total a pagar é R${:.2f} '.format(total))