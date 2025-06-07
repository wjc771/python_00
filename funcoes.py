lista_precos = [1000, 2000, 3000]

#o que sao funcoes?
# Funções são blocos de código que realizam uma tarefa específica e podem ser reutilizados em diferentes partes do programa.
def calcular_imposto(preco):
    if preco <= 1000:
        return preco * 1.2
    else:
        return preco * 1.30
# Função para calcular o total de imposto
def calcular_total_imposto(lista_precos):
    total_imposto = 0
    for preco in lista_precos:
        imposto = calcular_imposto(preco)
        total_imposto += imposto
    return total_imposto
# Função para exibir os preços e impostos
def exibir_precos_e_impostos(lista_precos):
    for preco in lista_precos:
        imposto = calcular_imposto(preco)
        print(f"Preço: {preco}, Imposto: {imposto}")
# Função principal para executar o programa
def main():
    print("Lista de preços:", lista_precos)
    exibir_precos_e_impostos(lista_precos)
    total_imposto = calcular_total_imposto(lista_precos)
    print("Total de imposto:", total_imposto)   
# Chamada da função principal
# if __name__ == "__main__":
#     main()  
# Explicação das funções:
# 1. `calcular_imposto(preco)`: Esta função recebe um preço como argumento e retorna o imposto calculado com base na regra definida.    
# 2. `calcular_total_imposto(lista_precos)`: Esta função recebe uma lista de preços, calcula o imposto para cada preço usando a função `calcular_imposto`, e retorna o total de imposto.
# 3. `exibir_precos_e_impostos(lista_precos)`: Esta função exibe cada preço da lista junto com o imposto calculado.
# 4. `main()`: Esta é a função principal que executa o programa, chamando as outras funções para exibir os preços, calcular e exibir o total de imposto.
# 5. `if __name__ == "__main__":`: Esta linha garante que a função `main()` seja executada apenas quando o script for executado diretamente, e não quando importado como um módulo em outro script. 

# calculo = calcular_imposto(100)
# print("Cálculo do imposto para 100:", calculo)

def calcular_imposto(preco):
    if preco <= 1000:
        return preco * 1.2
    elif 1000 <= preco < 2000:
        return preco * 1.3
    elif 2000 <= preco < 3000:
        return preco * 1.4
    else:
        return preco * 1.5

meu_preco = int(input("Digite o preço do produto: "))
imposto = calcular_imposto(meu_preco)
print(f"O imposto calculado para o preco de 1500 é: {imposto}")
# Explicação do código:
# 1. A função `calcular_imposto(preco)` recebe um preço como argumento e calcula o imposto com base em diferentes faixas de preço.
# 2. A função retorna o imposto calculado de acordo com as regras definidas.

# positional argument
# 3. O usuário é solicitado a inserir o preço do produto.
# 4. O preço inserido é convertido para um inteiro e passado para a função `calcular_imposto`.
# 5. O imposto calculado é exibido na tela.

def calcular_imposto2(preco, aliquota1=1.1, aliquota2=1.2, aliquota3=1.3, aliquota4=1.4):
    """
    Calcula o imposto com base no preço e na alíquota fornecida.
    
    :param preco: Preço do produto
    :param aliquota: Alíquota do imposto (padrão é 1.2)
    :return: Valor do imposto calculado
    """
    if preco <= 1000:
        return preco * aliquota1
    elif 1000 < preco <= 2000:
        return preco * aliquota2
    elif 2000 < preco <= 3000:
        return preco * aliquota3
    else:
        return preco * aliquota4

meu_preco2 = int(input("Digite o preço do produto: "))
imposto = calcular_imposto2(meu_preco2)
print(f"O iposto calculado 2 eh: {imposto}")