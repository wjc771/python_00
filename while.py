# contador = 0

# while contador < 5:
#     print("contador:", contador)
#     contador += 1  # Incrementa o contador em 1 a cada iteração

produtos = ["iphone", "ipad", "airpod"]
while True:
    novo_produto = input("Digite o nome do novo produto (ou 'sair' para encerrar): ")
    if novo_produto.lower() == 'sair':
        break  # Encerra o loop se o usuário digitar 'sair'
    novo_produto = novo_produto.lower()
    if novo_produto in produtos:
        print("Produto já existe")
    else:
        print("Produto cadastrado com sucesso")
        produtos.append(novo_produto)
print("Produtos:", produtos)

        
