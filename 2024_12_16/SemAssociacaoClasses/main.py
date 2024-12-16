#coding: utf-8
import CaixaAcoplada as CA

if __name__=="__main__":
	Vaso = CA.CaixaAcoplada()
	Vaso.IniciarUtilizacao()
	print("Nivel atual de água: ",Vaso.get_nivel_agua())
	Vaso.EncherCaixaAcoplada()
	print("Nivel atual de água: ",Vaso.get_nivel_agua())
	while True:	
		Vaso.AcionarDescarga()
		print("Nivel atual de água: ",Vaso.get_nivel_agua())
		print("Deseja enviar para manutenção?")
		print("Digite 1 para sim, outra tecla para usar o vaso.")
		resposta = input()
		if resposta == '1':
			Vaso.EnviarCaixaManutencao()
			break