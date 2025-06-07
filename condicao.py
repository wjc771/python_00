# faturamento = 1000
# custo = 500
# lucro = faturamento - custo
# print("Faturamento:", faturamento)
# print("Custo:", custo)  
# print("Lucro:", lucro)

# # Verificar se o lucro é positivo ou negativo
# # usar sempre o tab para identar o código
# # tudo qu vc quiser que seja executado dentro do if deve estar identado
# if lucro < 0:
#     print("Lucro negativo")
#     print("Lucro:", lucro)
#     print()
# if lucro > 0:
#     print("Lucro positivo")
#     print("Lucro:", lucro)
#     print()
# # tudo que vc quiser que aconteca caso a consição não seja atendida
# # dois sinais de == quer dizer comparação
# else:
#     print("Lucro zero")
#     print("Lucro:", lucro)
#     print() 

# produtos = ["iphone", "ipad", "airpod"]
# novo_produto = input("Digite o nome do novo produto: ")
# novo_produto = novo_produto.lower()
# if novo_produto in produtos:
#     print("Produto já existe")
# else:
#     print("Produto cadastrado com sucesso")
#     produtos.append(novo_produto)

# print("Produtos:", produtos)

# CTRL + / para comentar o código


# acima de 1500 -> 500 de bonus
# acima de 1000 -> 500 de bonus
# acima de 500 -> 50 de bonus


# vendas = 20000

# if vendas > 1500:
#     bonus = 500
# elif vendas > 1000:
#     bonus = 500
# elif vendas > 500:
#     bonus = 50
# else:
#     bonus = 0
# print("Vendas:", vendas)
# print("Bonus:", bonus)


# if vendas > 5000:
#     if vendas > 1000:
#         if vendas > 1500:
#             bonus = 500
#         else:
#             bonus = 150
#     else:
#         bonus = 500
# else:
#     bonus = 0

# vendas = 17000
# vendas_empresa = 60000
# meta_empresa = 50000

# if vendas > 1500 and vendas_empresa > meta_empresa:
#     bonus = 500
# elif vendas > 10000 and vendas_empresa > meta_empresa:
#     bonus = 150
# elif vendas > 5000 and vendas_empresa > meta_empresa:
#     bonus = 50
# else:
#     bonus = 0


# eexeercicio desafio
# sistema de consuta de preços
# input do usuario e o sistema retorna o preço do produto, se o produto não existir o sistema retorna que o produto não existe
produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]

produto = input("Digite o nome do produto: ")
produto = produto.lower()
if produto in produtos:
    posicao = produtos.index(produto)
    preco = precos[posicao]
    print("Produto:", produto)
    print("Preço:", preco)
else:
    print("Produto não existe")
    print("Produto:", produto)

