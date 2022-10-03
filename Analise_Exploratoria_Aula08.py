# Importando as bibliotecasa
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

#upload do aqruivo 
from google.colab import files
arq = files.upload()

# Criando nosso DataFrame
df = pd.read_excel("AdventureWorks.xlsx")

# visualizando as 5 primeiras linhas 
df.head()

# quantidade de linhas e colunas
df.shape

# verificando os tipos de dados 
df.dtypes

# qual a receita total 
df["Valor Venda"].sum()

# Qual o custo total?
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) # criando a coluna custo

df.head(1)

# Qual o custo total? 
round(df["custo"].sum(), 2)

# Agora que temos a receita e custo e o total, podemos achar o lucro total
# Vamos criar uma coluna de Lucro que será Receita - Custo 
df["lucro"] = df["Valor Venda"] - df["custo"]

df.head(1)

# total lucro
round(df["lucro"].sum(),2)

# criando uma coluna com total de dias para enviar o prduto 
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

df.head(1)

### **Agora, queremos saber a média do tempo de envio para cada Marca, e para isso precisamos trannsformar a coluna Tempo_envio em numérica**

# Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df ["Data Venda"]).dt.days

df.head(1)

# verificando o tipo da cluna Tempo_envio
df["Tempo_envio"].dtype

# Média do tempo de envio por Marca
df.groupby("Marca")["Tempo_envio"].mean()



# **Missing Values**

# Verificando se temos dados faltantes
df.isnull().sum()

# **E, se a gente quiser saber o Lucro por Ano e Por Marca?**

# Vamos agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()

pd.options.display.float_format = '{:20,.2f}'.format

# resetando o index 
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano

# Qual o total de produtos vendidos ?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

# Gráfico Total de produtos Vendidos 
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total de Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto"); 

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

# Selecionando apenas as vendas de 2009 
df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head()

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="lucro x Mês")  
plt.xlabel("Mês")
plt.ylabel("lucro");

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="lucro x Marca")  # Lucro por marca
plt.xlabel("Marca")
plt.ylabel("lucro")
plt.xticks(rotation='horizontal');

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="lucro x Classe")  # Lucro por classe
plt.xlabel("Classe")
plt.ylabel("lucro")
plt.xticks(rotation='horizontal');

df["Tempo_envio"].describe()

# Grafico de boxplot
plt.boxplot(df["Tempo_envio"]); 

# histograma
plt.hist(df["Tempo_envio"]);

# Tempo mínimo de envio
df["Tempo_envio"].min()

# tempo max de envio
df["Tempo_envio"].max()

# identificando o Oulier
df[df["Tempo_envio"] == 20]

# salvando a análise
df.to_csv("df_vendas_novo.csv", index=False)



