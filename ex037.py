num = int(input('Entre com um numero inteiro: '))
opcao = int(input('''Digite a base para conversão:
      1 Para Binário
      2 Para Octal
      3 Para Hexadecimal: '''))

if opcao == 1:
      print("O valor {} em binário é {}".format(num, bin(num)[2:]))
elif opcao == 2:
      print('O valor {} em Octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
      print('O valor {} em Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
      print('Valor inválido')