idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você \033[35mainda vai se alistar\033[m ao serviço militar')
elif idade == 18:
    print('Está na \033[35mhora de se alistar\033[m ao serviço militar')
else:
    print('Já \033[35mpassou do tempo do alistamento\033[m ao serviço militar')