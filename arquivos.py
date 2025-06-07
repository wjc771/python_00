# trabalhar com arquivos
# abrir com a função open()
# se nao usar o "with" statement, é necessário fechar o arquivo manualmente com arquivo.close()

# arquivo = open("produtos.txt", "r")  # Abre o arquivo em modo de leitura (read)

#     # faze o que quiser no arquivo

# arquivo.close()  # Fecha o arquivo manualmente


with open("vendas.txt", "r") as arquivo:  # Abre o arquivo em modo de leitura (read)
    #conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
    conteudo = arquivo.readlines()  # Lê todo o conteúdo do arquivo
print(conteudo)  # Exibe o conteúdo lido
print(conteudo[1])  # Exibe o conteúdo lido

vendas_totais = 0  # Inicializa a variável para armazenar o total de vendas
for item in conteudo:
    item = item.replace("\n", "")  # Remove a quebra de linha
    item = item.strip()  # Remove espaços em branco no início e no final da string
    #print(item)  # Exibe cada item sem a quebra de linha
    resultado = item.split(",")  # Divide o item em uma lista usando a vírgula como separador
    #print(resultado)  # Exibe a lista resultante da divisão
    valor = (resultado[1])  # Converte o segundo item da lista para float
    valor = float(valor)  # Converte o valor para float
    vendas_totais += valor  # Soma o valor ao total de vendas
    print(valor)  # Exibe o valor convertido
print(f"Vendas totais: {vendas_totais:.2f}")  # Exibe o total de vendas formatado com duas casas decimais