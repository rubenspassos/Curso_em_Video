def menuOpcoes(num):
    from time import sleep
    while True:
        print('-' * 30)
        print('MENU PRINCIPAL'.center(30))
        print('-' * 30)
        print(f'1 - \033[32mVer pessos Cadastradas\033[m')
        print(f'2 - \033[32mCadastrar nova Pessoa\033[m')
        print(f'3 - \033[32mSair do Sistema\033[m')
        print('-' * 30)
        while True:
            try:
                entrada = int(input(num))
                if entrada < 3:
                    print('-' * 30)
                    print(f'OPÇÃO {entrada}'.center(30))
                    print('-' * 30)
                    sleep(2)
                    break
                elif entrada == 3:
                    print('Fim do Programa. Até logo!!')
                    return 0
                else:
                    print('\033[31mERRO! Digite uma opção válida\033[m')
                    continue
            except (TypeError, ValueError):
                print('\033[31mERRO! Por favor, digite um número inteiro válido\033[m')
                continue
            except KeyboardInterrupt:
                print('O usuário preferiu encerrar a aplicação')
            return entrada


# Progama Principal
v1 = menuOpcoes('\033[36mSua Opção: \033[m')
