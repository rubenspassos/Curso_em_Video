valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos pretende pagar o fananciamento? '))
mensalidade = valor / (anos * 12)
if  mensalidade <= salario * 30/100:
    print('Parabens seu finaciamento foi aprovado, você pagará {} parcelas de \033[31mR${:.2f} '.format(meses,mensalidade))
else:
    print('Infelismente não foi possivel aprovar o seu financiamento')

