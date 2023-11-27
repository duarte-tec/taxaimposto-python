#Alunos:
#Lucas da Silva Duarte
#Claudenilson da Silva Clemente
#Sandro Marcelo Fernandes Monteiro

from tkinter import *
from tkinter import messagebox

class Produto:  
    imposto = 0.15
    lista_produtos = []
    
    def __init__(self, toplevel):
        toplevel.title("Cadastro de Produtos")
        toplevel.geometry("500x400")
        toplevel.configure(background="#1C1C1C")

        self.frame1 = Frame(toplevel)
        self.frame1.pack()

        Label(self.frame1, text="Nome do Produto:", width=17, background="#1C1C1C", foreground="#FFFFFF").pack(side=TOP)
        self.valor1 = Entry(self.frame1, width=20)
        self.valor1.pack(side=BOTTOM)

        self.frame2 = Frame(toplevel)
        self.frame2.pack()

        Label(self.frame2, text="Valor do Produto:", width=17, background="#1C1C1C", foreground="#FFFFFF").pack(side=TOP)
        self.valor2 = Entry(self.frame2, width=20)
        self.valor2.pack(side=BOTTOM)

        self.frame3 = Frame(toplevel)
        self.frame3.pack()

        Label(self.frame3, text="Quantidade:", width=17, background="#1C1C1C", foreground="#FFFFFF").pack(side=TOP)
        self.valor3 = Entry(self.frame3, width=20)
        self.valor3.pack(side=BOTTOM)

        self.frame4 = Frame(toplevel, pady=5, background="#1C1C1C")
        self.frame4.pack()

        self.cadastro = Button(self.frame4, text="Cadastrar Produto", command=self.cadProduto, background="#B0C4DE", foreground="#1C1C1C")
        self.cadastro.pack(side=TOP)

        self.frame5 = Frame(toplevel, pady=5, background="#1C1C1C")
        self.frame5.pack()

        self.listar = Button(self.frame5, text="Listar Produtos", command=self.listarProdutos, background="#B0C4DE", foreground="#1C1C1C")
        self.listar.pack(side=BOTTOM)

        self.lista = Listbox(toplevel, width=50, height=12)
        self.lista.pack()

    def cadProduto(self):
        try:
            nomedoitem = str(self.valor1.get())
            valor = float(self.valor2.get())
            quantidade = int(self.valor3.get())
            valortotal = round(((valor * (Produto.imposto + 1)) * quantidade), 2)
            valorimposto = round((valor * (Produto.imposto + 1)), 2)

            produto = {
                "nome": nomedoitem,
                "valor": valorimposto,
                "valortotal": valortotal,
                "quantidade": quantidade
            }
            self.lista_produtos.append(produto)
            self.lista.insert(END, f"{produto['nome']}")
            messagebox.showinfo("Informação", "Produto cadastrado com sucesso.")

        except ValueError:
            messagebox.showerror("Erro", "Entrada(s) inválida(s). Digite outra vez.")    

    def listarProdutos(self):
        self.lista.delete(0, END)
        for produto in Produto.lista_produtos:
           self.lista.insert(END, f"nome: {produto['nome']}, valor: {produto['valor']}, qtd: {produto['quantidade']}, valor total: {produto['valortotal']}")

app = Tk()
Produto(app)
app.mainloop()
