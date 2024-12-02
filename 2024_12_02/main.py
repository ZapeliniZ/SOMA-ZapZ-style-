def RequisicaoBasica():
    import requests, json
    url = "https://www.mercadobitcoin.net/api/BTC/trades/1686731660/1686733260/"
    requisicao = requests.get(url)
    lista1 = requisicao.json()
    print(lista1)
    print("Quantidade de dados:", len(lista1))

if __name__ == "__main__":
    RequisicaoBasica()