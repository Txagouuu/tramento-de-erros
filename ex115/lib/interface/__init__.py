def linha(tam=42):
    return '=' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    return ''

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc= leiaInt("Digite sua Opção: ")
    return opc
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Insira um valor válido.\033[m")
            continue

        except KeyboardInterrupt:
            print('\n' + '='*40)
            print("Saindo do programa...".center(40))
            print('=' * 40)
            return 0
        else:
            return n


