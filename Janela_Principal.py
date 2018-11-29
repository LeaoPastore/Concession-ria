# Importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from Janela_Menu import Janela_Menu

class Janela_Principal(Tk):

    def __init__(self, controle):

        self.controle = controle
        super().__init__()
        self.geometry('250x280+800+300')
        self.title('Concessionária')

        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.lbl_login = Label(self, text='Login')
        self.lbl_senha = Label(self, text = 'Senha')
        self.txt_login = Entry(self, width = 20)
        self.txt_senha = Entry(self, width = 20)
        self.btn_ok = Button(self, width=10, text='Ok', command= lambda: self.criar_terceira_janela(self.txt_login.get(),self.txt_senha.get()))

        self.btn_close.place(x=20, y=200)
        self.btn_ok.place(x=150, y=200)
        self.lbl_login.place(x=30, y=100)
        self.lbl_senha.place(x = 30, y = 150)
        self.txt_login.place(x=90, y=100)
        self.txt_senha.place(x=90, y = 150)


    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja sair?'):
            super().destroy()


    def menu_click(self):
       messagebox.showinfo('Menu', 'Clicou no item de menu!')

    def criar_terceira_janela(self, login, password):
        #print(self.findlist(self.format(self.readfile('Cadastro_Vendedor')), login)[1])
        #print(login)
        #login = self.findlist(self.readfile('Cadastro_Vendedor'),self.txt_login.get())[0]
        #password = self.findlist(self.readfile('Cadastro_Vendedor'),self.txt_senha.get())[1]

        if password == (self.findlist(self.format(self.readfile('Cadastro_Vendedor')), login)[1]):

            Janela_Menu(self)

        else:
            messagebox.showerror("Sem Permissão", "Login ou senha incorretos!")



    def readfile(self, file):
        f = open(file, 'r')
        a = f.read()
        f.close()
        return a

    def format(self, a):
        s = a.split('\n')
        for i in range(0, len(s)):
            s[i] = s[i].split(':')
        s.pop()
        return s

    def findlist(self, lista, id):
        for i in lista:
            if i[0] == id:
                return i

        return False