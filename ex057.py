sexo = str(input('Entre com o Sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Entre com um valor válido ')).strip().upper()[0]
print('Sexo registrado com sucesso.')
