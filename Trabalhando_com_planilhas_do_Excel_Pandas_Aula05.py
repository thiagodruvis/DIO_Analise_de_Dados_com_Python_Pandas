**Trabalhando com Planilhas do Excel** 

#importando a biblioteca
import pandas as pd

#Leitura dos arquivos
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

#juntando todos os arquivos
df = pd.concat([df1,df2,df3,df4,df5])

#exibindo as 5 primeiras linhas 
df.head()

#exibindo as 5 ultimas linhas
df.tail() 

df.sample(5)

#verficando cada tipo de dado de cada coluna
df.dtypes

#Alterando o tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")

df.dtypes

df.head()

**Tratando Valores Faltantes **

#Consultando linhas com valores faltantes
df.isnull().sum()

#Substituindo os valores nulos pela média
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

df.isnull().sum()

#Substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace=True)

#Apagando linhas com valores nulos 
df.dropna(inplace=True)

#Apagando as linhas com valores nulos com base apensa em 1 coluna 
df.dropna(subset=["Vendas"], inplace=True)

#Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)

**Criando colunas novas**


# Criando a coluna de receita 
df["Receita"] = df["Vendas"].mul(df["Qtde"])

df.head()

# Achar a colona de quantidade 
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

df.head()

#Retornando a maior receita
df["Receita"].max()

#Retornando a menor receita
df['Receita'].min()

#nlargest
df.nlargest(3, "Receita")


#nsmallest
df.nsmallest(3, "Receita")

#Agrupamento por cidade
df.groupby("Cidade")["Receita"].sum()

# ordenando conjunto de dados (nesse caso as 10 maiores receitas)
df.sort_values("Receita", ascending=False).head(10)

**Trabalhando com datas**

#Transformando a coluna de data em tipo inteiro
df['Data'] = df['Data'].view("int64")

#Verificando o tipo de dado de cada coluna
df.dtypes

#Transformando coluna de data em data
df['Data'] = pd.to_datetime(df["Data"])

df.dtypes

#Agrupamento por ano 
df.groupby(df['Data'].dt.year)["Receita"].sum()

#Criando uma nova coluna com o ano 
df["Ano_Venda"] = df["Data"].dt.year

df.sample(5)

#Extraindo mes do dia 
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

df.sample(5)

#Retornando a data mais antiga
df["Data"].min()

#calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()

df.sample(5)

#criando a coluna de trimestre 
df["trimestre_venda"] = df["Data"].dt.quarter

df.sample(5)

#Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

vendas_marco_19.sample(20)

# **Visualização de dados** 

df["LojaID"].value_counts(ascending=False)

#Grafico de barras
df["LojaID"].value_counts(ascending=False).plot.barh();

#Grafico de barras horizontais 
df["LojaID"].value_counts(ascending=True).plot.barh();

#grafico de pizza 
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie();

#Total vendas por cidade
df['Cidade'].value_counts()

#adicionando um título e alterando o nome dos eixos 
import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

#Alterando a cor 
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="black")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

#Alterando o estilo
plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total Produtos vendidos x mes")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend();

df.groupby(df['mes_venda'])["Qtde"].sum()

#Selecionando apenas as vendas de 2019
df_2019 = df[df["Ano_Venda"] == 2019]

#Total produtos vendidos por mÊs
[=- ]
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(title = "Total de produtos vendidos X mes", marker = "v")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend();

#Histograma
plt.hist(df["Qtde"], color="orangered");

 plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"]);

#Salvando em png
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend()
plt.savefig("grafico QTDE x MES.png")

