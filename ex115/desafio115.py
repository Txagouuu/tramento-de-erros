from ex115.lib.interface import *
from time import sleep
print(cabecalho('Sistema de Arquivos'))
while True:
    resposta = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        cabecalho('VER PESSOAS CADASTRADAS')
    elif resposta == 2:
        cabecalho('CADASTRAR NOVA PESSOA')
    elif resposta == 3:
        cabecalho('SAINDO DO SISTEMA .... ATÉ LOGO')
        break
    else:
        print('\033[31mERRO:  digite uma opção valida!!!\033[m')

    sleep(3)