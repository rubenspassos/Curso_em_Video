valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
meses = int(input('Em quantos meses pretende pagar o fananciamento? '))
mensalidade = valor / meses
print(mensalidade)
if  mensalidade <= salario * 30/100:
    print('Parabens seu finaciamento foi aprovado, você pagará {} parcelas de \033[31mR${:.2f} '.format(meses,mensalidade))
elif mensalidade > salario * 30/100:
    print('Infelismente não foi possivel aprovar o seu financiamento')

