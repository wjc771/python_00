def calcular_imposto(preco, ir=0.275, csll=0.035, iss=0.05):
    """
    Calcula o imposto sobre o preço do produto.
    
    Parâmetros:
    preco (float): O preço do produto.
    ir (float): Alíquota do Imposto de Renda (default: 27.5%).
    csll (float): Alíquota da CSLL (default: 3.5%).
    iss (float): Alíquota do ISS (default: 5%).
    
    Retorna:
    float: O valor total do imposto calculado.
    """
    # imposto_ir = preco * ir
    # imposto_csll = preco * csll     
    # imposto_iss = preco * iss
    # return ir, csll, iss#, imposto_ir + imposto_csll + imposto_iss

#resposta = calcular_imposto(1000)

# ir, csll, iss = calcular_imposto(1000)
# #print(f"o valor do imposto é: {resposta}")
# print(ir, csll, iss, sep="\n")
    
# tamanho_tela = (1920, 1080)


vendas  = {
    "Andre": [1000, 2000, 3000],
    "Maria": [1500, 2500, 3500],
    "João": [1200, 2200, 3200],
    "Ana": [1300, 2300, 3300],
}

# Lista de vendedores,, pois eh a chave do dicionario
# for vendedor in vendas:
#     print(vendedor)

# Acessando os valores de cada vendedor
# for vendedor in vendas:
#     valores = vendas[vendedor]
#     print(f"Vendas de {vendedor}: {valores}")

# cada venda o vendedor ganha R$ 2 e 1% do valor total das vendas

def calcula_bonus(lista_vendas):
    bonus1 = len(lista_vendas) * 2  # R$ 2 por venda
    bonus2 = sum(lista_vendas) * 0.01  # 1% do valor total das vendas
    return bonus1 + bonus2

bonus_total = 0
for vendedor in vendas:
    lista_vendas_vendedor = vendas[vendedor]
    #print(f"Vendedor {vendedor}: {lista_vendas_vendedor}")
    bonus = calcula_bonus(lista_vendas_vendedor)
    bonus_total += bonus
    print(f"Vendedor: {vendedor}, Vendas: {lista_vendas_vendedor}, Bônus: R$ {bonus:.2f}") 
    print(f"Bônus total até agora: R$ {bonus_total:.2f}")

# for vendedor, lista_vendas_vendedor in vendas.items():
#     bonus = calcula_bonus(lista_vendas_vendedor)
#     print(f"Vendedor: {vendedor}, Vendas: {lista_vendas_vendedor}, Bônus: R$ {bonus:.2f}") 
#     bonus_total += bonus