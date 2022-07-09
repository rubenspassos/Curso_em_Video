print('{:=^40}'.format(' Lojas do Rubão '))
preco = float(input('Digite o valor do produto: '))
print('''(1) A vista no dinheiro: 10% de desconto 
(2) A vista no cartão: 5% de desconto 
(3) Em 2x no cartão: Preço normal 
(4) Em 3x ou mais no cartão: 20% de juros''')

cond_pag = int(input('Digite a opção de pagamento: '))
if cond_pag == 1:
      valor = preco - (preco * 10/100)
      print('O valor a ser pago é de R${:.2f}'.format(valor))
elif cond_pag == 2:
      valor = preco - (preco * 5 / 100)
      print('O valor a ser pago é de R${:.2f}'.format(valor))
elif cond_pag == 3:
      print('O valor a ser pago é de R${:.2f}'.format(preco))
elif cond_pag == 4:
      valor =  preco + (preco * 20 / 100)
      print('O valor a ser pago é de R${:.2f}'.format(valor))
      parcelas = int(input('Em quantas vezes deseja parcelar? '))
      parcelado = valor / parcelas
      print('Valor parcelado = {} de R${:.2f}'.format(parcelas,parcelado))
else:
      print('Favor informar uma opção válida de pagamento')
