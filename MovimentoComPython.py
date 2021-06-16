from tkinter import *

def movecima(event):
    canvas.move(imge, 0,-10)
def movebaixo(event):
    canvas.move(imge, 0,10)
def moveesquerda(event):
    canvas.move(imge, -10,0)
def movedireita(event):
    canvas.move(imge, 10,0)


janela = Tk()
janela.geometry("600x600")

janela.bind("<w>",movecima)
janela.bind("<s>",movebaixo)
janela.bind("<a>",moveesquerda)
janela.bind("<d>",movedireita)

fotocarro = PhotoImage(file= "aaa.png")

canvas =Canvas(janela, width=500, height=500)
canvas.pack

imge= canvas.create_image(10,10,image=fotocarro,)

janela.mainloop()