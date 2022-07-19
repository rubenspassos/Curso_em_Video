matriz = []
l1 = []
l2 = []
l3 = []
for cont in range (0,3):
    l1.append(int(input(f'Digite o valor [0,{cont}] ')))
cont = 0
for cont in range (0,3):
    l2.append(int(input(f'Digite o valor [1,{cont}] ')))
cont = 0
for cont in range (0,3):
    l3.append(int(input(f'Digite o valor [2,{cont}] ')))
matriz.append([l1[:],l2[:],l3[:]])
#print(matriz)
print(f'[  {matriz[0][0][0]}  ][  {matriz[0][0][1]}  ][  {matriz[0][0][2]}  ]')
print(f'[  {matriz[0][1][0]}  ][  {matriz[0][1][1]}  ][  {matriz[0][1][2]}  ]')
print(f'[  {matriz[0][2][0]}  ][  {matriz[0][2][1]}  ][  {matriz[0][2][2]}  ]')


