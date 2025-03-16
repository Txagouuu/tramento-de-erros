def dobro(preco, formato = False):
    res = preco * 2
    return res if formato is False else moeda(res)

def metade(preco, formato = False):
    res = preco / 2
    return res if formato is False else moeda(res)


def aumentar(preco,taxa, formato = False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco,taxa, formato = False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def linha():
    print('='*30)


def moeda(preco=0,moeda='R$'):
    """"
    Transforma o valor inserido do dinheiro para forma brasileira.
    trocando ponto por virgula.
    e trocando caso haja necessidade
    :param preco: valor a ser formatado
    :param moeda: tipo da moeda
    :param return: valor formatado
    funcao replace faz a troca de ponto por virgula
    """

    return f'{moeda}{preco:>.2f}'.replace('.',',')


def resumo(preco,aumento=10,disconto=5):
    print('Resumo'.center(30))
    linha()
    print(f'Analizando o valor: \tR${moeda(preco)}')
    print(f'A metade: \t\t\t\tR${metade(preco, True)}')
    print(f'O dobro: \t\t\t\tR${dobro(preco, True)}')
    print(f'Aumento de {aumento}%: \t\tR${aumentar(preco, aumento, True)}')
    print(f'Redução de {disconto}%: \t\tR${diminuir(preco, disconto, True)}')
    linha()