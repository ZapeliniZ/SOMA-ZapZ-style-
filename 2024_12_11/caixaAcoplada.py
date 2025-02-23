#coding: utf-8
import time
class CaixaAcoplada(object):
    def __init__(self):
        self.NivelAgua = 0
        self.NivelMax = 5.0 #Valor em litros
        self.NivelMin = 0.5
        self.Estado = 0 #0 - Vazio, 1 - cheio
        self.Vazao = 0.5 #Vazao = 0,5 litros por segundo
        self.VazaoSaida = 0.9

def EncherCaixa(self):
    print("Caixa enchendo, volume inicial = ", self.NivelAgua)
    while(self.NivelAgua<=self.NivelMax):
        self.NivelAgua+=self.Vazao
        time.sleep(0.75)
        print("Nivel de agua = ",self.NivelAgua)
    self.Estado = 1

def EsvaziarCaixa(Self):
    print("Caixa esvaziando, volume inicial = ", self.NivelAgua)
    while (self.NivelAgua>=Self.NivelMin):
        self.NivelAgua-=self.VazaoSaida
        time.sleep(0.5)
        print("Nivel de agua = ",self.NivelAgua)
    self.Estado = 0