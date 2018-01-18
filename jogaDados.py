from tkinter import *
from random import *


######################################################################
#METODO PARA GERAR OS NUMEROS ALEATORIOS
def rolar():
    x=sp.get()
    cont = int(en.get())
    texto = []
    for i in range(0, cont):
        texto.append(randint(1, int(x)))
        if(cont > 1 and ((i+1) != cont)):
            texto.append("-")
    lb2["text"] = texto
######################################################################


######################################################################
#CRIANDO A JANELA PRINCIPAL
janela = Tk()
janela["bg"]= "#000000"
######################################################################


######################################################################
#LABEL PARA DADO
lb = Label(janela, text="DADO", font = "Helvetica 16 bold", bg="#000000", fg="#ffffff")
lb.grid(row=0)
######################################################################


######################################################################
#SPINBOX PARA SELECIONAR O TIPO DO DADO
sp = Spinbox(janela, values=(4,6,8,10,12,20,100), font = "Helvetica 16 bold")
sp.grid(row=1)
######################################################################


######################################################################
#LABEL PARA QUANTIDADE DE DADOS
lb3 = Label(janela, text="QUANTIDADE", bg="#000000", fg="#ffffff")
lb3.grid(row=3)
######################################################################


######################################################################
#SPINBOX PARA QUANTIDADE DE DADOS A SEREM ROLADOS
en = Spinbox(janela, from_=1, to=20, font="Helvetica 16 bold")
en.grid(row=4)
######################################################################


######################################################################
#BOTÃO QUE CHAMA O METODO QUE GERA OS NUMEROS ALEATORIOS, CONTEM UM BACKGROUND DE IMAGEM
bt = Button(janela, command=rolar, bg="#000000", font = "Helvetica 16 bold", fg="#000000",)
img1 = PhotoImage(file="Ten_sided_dice.png")
timg1 = img1.subsample(3,3)
bt.config(image=timg1, compound=RIGHT)
bt.grid(row=5, pady=10)
######################################################################


######################################################################
#LABEL QUE APRESENTA OS RESULTADOS
lb2 = Label(janela, text="RESULTADO", font = "Helvetica 16 bold", wraplength=400, bg="#000000", fg="#EE0000")
lb2.grid(row=6)
######################################################################

######################################################################
#INSERINDO A JANELA PRINCIPAL NO MAINLOOP
janela.mainloop()
######################################################################