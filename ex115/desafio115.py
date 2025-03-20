from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)

print(cabecalho('Sistema de Arquivos'))
while True:
    resposta = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        LerArquivo(arq)
    elif resposta == 2:
        cabecalho('CADASTRAR NOVA PESSOA')
        nome = str(input('Nome:'))
        idade =leiaInt('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
            cabecalho('SAINDO DO SISTEMA .... ATÉ LOGO')
            break
    else:
        print('\033[31mERRO:  digite uma opção valida!!!\033[m')

    sleep(3)