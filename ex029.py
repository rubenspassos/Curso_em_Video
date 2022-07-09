velo = float(input('Digite a Velocidade do veículo: '))
if velo > 80:
    print('Você ultrapassou a velocidade maxima da via')
    valor = (velo - 80) * 7
    print('O valor a ser pago é de R${:.2f} '.format(valor))
else:
    print('Siga bem caminhoneiro')
