# Tuplas ()
# Listas []
# Dicionário {}

#dados = dict()
dados = {'Nome':'Pedro','Idade':12}
print(dados['Nome'])# obs se o print for formatado (f') o valor do
                    # dicionário deverar ficar em aspas duplas ("")
print(dados['Idade'])

dados['Sexo'] = 'M'
print(dados)

del dados['Idade']
print(dados)

print('=' * 60)
#================================================================

filme = {'titulo':'Stars Wars',
         'ano':1977,
         'diretor':'George Lucas'
         }
print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')

print('=' * 60)
#===================================================================

locadora = list()
locadora.append(filme)
print(locadora)
print(locadora[0]['ano'])

print('=' * 60)
#==================================================================

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()