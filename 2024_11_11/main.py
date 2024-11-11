def script01():
    Diario_Notas = {'Joao':5, 'Julia':7}
    Nota = Diario_Notas['Joao']
    print(Nota)

def script02():
    Preco={} 
    Preco ["manga"] = 6
    Preco ["banana"] = 4
    Preco ["maçã"] = 10
    print(Preco)

def scrpit03():
    pessoa = dict(nome="Carol", idade = 18, altura = 1.8)
    print("Dicionario de entrada")
    #Retorna dados em tupla
    for elemento in pessoa.items():
        print(elemento[0], ":", elemento[1])

def script04():
    dic = {i:i**2 for i in range(5)}
    print(dic)

def script05():
    frutas = ["maçã", 'pera', 'uva', 'melancia', 'mamão']
    precos = ["12", '10', '10', '8', '11']
    pprint({frutas[i]:precos[i] for i in range(len(frutas))})

if __name__ == "__main__":
    #script01()
    #script02()
    #scrpit03()
    #script04()
    script05()