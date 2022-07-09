# Importa o modulo datetime
from datetime import date
# Recebe a variável inserida pelo usuário
data_nasc = int(input('Digite o ano do seu nascimento: '))
# Verifica data atual
data_atual = date.today().year
# Calcula a idade do usuário
idade = data_atual - data_nasc
# imprimi o resultado conforme condicionante
if idade < 18:
    print('Você \033[35mainda vai se alistar\033[m ao serviço militar')
    saldo = 18 - idade
    print('Ainda falta {} anos para você se alistar'.format(saldo))
elif idade == 18:
    print('Está na \033[35mhora de se alistar\033[m ao serviço militar. ', end=(''))
    print('Apresente-se IMEDIATAMENTE!')
else:
    print('Já \033[35mpassou do tempo do alistamento\033[m ao serviço militar')
    saldo = idade - 18
    print('Voce deveria ter se alistado a {} anos'.format(saldo))