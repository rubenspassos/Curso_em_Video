from datetime import date
data = date.today().year
menor = 0
maior = 0
for cont in range(0,7):
    ano_nasc = int(input('Digite o ano de nascimento: '))
    if data - ano_nasc < 21:
        menor = menor + 1
    else:
        maior = maior + 1
print('''Das datas digitadas
{} são menores de idade
{} são maiores de idade'''.format(menor,maior))