from datetime import datetime, date
# Recebe entrada como string
nasc_strg = str(input('Digite a data de nascimento: '))

# Lê data atual
hoje = date.today()
# Tranforma string em data com datetime Obs (%Y 4 ano 4 digitos) (%y ano 2 digitos)
nasc = datetime.strptime(nasc_strg,'%d/%m/%Y').date()
# Calcula idade e verificando aniversário do ano atual - Caso Falso terá valor -1
idade = hoje.year - nasc.year - ((hoje.month,hoje.day) < (nasc.month, nasc.day))
# Imprimi resultado
if idade <= 9:
    print('Até 9 anos: Categoria \33[34mMIRIM\33[m')
    if (hoje.month,hoje.day) == (nasc.month, nasc.day):
        print('PARABENS HOJE É SEU ANIVERSARIO')
elif idade >= 10 and idade <= 14:
    print('Até 14 anos: Categoria \33[34mINFANTIL\33[m ')
    if (hoje.month,hoje.day) == (nasc.month, nasc.day):
        print('PARABENS HOJE É SEU ANIVERSARIO')
elif idade >= 15 and idade <= 19:
    print('Até 19 anos: Categoria \33[34mJUNIOR\33[m')
    if (hoje.month,hoje.day) == (nasc.month, nasc.day):
        print('PARABENS HOJE É SEU ANIVERSARIO')
elif idade == 20:
    print('Até 20 anos: Categoria \33[34mSÊNIOR\33[m')
    if (hoje.month,hoje.day) == (nasc.month, nasc.day):
        print('PARABENS HOJE É SEU ANIVERSARIO')
else:
    print('Acima dos 20 anos: Categoria \33[34mMASTER\33[m')
    if (hoje.month,hoje.day) == (nasc.month, nasc.day):
        print('PARABENS HOJE É SEU ANIVERSARIO')