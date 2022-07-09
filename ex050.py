valor_final = 0
contador = 0
for cont in range(1,7):
    n1 = int(input('Entre com o {}º valor: '.format(cont)))
    if n1 % 2 == 0:
        valor_final = n1 + valor_final
        contador = contador + 1
print('A soma dos {} numeros pares digitados é {}'.format(contador, valor_final))