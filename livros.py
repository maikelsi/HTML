import pandas as pd

df = pd.read_csv("tabela_livros.csv")

print(df)

class Livro:
    def __init__(self, titulo, autor, categoria, ano, ativo):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano = ano
        self.ativo = ativo

livro0 = Livro("livro 0", "Julio Cezar","Programação", "2012", "Sim")
livro1 = Livro("Livro 1", "Julio Cezar","Programação", "2012", "Sim")
livro2 = Livro("Livro 2", "Julio Cezar","Programação", "2012", "Sim")
lista_de_livros = [livro0, livro1, livro2]

for livro in lista_de_livros:
    print(livro.titulo)