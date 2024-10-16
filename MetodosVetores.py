#coding; utf-8

def Insercao_dados():
    vC = [1 , 3.4 , ’A’ , " IFSC " ]
    vC.insert(0,56) #Adiciona na posição 0 o inteiro 56.
    vC.insert(3,’B’)
    vC.append(11)
    for i in vC :
        print ( i )

def Remocao_dados(vet):
    print("Vetor recebido: ", vet)
    print("Elemento 'A' removido")
    vet.remove('A')
    print("Vetor alterado: ", vet)
    input("Digite enter para prosseguir")
if __name__ == "__main__":
    Insercao_dados()