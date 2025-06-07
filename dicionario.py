# dictionaty of words coloca chave + valor , consjuto de elementos chave  e valor
precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]
dic_precos = {"celular": 1500, "camera": 1000, 
               "fone de ouvido": 800, "monitor": 2000}
print(dic_precos)
vendas_ano = {

    "jan": 1000,
    "fev": 2000,
    "mar": 3000,
    "abr": 4000
    
    }


# pegar item do dicionario
preco_celular = dic_precos["celular"]
print(preco_celular)    

# editar o valor do dicionario

dic_precos["celular"] = 2000
print(dic_precos)

# adicionar um novo item no dicionario
# nao existe valor duplicado as chaves são unicas
dic_precos["celular"] = 3000

print(dic_precos)

# remover um item do dicionario - pode ser usando del ou pop
#del dic_precos["celular"]   
dic_precos.pop("celular")
print(dic_precos)

# tamando do dicionario
print(len(dic_precos))  
# verificar se a chave existe no dicionario
print("celular" in dic_precos)
# verificar se a chave existe no dicionario 
print("celular" not in dic_precos)
# pegar todas as chaves do dicionario
print(dic_precos.keys())    
# pegar todos os valores do dicionario
print(dic_precos.values())
# pegar todos os itens do dicionario    
print(dic_precos.items())
# limpar o dicionario
dic_precos.clear()
print(dic_precos)
