#coding:utf-8

import tkinter as tk
import ColorPalette as pc

janela = tk.Tk()
janela.title("calc parte 1")
janela.geometry("240x320") #Comprimento e altura, pixeis janela

#Criação do frame visor
frame_visor=tk.Frame(janela, width = 240, height = 50, bg =pc.colorwhite)
frame_visor.grid(row = 0, column = 0)

#Criação do frame Botoes
frame_botoes = tk.Frame(janela, width = 240, height = 270, bg = pc.colorgray)
frame_botoes.grid(row = 1, column = 0)

#inclusao dos botoes
butao_11 = tk.Button(frame_botoes, text = "Clear", width = 12, height = 2)
butao_11.place(x=0, y=0)

#Butao12 e Butao13:
butao_12 = tk.Button(frame_botoes, text = "module", width = 4, height = 2)
butao_12.place(x=123, y=0)
butao_13 = tk.Button(frame_botoes, text = "/", width = 4, height = 2)
butao_13.place(x=182, y=0)

#Linha 2:
butao_21 = tk.Button(frame_botoes, text = "7", width = 4, height = 2)
butao_21.place(x=0, y=51)
butao_22 = tk.Button(frame_botoes, text = "8", width = 4, height = 2)
butao_22.place(x=64, y=51)
butao_23 = tk.Button(frame_botoes, text = "9", width = 4, height = 2)
butao_23.place(x=123, y=51)

janela.mainloop()