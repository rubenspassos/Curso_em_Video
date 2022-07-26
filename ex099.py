# Desempacotamento de parâmetros
def maior(* num):
# importar biblioteca para ter pausas durante a execução do código
    from time import sleep
    print('-=' * 30)
    cont = maioral = 0
    # c = len(maior())
# Criar laço para imprimir valores da função maior
    for ind in num:
        print(f'{ind}', end=' ')
        sleep(.3)
        # Armazenar maior valor
        if cont == 0:
            maioral = ind
        else:
            if ind > maioral:
                maioral = ind
        cont += 1
# Imprimir valores obtidos
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor foi {maioral}')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()

