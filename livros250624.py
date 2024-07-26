import pandas as pd 

df = pd.read_csv("tabela_livros.csv")

df_filtrado = df[df["Ano de Publicação"] == 1993]
print(df_filtrado)
