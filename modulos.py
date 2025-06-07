# # usar a biblioteca os para manipular arquivos e diretórios
# import os
# #listar aquivos dentro do diretório arquivos que fica no mesmo diretório do arquivo modulos.py
# arquivo_path = os.path.dirname(__file__)  # Obtém o diretório do arquivo atual
# arquivo_path = os.path.join(arquivo_path, "arquivos")  # Cria o caminho para o diretório "arquivos"
# print(arquivo_path)  # Exibe o caminho do diretório "arquivos"
# lista_arquivos = os.listdir(arquivo_path)  # Lista todos os arquivos e diretórios no diretório atual
# #print (lista_arquivos)  # Exibe a lista de arquivos e diretórios

# esta bibliioteca nao vem instalada por padrão, é necessário instalar com o comando pip install requests
import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)

dic_resposta = resposta.json()  # Converte a resposta JSON em um dicionário Python
print(dic_resposta)  # Exibe o dicionário resultante da conversão
print("---------")
print (dic_resposta["USDBRL"])  # Exibe o código da moeda USD

cotacao_dolar = dic_resposta["USDBRL"]   # Obtém a cotação do dólar
print ("Dollar: ", cotacao_dolar["bid"])  # Exibe a cotação do dólar formatada