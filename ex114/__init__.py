import requests

def verificar_site(url):
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print(f"O site {url} está online!")
        else:
            print(f"O site {url} respondeu com código {resposta.status_code}.")
    except requests.ConnectionError:
        print(f"O site {url} está offline ou inacessível.")
    except requests.Timeout:
        print(f"O site {url} demorou muito para responder (timeout).")
    except requests.RequestException as e:
        print(f"Ocorreu um erro ao acessar o site {url}: {e}")

# Exemplo de uso:
verificar_site("https://www.pudim.com.br")
