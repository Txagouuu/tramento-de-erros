# Exemplo básico sobre tratamento de erros e exceções em Python

# 1. Exemplo de bloco try-except básico
try:
    num = int(input("Digite um número: "))
    print(f"O dobro do número é {num * 2}")
except ValueError:
    print("Erro: Você não digitou um número válido.")

# 2. Uso da cláusula else
try:
    num = int(input("Digite outro número: "))
except ValueError:
    print("Erro: Entrada inválida.")
else:
    print(f"Você digitou um número válido: {num}")

# 3. Uso da cláusula finally
try:
    arquivo = open("exemplo.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
finally:
    print("Encerrando o bloco try-finally.")


# 4. Definição de uma exceção personalizada
class MinhaExcecao(Exception):
    """Exceção personalizada para demonstração."""

    def __init__(self, mensagem):
        super().__init__(mensagem)


try:
    valor = -1
    if valor < 0:
        raise MinhaExcecao("Erro personalizado: Valor não pode ser negativo.")
except MinhaExcecao as e:
    print(f"MinhaExceção capturada: {e}")
