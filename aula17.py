num = [2 , 5 , 9 , 1] # Criando lisa []
num [2] = 3 # O espaço 2 da lista recebe o valor 3
num.append(7) # Insere valor 7 no final da lista
num.sort(reverse=True) #Apenas sort organiza de forma crescente/ reveser=True d
                       # e forma decrescente
num.insert(2,0) #Insere o valor 0 na posição 2
num.pop() #remove a ultima posisção
num.remove(2) #Remove o valor 2 da lista, caso encontre
print(num)
print(f'Essa lista tem {len(num)} elementos')

print('-' * 20)
print('Divisão do exercicio')
print('-' * 20)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')


print('-' * 20)
print('Divisão do exercicio')
print('-' * 20)

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei novamente ao final do exercício')