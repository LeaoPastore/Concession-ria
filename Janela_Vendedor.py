from tkinter import *
from tkinter import messagebox

# Classe Segunda_Janela
class Janela_Vendedor(Toplevel):
    # Metodo construtor
    def __init__(self, parent):
        # Chamar o init da classe mae
        super().__init__(parent)
        self.geometry('500x290+800+300')
        self.title('Cadastro Vendedor')
        self.transient(parent)
        self.grab_set()

        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_ok = Button(self, width=10, text='Ok', command=self.cadastro_comprador)#add funcao para salvar
        self.lbl_nome = Label(self, width=20, text='Login')
        self.lbl_tel = Label(self, width=20, text='Senha')
        self.lbl_mat = Label(self, width=20, text='Nome')
        self.lbl_senha = Label(self, width=20, text= "Telefone")
        self.lbl_obs = Label(self, width=20, text="Matrícula")
        self.txt_nome = Entry(self, width=50)
        self.txt_tel = Entry(self,width=50)
        self.txt_mat = Entry(self,width=50)
        self.txt_senha = Entry(self,width=50)
        self.txt_obs = Entry(self, width=50)

        self.btn_close.place(x=100, y=240)
        self.btn_ok.place(x=300, y=240)
        self.lbl_nome.place(x=10, y=30)
        self.lbl_tel.place(x=10, y=70)
        self.lbl_mat.place(x=10, y=110)
        self.lbl_senha.place(x=10, y=150)
        self.lbl_obs.place(x=10, y=190)
        self.txt_nome.place(x=150, y=30)
        self.txt_tel.place(x=150, y=70)
        self.txt_mat.place(x=150, y=110)
        self.txt_senha.place(x=150, y=150)
        self.txt_obs.place(x=150, y=190)

        self.dados_vendedor = []


        # Metodo para fechar a janela
    def destroy(self):
        # Janela de confirmacao
        if messagebox.askokcancel('Confirmação', 'Deseja sair, o cadastro não foi finalizado?'):
            super().destroy()

    def cadastro_comprador(self):
        self.dados_vendedor.append([self.txt_nome.get(), self.txt_tel.get(), self.txt_mat.get(), self.txt_senha.get(), self.txt_obs.get()])
        f = open('Cadastro_Vendedor', '+a')
        f.write("%s:%s:%s:%s:%s\n"%(self.dados_vendedor[0][0], self.dados_vendedor[0][1],self.dados_vendedor[0][2],self.dados_vendedor[0][3],self.dados_vendedor[0][4]))
        f.close()

        print('Cadastro vendedor:')
        print('Login:', self.txt_nome.get())
        print('Senha:', self.txt_tel.get())
        print('Nome:',self.txt_mat.get())
        print('Telefone:',self.txt_senha.get())
        print('Matrícula',self.txt_obs.get())
        super().destroy()
        #print(self.dados_vendedor[0])

