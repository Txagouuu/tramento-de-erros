def linha(tam=42):
    return '=' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    return ''

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


