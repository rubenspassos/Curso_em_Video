times = ('Palmeiras', 'Athletico-PR','Atlético-MG','Corinthians',
         'Internacional','Fluminense','São Paulo','Flamengo',
         'Botafogo','Santos','Avaí','Coritiba','América-MG',
         'Red Bull Bragantino','Ceará','Atlético-GO',
         'Cuiabá', 'Juventude' ,'Fortaleza')
print('*' * 40)
# Como eu pensei
#for cont in range(0,5):
#    print(f'Os 5 primeros são {times[cont]}')
print(f'Os 5 primeires são {times[0:5]}')
print('*' * 40)
# Como eu pensei
#for cont in range(1,5):
#   cont_inverso = len(times) - cont
#    print(f'Os quatro ultimos times são {times[cont_inverso]}')
print(f' Os 4 ultimos times são: {times[-4:]}')
print('*' * 40)
print(f'Classificação por ordem alfabética:{sorted(times)} ')
print('*' * 40)
print(f'O Palmeiras está na {times.index("Palmeiras")+1} posição')
print('*' * 40)


