
def script01():
        vC = [1 , 3.4 , 'A' , "IFSC"]
        #print(vC)
        #input("pressione enter para continuar")
        #print("Inserção de 56 na posição 0")
        vC.insert(0,56)
        #print(vC)
        #input("pressione enter para continuar")
        #print("Inserção de B na posição 3")
        vC.insert(3,'B')
        #print(vC)
        #input("inserção no final do vetor de '11'")
        vC.append(11)
        vC.append('A')
        #print(vC)
        return vC

def script02(vetA):
        print("Vetor recebido:", vetA)
        print("Remoção do valor", vetA[2])
        vetA.remove(3.4)
        print("Escolha a remoção do A:")
        choice = input("Pressione 1 para remover o primeiro 'A' e dois para o segundo. Pressione qualquer outra tecla para remover os dois: ")
        if(choice == '1'):
                vetA.remove('A')
        else:
            while "A" in vetA:
                        vetA.remove('A')        
        print("vertor final", vetA)

def script03(vetB):
        print("vetor recebido", vetB)
        positionI = 1
        positionF = 3
        del vetB[positionI:positionF]
        print(f"Vetor com posição {positionI}:{positionF} removida: ", vetB)
        print("remoção por pop: ")
    
if __name__ == "__main__":
        vet = script01()
        #script02(vet)
        script03(vet)