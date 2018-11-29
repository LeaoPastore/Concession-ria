from tkinter import *
from tkinter import messagebox

class Finalizando_Compra(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('550x650+800+300')
        self.title('Finalização da Compra')
        self.transient(parent)
        self.grab_set()

        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_ok = Button(self, width=10, text='Emitir NF', command=self.emitirnf)
        self.btn_atualizar = Button(self, width=40, text='Atualizar dados para emissão da NF', command=lambda: self.get_listas(self.txt_login.get(),self.txt_cpf.get(), self.txt_placa.get()))
        self.lbl_confirmarlogin = Label(self, text='Confirme o Login do vendedor')
        self.lbl_login = Label(self, width=20, text='Login')
        self.lbl_confirmarcpf = Label(self, text='Confirmar CPF do cliente')
        self.lbl_cpf = Label(self, width=20, text='CPF')
        self.lbl_confirmarplaca = Label(self, text='Confirme as informações do veículo')
        self.lbl_placa = Label(self, width=20, text='Placa')
        self.lbl_valor = Label(self, width=20, text='Valor da venda')

        self.lbl_nf = Label(self, text='Dados da Compra')
        self.lbl_infovendedor = Label (self, text='Informaçõs vendedor')
        self.lbl_nomevendedor1 = Label(self, text='Nome:')
        self.lbl_nomevendedor = Label(self, text='Vazio')
        self.lbl_telefonevendedor1 = Label(self,text='Telefone:')
        self.lbl_telefonevendedor = Label(self, text='Vazio')
        self.lbl_nummat1 = Label(self,text='Número da Matrícula:')
        self.lbl_nummat = Label(self, text='Vazio')
        self.lbl_infocomprador = Label (self, text='Informações Cliente')
        self.lbl_nomecomprador1 = Label(self, text='Nome:')
        self.lbl_nomecomprador = Label(self, text='Vazio')
        self.lbl_cpfcomprador1 = Label(self, text='CPF:')
        self.lbl_cpfcomprador = Label(self, text='Vazio')
        self.lbl_telefonecomprador1 = Label(self, text='Telefone:')
        self.lbl_telefonecomprador = Label(self, text='Vazio')
        self.lbl_endcomrpador1 = Label(self,text='E-mail:')
        self.lbl_endcomrpador = Label(self, text='Vazio')
        self.lbl_infcar = Label(self, text='Informações do carro')
        self.lbl_modelo1 = Label(self, text='Modelo:')
        self.lbl_modelo = Label(self, text='Vazio')
        self.lbl_ano1 = Label(self,text='Ano:')
        self.lbl_ano = Label(self, text='Vazio')
        self.lbl_cor1 = Label(self,text='Cor:')
        self.lbl_cor = Label (self, text='Vazio')
        self.lbl_valorconfirm1  =Label(self,text='Valor R$:')
        self.lbl_valorconfirm = Label(self, text='Vazio')
        self.lbl_placaconfirm1 = Label(self, text='Placa:')
        self.lbl_placaconfirm = Label(self, text='Vazio')

        self.txt_login = Entry(self, width=50)
        self.txt_cpf = Entry(self, width=50)
        self.txt_placa = Entry(self, width=50)
        self.txt_valor = Entry(self, width=50)

        self.btn_close.place(x=100, y=590)
        self.btn_ok.place(x=300, y=590)
        self.btn_atualizar.place(x=150,y=280)
        self.lbl_confirmarlogin.place(x=10, y=20)
        self.lbl_login.place(x=10, y=50)
        self.lbl_confirmarcpf.place(x=10, y=90)
        self.lbl_cpf.place(x=10, y=120)
        self.lbl_confirmarplaca.place(x=10, y=160)
        self.lbl_placa.place(x=10, y=200)
        self.lbl_valor.place(x=10, y=240)
        self.lbl_nf.place(x=10, y=320)
        self.lbl_infovendedor.place(x=10, y=345)
        self.lbl_nomevendedor1.place(x=10, y=370)
        self.lbl_nomevendedor.place(x=10, y=385)
        self.lbl_telefonevendedor1.place(x=220,y=370)
        self.lbl_telefonevendedor.place(x=220, y=385)
        self.lbl_nummat1.place(x=320, y=370)
        self.lbl_nummat.place(x=320, y=385)
        self.lbl_infocomprador.place(x=10, y=420)
        self.lbl_nomecomprador1.place(x=10, y=445)
        self.lbl_nomecomprador.place(x=10, y=460)
        self.lbl_cpfcomprador1.place(x=170, y=445)
        self.lbl_cpfcomprador.place(x=170, y=460)
        self.lbl_telefonecomprador1.place(x=270, y=445)
        self.lbl_telefonecomprador.place(x=270, y=460)
        self.lbl_endcomrpador1.place(x=370, y=445)
        self.lbl_endcomrpador.place(x=370, y=460)
        self.lbl_infcar.place(x =10, y=495)
        self.lbl_modelo1.place(x=10, y=520)
        self.lbl_modelo.place(x=10, y=535)
        self.lbl_ano1.place(x=110, y=520)
        self.lbl_ano.place(x=110, y=535)
        self.lbl_cor1.place(x=200, y=520)
        self.lbl_cor.place(x=200, y=535)
        self.lbl_valorconfirm1.place(x=280, y=520)
        self.lbl_valorconfirm.place(x=280, y=535)
        self.lbl_placaconfirm1.place(x=390, y=520)
        self.lbl_placaconfirm.place(x=390, y=535)

        self.txt_login.place(x=150, y=50)
        self.txt_cpf.place(x=150, y=120)
        self.txt_placa.place(x=150, y=200)
        self.txt_valor.place(x=150,y=240)

        self.bd_nf = []

    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja sair, o cadastro não foi finalizado?'):
            super().destroy()

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

    def findlistcar(self, lista, id):
        for i in lista:
            if i[4] == id:
                return i

        return False

    def get_listas(self, login, cpf, placa):

        a = (self.findlist(self.format(self.readfile('Cadastro_Vendedor')), login))
        b = (self.findlist(self.format(self.readfile('Cadastro_Comprador')), cpf))
        c = (self.findlistcar(self.format(self.readfile('Cadastro_Carro')), placa))
        self.lbl_nomevendedor.config(text=a[2])
        self.lbl_telefonevendedor.config(text=a[3])
        self.lbl_nummat.config(text=a[4])
        self.lbl_nomecomprador.config(text=b[1])
        self.lbl_cpfcomprador.config(text=b[0])
        self.lbl_telefonecomprador.config(text=b[2])
        self.lbl_endcomrpador.config(text=b[3])
        self.lbl_modelo.config(text=c[0])
        self.lbl_ano.config(text=c[1])
        self.lbl_cor.config(text=c[2])
        self.lbl_placaconfirm.config(text=c[4])
        self.lbl_valorconfirm.config(text=self.txt_valor.get())

    def emitirnf(self):
        self.bd_nf.append([self.lbl_nomevendedor.cget('text'),self.lbl_telefonevendedor.cget('text'),self.lbl_nummat.cget('text'),
                           self.lbl_nomecomprador.cget('text'), self.lbl_cpfcomprador.cget('text'), self.lbl_telefonecomprador.cget('text'),
                          self.lbl_endcomrpador.cget('text'),self.lbl_modelo.cget('text'), self.lbl_ano.cget('text'), self.lbl_cor.cget('text'),
                          self.lbl_valorconfirm.cget('text'), self.lbl_placaconfirm.cget('text')])
        f = open('Notas_Fiscais', '+a')
        f.write("%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s\n" % (self.bd_nf[0][0],self.bd_nf[0][1],self.bd_nf[0][2],self.bd_nf[0][3],self.bd_nf[0][4],self.bd_nf[0][5],
                                                self.bd_nf[0][6],self.bd_nf[0][7],self.bd_nf[0][8],self.bd_nf[0][9],self.bd_nf[0][10],self.bd_nf[0][11]))
        f.close()


        super().destroy()
