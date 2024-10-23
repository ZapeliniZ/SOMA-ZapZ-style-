
def compressãoLista1():
    nomes = ["Larissa", "Rafael", "Marcos", "Joao"]
    strg = " Aprovado "
    nomes_aprovados = []#Lista vazia
    for nome in nomes:
        saida = nome+strg
        nomes_aprovados.append(saida)
    print(nomes_aprovados)
    nomes2 = ["Ana, Cala", "rotundo", "Henrique"]
    strg = " Reprovado "
    nomes_reprovados = [nome+strg for nome in nomes2]
    print(nomes_reprovados)

if __name__ == "__main__":
    compressãoLista1()
    
