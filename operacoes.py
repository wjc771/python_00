faturamento = 1000
custo = 700
novas_vendas= 300

faturamento = faturamento + novas_vendas # somar
imposto = faturamento * 0.01 # multiplicar
lucro = faturamento - custo - imposto # subtrair
print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento # dividir
print(margem_lucro)
print(imposto)
restituicao = imposto * 0.1
print("restituicao ", restituicao)
#mod eh o resto da divisao...sendo que o sinal utilizado eh o %, nao confundir com percent
# Numa divisao de 10 dividido por 3 o resultado eh 3 mas o resto eh 1
print(10 % 3)

# caso pratico -- tempo em anos
tempo_em_meses = 160
tempo_em_anos = tempo_em_meses / 12
# o int converte e pega somente a parte inteira
tempo_em_anos_int = int(tempo_em_meses / 12)
print(tempo_em_anos_int, "anos")
print(tempo_em_meses % 12, "meses")

numero= 123.97
print("numero arredondado: ",(round(numero)))
faturamento = 139_018_182 # edicao visual, o numero continua 139018182
print(faturamento)
