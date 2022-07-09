cont = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o Segundo Valor: '))
while cont != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa''')
    num_opcao = int(input('>>>>> Qual é a sua opção: '))
    if num_opcao == 1:
        soma = n1 + n2
        print('O valor da soma dos valores {} e {} é igual a {}'.format(n1, n2, soma))
    elif num_opcao == 2:
        mult = n1 * n2
        print('A multiplicação do valores {} e {} é igual a {}'.format(n1, n2, mult))
    elif num_opcao == 3:
        if n1 > n2:
            print('O maior numero digitado foi {}'.format(n1))
        else:
            print('O maior numero digita foi {}'.format(n2))
    elif num_opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o Segundo Valor: '))
    elif num_opcao == 5:
        cont = 5
    elif num_opcao > 5:
        print('Digite uma opção válida')
    print('=' * 50)
print('Fim do programa')
