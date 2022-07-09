nome = input('Digite o seu nome completo: ')
print(nome.upper())
print(nome.lower())
separado = nome.split()
print(len(''.join(separado))) #numero de letras no nome sem contar espaço
#print('Seu nome tem ao todo {} letras ' .format(len(nome) - nome.count(' ")))
print(nome.find(' '))
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separado[0], len(separado[0])))