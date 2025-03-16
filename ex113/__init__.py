def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except ValueError:
            print("ERRO! Por favor, digite um número real válido.")
