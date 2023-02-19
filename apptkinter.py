from tkinter import *

root= Tk()

root.title("Bem vindo a Força Geek")
root.geometry('350x200')

menu = Menu(root)
item = Menu(menu)
item.add_command(label="new")
menu.add_cascade(label="file", menu=item)
root.config(menu=menu)


lbl = Label(root, text = "Você é um GEEK?")
lbl.grid()

txt = Entry(root,width=10)
txt.grid(column=1, row=0)



def clicked():
    res = "Você Escreveu:  " + txt.get()
    lbl.configure(text= res)

botao = Button(root, text = "Clique", fg = "red", command=clicked)

botao.grid(column=2, row=0)

root.mainloop()