# estrutura do for --- o que eu quero que execute varias vezes -- ou seja executa o bloco de código várias vezes, o numero de vezes que o for for executado depende do range que você passar
# for i in range(3):
#     print(i)


# for i in range(5):
#     print(i)    
#     print("Wagner Julio de Campos")


# pegar cada item da lista e executar o bloco de código 
# lista_produtos = ["iphone", "ipad", "airpod"]

# for produto in lista_produtos:            
#     print(produto)
    

# lista_precos = [1000, 2000, 3000]
# for preco in lista_precos:
#     imposto = preco * 1.2
#     # se o print estiver dentro do for, ele vai imprimir o valor do imposto para cada preço
#     # se o print estiver fora do for, ele vai imprimir o valor do imposto apenas uma vez, do ultimo item do for
#     print(f"preco {preco}, imposto {imposto}")

# nova regra do imposto
# se preco ate 1000, imposto é 10%
# se preco maior que  1000 o imposto eh de 15%     
print("----------------")

# lista_precos = [1000, 2000, 3000]
# for preco in lista_precos:
#     if preco <= 1000:
#         imposto = preco * 1.2
#     else:
#         imposto = preco * 1.30
#     # se o print estiver dentro do for, ele vai imprimir o valor do imposto para cada preço
#     # se o print estiver fora do for, ele vai imprimir o valor do imposto apenas uma vez, do ultimo item do for
#     print(f"preco {preco}, imposto {imposto}")

# print("----------------")

# total_imposto = 0
# print("total de imposto antes = ", total_imposto)

# for preco in lista_precos:
#     if preco <= 1000:
#         imposto = preco * 1.2
#     else:
#         imposto = preco * 1.30
#     # se o print estiver dentro do for, ele vai imprimir o valor do imposto para cada preço
#     # se o print estiver fora do for, ele vai imprimir o valor do imposto apenas uma vez, do ultimo item do for
#     print(f"preco {preco}, imposto {imposto}")
#     # total_imposto += imposto
#     print(f"total de imposto parcial = {total_imposto}")
#     total_imposto = total_imposto + imposto

# print("total de imposto depois = ", total_imposto)


print("----------------")


vendas_22 = {"jan": 1000, "fev": 2000, "mar": 3000, "abr": 4000, "mai": 5000, "jun": 6000, "jul": 7000, "ago": 8000, "set": 9000, "out": 10000, "nov": 11000, "dez": 12000}
vendas_23 = {"jan": 1500, "fev": 1800, "mar": 3500, "abr": 3800, "mai": 5500, "jun": 6500, "jul": 7500, "ago": 7400, "set": 9500, "out": 10500, "nov": 11500, "dez": 12500}

# exercicio 1 - saber quanto variou as vendas de 2022 para 2023

# for mes in vendas_22:
#     valor_22 = vendas_22[mes]
#     valor_23 = vendas_23[mes]
#     variacao_percentual = ((valor_23 - valor_22) / valor_22) * 100
#     print("variacao 1",variacao_percentual)
#     variacao_percentual = ((valor_23 / valor_22) - 1 ) 
#     print(f"variacao do mes {mes}: {variacao_percentual:.2%}")
#     print (mes, valor_22, valor_23)


# exercicio 2 - simular se a empresa tivesse pelo menos empatado com 2022 no meses em que ela vendeu menos que 2022, quanto teria sido o faturamento total de 2023
faturamento_total_simulado = 0
for mes in vendas_22:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    if vendas_23[mes] < vendas_22[mes]:
        #print(f"mes {mes} teve vendas menores que 2022, vendas 2022: {vendas_22[mes]}, vendas 2023: {vendas_23[mes]}")
        faturamento_total_simulado = faturamento_total_simulado + vendas_22[mes]
    else:
        faturamento_total_simulado = faturamento_total_simulado + vendas_23[mes]
print(faturamento_total_simulado)
