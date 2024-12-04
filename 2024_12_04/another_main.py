class Computador():
    def __init__(self):
        self.marca = ''
        self.memoria = ''
        self.placaV = ''
    def set_computador(self):
        self.marca = input("Digite a marca do computador: ")
        self.memoria = input("Digite a quantidade de memória: ")
        self.placaV = input("Digite a placa de vídeo: ")
    def get_computador(self):
        print("Marca do computador:", self.marca)
        print("Memória do computador:", self.memoria)
        print("Placa de vídeo do computador:", self.placaV)
Lista_computadores = []
for _ in range(10):
    A = Computador()
    Lista_computadores.append(A)
print("Pc1")
Lista_computadores[0].set_computador()
Lista_computadores[0].get_computador()
print(" ")
print("Pc2")
Lista_computadores[1].set_computador()
Lista_computadores[1].get_computador()