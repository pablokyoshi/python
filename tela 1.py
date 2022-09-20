#tela1.python

import tkinter as tk

#cria uma instância
janela=tk.Tk()
#Adiciona um título
janela.title("Bem vindo ao Tkinter")

texto=tk.Label(janela, text=("Este é um Label"),font=("Arial Bold",200))
texto.grid(column=0,row=0)

botao=tk.Button(janela,text='Sair', height=5,width=35, command=janela.destroy)
botao.grid(column=0, row=1)


janela.geometry('1960x500')


#Inicia GUI
janela.mainloop()

