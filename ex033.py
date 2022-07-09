sal = float(input('Digite o salário do funcionário: '))
if sal > 1250:
    aum = sal + (sal * 10/100)
    print('O novo salário com aumento de 10% será de {:.2f}'.format(aum))
else:
    aum = sal + (sal * 15/100)
    print('O novo salário com aumento de 15% será de {}' .format(aum))