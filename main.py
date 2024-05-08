from tkinter import Tk, Label, Entry, Button

def cadastrar():
    resposta = Label(janela, text="Cadastrado com sucesso!!")
    resposta.grid(column=0, row=6, padx=5, pady=10)

    print("Usuário:", campoUsuario.get(), "Senha:", campoSenha.get(), "CPF:", campoCpf.get(), "Data de Nascimento:", campoData.get())

    # Clear entry fields after successful registration
    campoUsuario.delete(0, 'end')
    campoSenha.delete(0, 'end')
    campoCpf.delete(0, 'end')
    campoData.delete(0, 'end')

janela = Tk()
janela.title("Currículo")
janela.geometry('300x300')

titulo = Label(janela, text="Currículo do Estudante")
titulo.grid(column=0, row=0, padx=10, pady=10)

nomeLabel = Label(janela, text="Nome do Estudante")
nomeLabel.grid(column=0, row=1, padx=5, pady=10)
campoUsuario = Entry(janela, width=10)
campoUsuario.grid(column=1, row=1, padx=1, pady=10)

cpfLabel = Label(janela, text="CPF")
cpfLabel.grid(column=0, row=2, padx=1, pady=5)
campoCpf = Entry(janela, width=10)
campoCpf.grid(column=1, row=2, padx=1, pady=5)

senhaLabel = Label(janela, text="Senha")
senhaLabel.grid(column=0, row=3, padx=1, pady=5)
campoSenha = Entry(janela, width=10)
campoSenha.grid(column=1, row=3, padx=1, pady=10)

dataLabel = Label(janela, text="Data de Nascimento")
dataLabel.grid(column=0, row=4, padx=1, pady=5)
campoData = Entry(janela, width=10)
campoData.grid(column=1, row=4, padx=1, pady=10)

botao = Button(janela, text="Cadastrar", command=cadastrar)
botao.grid(column=0, row=5, padx=1, pady=5)

janela.mainloop()
