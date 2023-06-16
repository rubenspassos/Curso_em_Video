from ex115.lib.interfaces import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas ','Cadastrar novas pessoas','Sair do Sistema'])
    if resposta == 1:
        # cabeçalho('Opção 1')
        lerArquivo(arq)
    elif resposta == 2:
        # cabeçalho('Opção 2')
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ').strip().title())
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    elif KeyboardInterrupt:
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)

