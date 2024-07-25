import pandas as pd

# Definição da Classe Livro
class Livro:
    def __init__(self, titulo, autor, categoria, ano_publicacao, ativo):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano_publicacao = ano_publicacao
        self.ativo = ativo

# Função para ler a tabela de livros e criar instâncias da classe Livro
def ler_tabela_livros():
    # Carrega o arquivo CSV para um DataFrame do Pandas
    df = pd.read_xlsx('Tabela_de_Livros_em_Portugu_s_e_Programa__o.xlsx')
    
    # Lista para armazenar as instâncias da classe Livro
    lista_livros = []
    
    # Itera sobre as linhas do DataFrame
    for index, row in df.iterrows():
        # Cria uma instância da classe Livro para cada linha da tabela
        livro = Livro(row['titulo'], row['autor'], row['categoria'], row['ano_publicacao'], row['ativo'])
        lista_livros.append(livro)
    
    return lista_livros

# Função para imprimir os atributos dos 10 primeiros livros
def imprimir_10_primeiros_livros(lista_livros):
    # Limita a impressão aos 10 primeiros livros
    for i in range(min(len(lista_livros), 10)):
        livro = lista_livros[i]
        print(f"=== Livro {i+1} ===")
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Categoria: {livro.categoria}")
        print(f"Ano de Publicação: {livro.ano_publicacao}")
        print(f"Ativo: {livro.ativo}")
        print()

# Ler a tabela de livros e criar a lista de instâncias da classe Livro
lista_de_livros = ler_tabela_livros()

# Imprimir os atributos dos 10 primeiros livros
imprimir_10_primeiros_livros(lista_de_livros)
