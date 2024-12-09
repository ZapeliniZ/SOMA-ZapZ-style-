#coding: utf-8

class ArquivoPastaSuspensa(object):
	def __init__(self, cor, departamento, NumMaxPastas=10): 
		self.cor = cor
		self.depto = departamento
		self.NumMaxPastas = NumMaxPastas
		self.estado = 0
		self.Pastas = [] 
		#print("cor = ", self.cor, "NumPastas = ", self.NumMaxPastas)
	
	def ReceberPasta(self, pasta):
		self.Pastas.append(pasta) 
		self.estado = 1
	
	def get_pastas(self): 
		for i in range(len(self.Pastas)): 
			print("Identificador da pasta: ",self.Pastas[i].id)
			print("Quantidade de documentos: ", len(self.Pastas[i].documento)) 

	def GavarArquivoPastaSuspensa(self):
		#Converter todos os documentos para um vetor e transferir para o arquivo
		vetorTemporario = [self.Pastas[1].documento for i in range(len(self.Pastas))]
		print(vetorTemporario)
		with open("gravacaoPasta.json", "w", encoding = "utf-8") as gr:
			