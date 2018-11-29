from tkinter import *
from tkinter import messagebox
from Janela_Vendedor import Janela_Vendedor
from Dados_Carro import Dados_Carro
from Janela_Patio import Janela_Patio
#from testeprojeto.Janela_Comprador import Janela_Comprador

class Janela_Menu(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('250x250+800+300')
        self.title('Menu')
        self.transient(parent)
        self.grab_set()

        self.btn_close = Button(self, width=15, text='Encerrar Sessão', command=self.destroy)
        self.btn_vendedor= Button(self, width=10, text='Cadastro\nVendedor', command = self.cadastro_vendedor)
        self.btn_carro = Button(self, width=10, text='Cadastro\nCarro', command = self.cadastro_carro)
        self.btn_venda = Button(self, width=10, text='Apagar\nCarro')
        self.btn_vender = Button(self, width=10, text='Realizar\nVenda', command = self.carros)

        self.btn_close.place(x=65, y=200)
        self.btn_vendedor.place(x=20, y=60)
        self.btn_carro.place(x=150, y=60)
        self.btn_venda.place(x= 20, y = 130)
        self.btn_vender.place(x = 150, y = 130)

        '''self.menu = Menu(self)
        # Criando um item de menu e subtitens
        self.menu_principal = Menu(self.menu, tearoff=0)
        self.menu_principal.add_command(label='Compradores')
        self.menu_principal.add_command(label='Vendedores')
        # Criar terceira janela
        self.menu_principal.add_command(label='Carros Vendidos')
        # Criar quarta janela
        self.menu_principal.add_separator()
        self.menu_principal.add_command(label='Sair', command=self.destroy)
        self.menu.add_cascade(label='Menu', menu=self.menu_principal)
        # Mostrando o menu
        self.config(menu=self.menu)
'''
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja encerrar sua sessão?'):
            super().destroy()

    def cadastro_vendedor(self):
        Janela_Vendedor(self)


    def cadastro_carro(self):
        Dados_Carro(self)

    def carros(self):
        Janela_Patio(self)
