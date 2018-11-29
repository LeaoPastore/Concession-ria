# Importacao das bibliotecas
from tkinter import *
from tkinter import messagebox
from Verificar_Cliente import Verificar_Cliente

# Classe Segunda_Janela
class Janela_Patio(Toplevel):
    # Metodo construtor
    def __init__(self, parent):
        # Chamar o init da classe mae
        super().__init__(parent)
        self.geometry('200x500+800+300')
        self.title('Carros no Pátio')
        self.transient(parent)
        self.grab_set()


        for i in self.format(self.readfile('Cadastro_Carro')):
            btn = Button(self, width=10, text='%s' % i[4], command = self.verificar)
            btn.pack(side=TOP)

        # Widgets
        self.btn_close = Button(self, width=5, text='Voltar', command=self.destroy)

        # Posicionando os widgets
        self.btn_close.place(x=10, y=10)


    # Metodo para fechar a janela
    def menu_click(self):
       messagebox.showinfo('Menu', 'Clicou no item de menu!')

    def destroy(self):
        # Janela de confirmacao
        if messagebox.askokcancel('Confirmação','Deseja voltar ao menu?'):
            super().destroy()

    def verificar(self):
        Verificar_Cliente(self)

    def criar(self):

        self.menu_principal.add_command(label = (self.findlist(self.format(self.readfile('Cadastro_Carro')))))



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

    def contar(self, s):
        for i in range(0, len(s)):
            self.menu_principal.add_command(label = self.findlist(self.format(self.readfile('Cadastro_Carro'))))

    def findlist(self, lista):
        for i in lista:
            print(i[4])
            return i[4]

    def destruir(self):
        self.menu_principal.destroy()