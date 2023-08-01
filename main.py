from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

from PIL import Image, ImageTk

# Criando janela

janela = Tk()
janela.title('CONTROLE FINANCEIRO')
janela.geometry('880x600')
janela.configure(background='#B5B5B5')
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

# ==========  TITULOOOO ===============

Frame_header = Frame(janela, width=880, height=55, bg='#E7A33D')
Frame_header.grid(row=0,column=0,columnspan=2)

nome_logo = Label(Frame_header, text='CONTROLE FINANCEIRO',  width=900, compound=RIGHT, padx=5,font=('Ivy 18 bold'), anchor=NW, bg='#E7A33D', fg='#FFFFFF')
nome_logo.place(x=300, y=12)


# =============== PREENCHIMENTO DOS ITENS ==============

Frame_preencher = Frame(janela, width=880, height=150, bg='#575656')
Frame_preencher.grid(row=1,column=0,columnspan=2)

# ==== VALOR =======
vvalor = IntVar()
l_valor = Label(Frame_preencher, text='Digite um valor:', anchor=E, font=('verdana 10'), bg='#575656', fg='#FFFFFF')
l_valor.place(x=15, y=35)

e_valor = Entry(Frame_preencher,textvariable=vvalor, width=10, font=('Ivy 12'), justify='left', relief='solid')
e_valor.place(x=20, y=60)

# ==== DESCRIÇÃO =======
vDescricao = StringVar()
l_Descricao = Label(Frame_preencher,  text='Descrição..', anchor=E, font=('verdana 10'), bg='#575656', fg='#FFFFFF')
l_Descricao.place(x=150, y=35)
e_Descricao = Entry(Frame_preencher,textvariable=vDescricao, width=20, font=('Ivy 12'), justify='left', relief='solid')
e_Descricao.place(x=150, y=60)


# ==== POSITIVO OU NEGATIVO =======
l_positivo_ou_negativo = Label(Frame_preencher,  text='Selecione se entrou ou saiu dinheiro :', anchor=E, font=('verdana 10'), bg='#575656', fg='#FFFFFF')
l_positivo_ou_negativo.place(x=350, y=35)


vpositivoenegativo = StringVar()


l_selecionar_positivo = Radiobutton(Frame_preencher, text='Entrou +',variable=vpositivoenegativo, value='+', cursor='hand2')
l_selecionar_positivo.place(x=420 , y=60)


l_selecionar_negativo = Radiobutton(Frame_preencher, text='Saiu -',variable=vpositivoenegativo, value='-', cursor='hand2')
l_selecionar_negativo.place(x=420 , y=100)


# ======== IMPRESSÃO DOS DADOS ===========
Frame_Impressao_dos_dados = Frame(janela, width=800, height=300, bg='#D9D9D9')
Frame_Impressao_dos_dados.grid(row=2,column=0, columnspan=2)

tree = ttk.Treeview(Frame_Impressao_dos_dados, selectmode=BROWSE, columns=('column1', 'column2', 'column3'), show='headings')

tree.column('column1', width=150, minwidth=400, stretch=NO )
tree.heading('#1', text='SALDO')

tree.column('column2', width=470, minwidth=400, stretch=NO)
tree.heading('#2', text='DESCRIÇÃO')

tree.column('column3', width=137, minwidth=400, stretch=NO )
tree.heading('#3', text='ENTRADA / SAIDA')

Barra_de_rolagem = Scrollbar(Frame_Impressao_dos_dados, orient='vertical')
tree.configure(yscrollcommand= Barra_de_rolagem.set)
Barra_de_rolagem.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

tree.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

# ==== BOTÃO ====
def Adicionar():
    valor = e_valor.get()
    Descricao = e_Descricao.get()
    positivoenegativo= vpositivoenegativo.get()

    if valor == '' or Descricao == '' or positivoenegativo=='':
        messagebox.showinfo(title='ERRO', message='Preencha todos os dados!')
        print('PREENCHA OS CAMPOS CORRETAMENTE!')
        return
    else:
        dados = valor, Descricao, positivoenegativo
        tree.insert("", END, values=dados)
        e_valor.delete(0, END)
        e_Descricao.delete(0, END)

   

botao_Adicionar = Button(Frame_preencher, text='ADICIONAR',command= Adicionar , padx=10, width=15, anchor=CENTER, font=('Ivy 12 bold'), bg='#E7A33D', fg='#FFFFFF', cursor='hand2')
botao_Adicionar.place(x=650, y=60)

janela.mainloop()


