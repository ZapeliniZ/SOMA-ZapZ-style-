#coding: utf-8

def forma1_leitura():
    split()
    tamanho_vet = len(vet)
    for i in range(tamanho_vet):
        (vet[i])
    print(vet)

def forma2_leitura():
    vet = list(map(int, input().split()))
    tamanho_vet = len(vet)
    for i in range(tamanho_vet):
        vet[i] = 3*vet[i]
        print(vet[i], end = ' ')
    print()

#maneira otimizada:

import array as ar
def forma3_leitura_array():
    vet = ar.array('i', map(int, input().split()))
    tamanho_vet = len(vet)


if __name__ == "__main__":
    #forma1_leitura()
    #forma2_leitura()
    forma3_leitura_array()