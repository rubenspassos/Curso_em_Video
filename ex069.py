
pessoa = homem = mulher_menor = maior = 0
continuar = 'S'
while True:
    if continuar == 'N':
        break
    print('-=' * 20)
    print('CADASTRE UMA PESSOA')
    print('-=' * 20)
    idade = int(input('Digite a Idade: '))
    while True:
        sexo = str(input('Digite o Sexo:  [M/F] ').upper().strip()[0])
        if sexo == 'M' or sexo == 'F':
            break
    if continuar == 'S':
        if idade >= 18:
            maior += 1
        if sexo == 'M':
            homem += 1
        if sexo == 'F' and idade < 20:
            mulher_menor += 1
        while True:
            continuar = str(input('Deseja continuar? ').upper().strip()[0])
            if continuar == 'N' or continuar == 'S':
                break
print('Fim do Programa')
print(f'Total de Pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher_menor} com menos de 20 anos')