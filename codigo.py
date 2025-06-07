faturamento = 1200 # tipo: int -> inteiro
custo = 500 # tipo: -> float -> ponto flutuante
novas_vendas = 300
faturamento = faturamento+novas_vendas
taxa_imposto = 0.1 # decimal -> float
# inteiro
# float
# text
# boolean
teve_lucro = False
imposto = taxa_imposto * faturamento
mensagem = "o faturamento foi de"

print("imposto", imposto)
print("Faturamento ", faturamento)
print("Custo ", custo)
print("Lucro ", faturamento - custo - imposto)
print(mensagem, faturamento)

