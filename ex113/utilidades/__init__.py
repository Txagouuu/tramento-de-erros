def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Insira um valor válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mERRO: Usuário não desejou inserir um valor.\033[m")
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Insira um valor válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mERRO: Usuário não desejou inserir um valor.\033[m")
            return 0
        else:
            return n