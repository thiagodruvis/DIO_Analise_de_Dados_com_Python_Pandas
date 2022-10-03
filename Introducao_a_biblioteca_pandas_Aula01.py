### **Python para análise de dados(Pandas) - Thiago Drummond Rabello**

#importando a biblioteca pandas 
import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Gapminder.csv", error_bad_lines=False, sep=";")

#Visualizando as 5 primeiras linhas 
df.head()

df = df.rename(columns={"country":"Pais", "continent":"continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap":"PIB"})

df.head()

df.head(10)

#Total de linhas e colunas
df.shape

df.columns

df.dtypes

df.tail(15)

#informações estatísticas do conjundo de dados
df.describe()

df["continente"].unique()

Oceania = df.loc[df["continente"] == "Oceania"]
Oceania.head()

Oceania["continente"].unique()

df.groupby("continente")["Pais"].nunique()

# Saber qual expectativa de vida(a média de vida) para cada ano
df.groupby("Ano")["Expectativa de vida"].mean()

df["PIB"].sum()

df["PIB"].mean()