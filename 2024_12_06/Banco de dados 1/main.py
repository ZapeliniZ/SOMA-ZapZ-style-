#coding: utf-8

import sqlite3 as sq
import time as t

def CriarBD(): 
	conexao = sq.connect("Funcionarios.db")
	cursor= conexao.cursor()
	return conexao, cursor

def CriarTabela(): 
	tabela = """
	create table if not exists Funcionarios(
		id integer primary key, 
		nome text not null, 
		cargo text not null, 
		dataContratacao text not null); 
		"""
	return tabela

def InserirDados(conexao, cursor, i): 
	nome = input('Digite um nome:')
	cargo = input('Digite um cargo:')
	data = input('Digite uma data no formato aaaa-mm-dd:')
	cursor.execute("INSERT INTO Funcionarios VALUES (?, ?, ?, ?)",(i, nome, cargo, data))
	conexao.commit()

def parte1():
	conexao, cursor = CriarConexaoBD()
	tabela = CriarTabela()
	cursor.execute(tabela)
	conexao.commit()
	for i in range(3):
		InserirDados(conexao, cursor, i)

def VerDados(conexao):
	cursor = conexao.cursor()
	cursor.execute("SELECT * FROM Funcionarios")
	return cursor.fetcha11() #Retorna na forma de vetor.

def DeletarDado():
	cursor.execute("DELETE FROM Funcionarios WHERE id = ?", (id,)) #precisa colocar vírgula no final
	conexao.commit()

def AlterarDado(conexao, id, cargo):
	cursor=conexao.cursor()
	cursor.execute("UPDATE Funcionarios SET cargo = ? WHERE id - ?", (cargo, id))

def Parte2():
	conexao, cursor = CriarConexaoBD()
	dados = VerDados(conexao)
	print(dados)
	t.sleep(2)
	InserirDados(conexao, cursor, 1)
	print(VerDados(conexao))
	t.sleep(2)
	AlterarDado(conexao, 1, "CEO")
	#print(VerDados(conexao))
	#DeletarDado(conexao, cursor, 1)
	#AlterarDado(conexao, 1, "CEO")
	#print(VerDados(conexao))
	
if __name__=="__main__": 
	#Parte1()
	Parte2() #Alterações no banco de dados