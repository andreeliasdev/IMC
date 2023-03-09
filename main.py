from tkinter import *
from tkinter import ttk, Label

################# cores ###############

co0 = "#4065a1"  # azul
co1 = "#000000"  # preto


janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg=co1)
style = ttk.Style(janela)
style.theme_use("clam")

# dividindo a tela
parte_cima = Frame(janela, width=295, height=50, bg=co1, pady=0, padx=0, relief="flat", )
parte_cima.grid(row=0, column=0, sticky=NSEW)

parte_baixo = Frame(janela, width=295, height=200, bg=co1, pady=0, padx=0, relief="flat", )
parte_baixo.grid(row=1, column=0, sticky=NSEW)



# ---------------- Configuracoes do Frame cima ---------------------

nome_aplicativo = Label(parte_cima, text="Calculadora de IMC", width=23, height=1, padx=0, relief="flat", anchor="center",
                        font=('Arial 16 bold'), bg=co1, fg=co0)
nome_aplicativo.place(x=0, y=2)

linha_cima = Label(parte_cima, text="", width=400, height=1, padx=0, relief="flat", anchor="nw", font=('Arial 1'),
                   bg=co0, fg=co1)
linha_cima.place(x=0, y=35)

# ---------------- Configuracoes do Frame_baixo ---------------------

l_peso = Label(parte_baixo, text="Insira seu peso", height=1, padx=0, relief="flat", anchor="center",
               font=('Arial 10 bold'), bg=co1, fg=co0)
l_peso.grid(row=0, column=0, columnspan=1, sticky=NW, pady=10, padx=3)
e_peso = Entry(parte_baixo, width=5, font=('Arial 10 bold'), justify='center', relief=SOLID)
e_peso.grid(row=0, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(parte_baixo, text="Insira sua altura", height=1, padx=0, relief="flat", anchor="center",
                 font=('Arial 10 bold'), bg=co1, fg=co0)
l_altura.grid(row=1, column=0, columnspan=1, sticky=NW, pady=10, padx=3)
e_altura = Entry(parte_baixo, width=5, font=('Arial 10 bold'), justify='center', relief=SOLID)
e_altura.grid(row=1, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

l_resultado: Label = Label(parte_baixo, width=5, text="---", height=1, padx=6, pady=12, relief="flat", anchor="center",
                           font=('Arial 24 bold'), bg=co0, fg=co1)
l_resultado.place(x=175, y=10)

l_resultado_texto = Label(parte_baixo, width=37, text="", height=1, padx=0, pady=12, relief="flat", anchor="center",
                          font=('Arial 10 bold'), bg=co1, fg=co0)
l_resultado_texto.place(x=0, y=85)

# ------------ Botao calcular ------------------

b_calcular = Button(parte_baixo, text="Calcular", width=34, height=1, overrelief=SOLID, bg=co0, fg="white",
                    font=('Arial 10 bold'), anchor="center", relief=RAISED)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)


def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get()) ** 2
    resultado = peso / altura

    if resultado < 18.6:
        l_resultado_texto['text'] = "Seu IMC é: Abaixo do peso"
    elif resultado >= 18.5 and resultado < 24.9:
        l_resultado_texto['text'] = "Seu IMC é: Ideal, parabéns!!"
    elif resultado >= 25 and resultado < 29.9:
        l_resultado_texto['text'] = "Seu IMC é: levemente acima do peso"
    elif resultado >= 30 and resultado <34.9:
        l_resultado_texto['text'] = "Seu IMC é: Obesidade Grau 1"
    elif resultado >= 35 and resultado <39.9:
        l_resultado_texto['text'] = "Seu IMC é: Obesidade Grau 2"
    else:
        l_resultado_texto['text'] = "Seu IMC é: Obesidade Grau 3"

    l_resultado['text'] = "{:.{}f}".format(resultado, 2)

b_calcular = Button(parte_baixo, command=calcular, text="Calcular", width=34, height=1, overrelief=SOLID, bg=co0,
                    fg="white", font=('Arial 10 bold'), anchor="center", relief=RAISED)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)

janela.mainloop()



