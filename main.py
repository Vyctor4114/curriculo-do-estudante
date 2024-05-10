import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox, StringVar, OptionMenu

def cadastrar():
    if not campoUsuario.get() or not campoSenha.get() or not campoCpf.get() or not campoData.get() or not varSexo.get():
        messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
        return

    if len(campoCpf.get()) != 11 or not campoCpf.get().isdigit():
        messagebox.showerror("Erro", "Por favor, insira um CPF válido.")
        return

    conn = sqlite3.connect('curriculo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS curriculos
                 (nome TEXT, cpf TEXT, senha TEXT, experiencia TEXT, data_nascimento TEXT, sexo TEXT)''')

    c.execute("INSERT INTO curriculos VALUES (?, ?, ?, ?, ?, ?)", (campoUsuario.get(), campoCpf.get(),
                                                                    campoSenha.get(), campoExperiencia.get(),
                                                                    campoData.get(), varSexo.get()))

    conn.commit()
    conn.close()

    resposta = Label(janela, text="Cadastrado com sucesso!!", fg="green")
    resposta.grid(column=0, row=10, columnspan=2, padx=5, pady=10)

    campoUsuario.delete(0, 'end')
    campoSenha.delete(0, 'end')
    campoCpf.delete(0, 'end')
    campoExperiencia.delete(0, 'end')
    campoData.delete(0, 'end')
    varSexo.set('')  # Resetar o valor do campo de sexo

janela = Tk()
janela.title("Currículo")
janela.geometry('500x480')

labels = ["Nome do Estudante:", "CPF:", "Senha:", "Experiência:", "Data de Nascimento:", "Sexo:"]
for i, label_text in enumerate(labels):
    Label(janela, text=label_text, fg="black").grid(column=0, row=i, padx=5, pady=5)

campoUsuario = Entry(janela, width=30)
campoUsuario.grid(column=1, row=0, padx=5, pady=5)

campoCpf = Entry(janela, width=30)
campoCpf.grid(column=1, row=1, padx=5, pady=5)

campoSenha = Entry(janela, width=30)
campoSenha.grid(column=1, row=2, padx=5, pady=5)

campoExperiencia = Entry(janela, width=30)
campoExperiencia.grid(column=1, row=3, padx=5, pady=5)

campoData = Entry(janela, width=30)
campoData.grid(column=1, row=4, padx=5, pady=5)

sexo_options = ['Masculino', 'Feminino', 'Outro']
varSexo = StringVar(janela)
varSexo.set('')  # Valor padrão vazio
sexo_dropdown = OptionMenu(janela, varSexo, *sexo_options)
sexo_dropdown.grid(column=1, row=5, padx=5, pady=5)

botao = Button(janela, text="Cadastrar", command=cadastrar, bg="orange", fg="white")
botao.grid(column=0, row=6, columnspan=2, padx=5, pady=5)

janela.mainloop()
