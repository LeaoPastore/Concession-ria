from tkinter import *
from tkinter import messagebox

class Janela_Comprador(Toplevel):

    def __init__(self, parent):

        super().__init__(parent)
        self.geometry('500x250+800+300')
        self.title('Cadastro Comprador')
        self.transient(parent)
        self.grab_set()

        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_ok = Button(self, width=10, text='Ok', command=self.cadastro_carro)

        self.lbl_comprador = Label(self, width=20, text='CPF')
        self.lbl_cpf = Label(self, width=20, text='Nome do Comprador')
        self.lbl_tel = Label(self, width=20, text='Telefone')
        self.lbl_email = Label(self, width=20, text= "E-mail")

        self.txt_comprador = Entry(self, width=50)
        self.txt_cpf = Entry(self,width=50)
        self.txt_tel = Entry(self,width=50)
        self.txt_email = Entry(self,width=50)


        self.btn_close.place(x=100, y=200)
        self.btn_ok.place(x=300, y=200)

        self.lbl_comprador.place(x=10, y=30)
        self.lbl_cpf.place(x=10, y=70)
        self.lbl_tel.place(x=10, y=110)
        self.lbl_email.place(x=10, y=150)

        self.txt_comprador.place(x=150, y=30)
        self.txt_cpf.place(x=150, y=70)
        self.txt_tel.place(x=150, y=110)
        self.txt_email.place(x=150, y=150)

        self.dados_comprador = []


    def destroy(self):
         if messagebox.askokcancel('Confirmação', 'Deseja sair, o cadastro não foi finalizado?'):
            super().destroy()

    def cadastro_carro(self):
        self.dados_comprador.append([self.txt_comprador.get(), self.txt_cpf.get(), self.txt_tel.get(), self.txt_email.get()])
        f = open('Cadastro_Comprador', '+a')
        f.write("%s:%s:%s:%s\n" % (
        self.dados_comprador[0][0], self.dados_comprador[0][1], self.dados_comprador[0][2], self.dados_comprador[0][3]))
        f.close()

        print('Dados do comprador:')
        print('CPF:', self.txt_comprador.get())
        print('Nome:', self.txt_cpf.get())
        print('Telefone:', self.txt_tel.get())
        print('Email:', self.txt_email.get())
        super().destroy()