lista = []
menor = 0
maior = 0
for cont in range(0,5):
    lista.append(int(input('Digite um valor: ')))
    if cont == 0:
        menor = lista[cont]
        maior = lista[cont]
        cont += 1
    elif lista[cont] > maior:
        maior = lista[cont]
    elif lista[cont] < menor:
        menor = lista[cont]
print(f'Você digitou os valores{lista}')

for c, maior in enumerate(lista):
    print(f'O maior valor digitado foi {maior}')
   # if maior == enumerate(lista):
      #  print(f'O maior valor digitado foi {maior} nas posições {c}')
print(menor)

