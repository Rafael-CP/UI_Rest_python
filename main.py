from tkinter import *
from tkinter import messagebox
import pymysql



class UserLogin():
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        #self.root.geometry('250x150')
        self.root.geometry('300x300')
        Label(self.root, text='Efetue o login').grid(row=0, column=0, columnspan=3)

        Label(self.root, text = 'Nome de usuário').grid(row = 1, column = 0)
        self.login = Entry(self.root)
        self.login.grid(row = 1, column = 1, columnspan = 2, padx = 3, pady = 3)

        Label(self.root, text='Senha').grid(row=2, column=0)
        self.password = Entry(self.root, show = '*')
        self.password.grid(row=2, column=1, columnspan=2, padx = 3, pady = 3)

        Button(self.root, text = 'Entrar', bg = 'green3', relief = 'flat', width = 7, command = self.entrarAdmin).grid(row = 5, column = 1, padx = 3, pady = 3) # relief = borda
        Button(self.root, text = 'Cadastrar', bg = 'yellow', command = self.cadastro).grid(row = 5, column = 2, padx = 3, pady = 3)
        Button(self.root, text = 'Verificar Cadastros', bg = 'orange').grid(row = 4, column = 1, columnspan = 3, padx = 3, pady = 3)

        self.depende = Toplevel() #cria uma instancia de tk, porem que depende da tela criada acima, que caso seja fechada, fechará esta junto
        self.depende['bg'] = 'black'
        self.depende.title('Teste')
        self.root.mainloop()

    def entrarAdmin(self):
        if (self.login.get() == 'admin') and (self.password.get() == '0000'):
            if messagebox.askyesno('Confirmação','Deseja realmente entrar?'):
                admin = Tk()
                admin.title("Janela do Administrador")
                admin.geometry('300x300')
                admin.mainloop()
        else:
            messagebox.showinfo('info', 'to u')
            messagebox.showwarning('warning', 'u were warned')
            messagebox.showerror('error', 'error')
            self.root.destroy()

    def cadastro(self):
        Label(self.root, text = 'Codigo de Segurança: ').grid(row = 3, column = 0, padx = 5, pady = 5)
        self.Codigo = Entry(self.root, show = '*')
        self.Codigo.grid(row = 3, column = 1, padx = 5, pady = 5, columnspan = 2)
        Button(self.root, text = 'Confirmar Cadastro').grid(row = 4, column = 1, padx = 5, pady = 5, columnspan = 2)


x = UserLogin()





