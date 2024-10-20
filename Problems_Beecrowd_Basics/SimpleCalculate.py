cod1, qtd1, vlr1 = map(float, input().split(" "))
cod2, qtd2, vlr2 = map(float, input().split(" "))
pgto = ((qtd1)*(vlr1))+((qtd2)*(vlr2))
print("VALOR A PAGAR: R$ {0:.2f}".format(pgto))