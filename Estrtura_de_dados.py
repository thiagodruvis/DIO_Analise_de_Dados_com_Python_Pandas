# Criando uma lista chamda animais 
animais = [1,2,3]
animais

animais = ["cachorro", "gato", 12345, 6.5]
animais 

# Imprimindo o primeiro elemento de lista 
animais[0]

# Imprimindo o 4 elemento da lista 
animais[3]

# Sustituindo o primeiro elemento da lista
animais[0] = "papagaio"

animais 

# removendo gato da lista
animais.remove("gato")

animais 

len(animais)

"gato" in animais

lista = [500, 30, 300, 80, 10]

max(lista)

min(lista)

animais.append("leão")

animais

animais.extend(["cobra", 6])

animais

animais.count("cahorro")

lista.sort()

lista

**Tuplas**

# As Tuplas usam parênteses como sintaxe 
tp = ("Banana", "Maçã", 10, 50)

# Retornando o primeiro elemento 
tp[0]

# diferente das listas as tuplas são imutáveis, o que quer dizer que não podemos alterar seus elementos 
tp[0] = "Laranja"

tp.count("Maçã")

tp[0:2]

**Dicionários**

# Para criar um dicionário utilizamos as {}
dc = {"Maçã":20, "Banana":10, "Laranja":15, "Uva":5} # dicionários trabalham com o conceito de chave a valor

dc

# Acessando o valor de um dicionário através da chave
dc["Maçã"]

# Atualizando o valor da Maçã 
dc["Maçã"] = 25

dc


# retornando todas as chaves do diconários 
dc.keys()

dc.values()

# verficando se ja existe uma cha no dicionário e caso não exista inserir
dc.setdefault("Limão", 22)

dc

