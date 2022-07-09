soma_num = 0
c = "S"
cont = 0
while c == 'S':
    num = int(input('Digite um numero: '))
    soma_num += num
    if cont == 0:
        num_maior = num
        num_menor = num
    if num_maior < num:
        num_maior = num
    if num_menor > num:
        num_menor = num
    cont = cont + 1
    c = str(input('Deseja continuar: S/N ')).upper().strip()[0]
print('A média da soma dos {} numeros digitados é {}'.format(cont,soma_num/cont))
print('O maior numero digitado é {}'. format(num_maior))
print('O Menor número digitado é {}'.format(num_menor))

