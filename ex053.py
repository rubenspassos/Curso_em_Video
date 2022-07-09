frase = str.strip(str.lower(input('Entre com uma frase: '))).replace(' ','')
cont_inv = frase[:: -1]
cont = 0
somador = 0
print(cont_inv)
'''for cont_inv in range(cont_inv, 0, -1):
    print(frase[cont_inv-1], end='')
    if frase[cont] == frase[cont_inv - 1]:
        somador = somador  + 1
    cont = cont + 1'''
if cont_inv == frase:
    print('A frase é um palíndromo ')
else:
    print('A frase NÃO é um palíndromo')
