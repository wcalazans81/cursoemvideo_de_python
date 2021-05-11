from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'curso em video.txt'
if not arquivoExiste(arq):
    criarAquivo(arq)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #cabecalho('Opção 1')
        lerAquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_Int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
