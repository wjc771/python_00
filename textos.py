faturamento = 1000
custo = 700
lucro = faturamento - custo

# como fazer isso
# print("faturamento: valor, custo: valor, lucro: valor")
print("faturamento: ", faturamento, ", custo: ", custo, ", lucro:", lucro)

# usando o f no inicio do texto, indica que está formatando e que pode usar as variaveis entre {}
# Fica bem mais facil usar desta forma
print(f"faturamento: {faturamento}, custo: {custo}, lucro: {lucro}")

# como concatenar os textos usando +, só junta texto com texto
# como converter int para texto usando str
print("faturamento: " + str(faturamento) + ", custo: " + str(custo) + ", lucro: " + str(lucro))

email="EMAIL_false@gmail.com"

# converter para minusculo 
# toda funcao tem que abrir e fechar o parentesis
print(email.lower())

email="EMAIL_false@gmail.com"
#      01234567891011
# procurar um caracter, sendo que o indice começa no 0 ou -1 se nao encontrar
print(email.find("@"))

# pegar um pedaço do texto...neste caso o @, use o : antes ou depois pra pegar até onde quer o texto
caracter= email[11]
print(email[11])
print(caracter)
posicao = email.find("@")
print(posicao)

# pegar parte do texto ate o final ou até o inicio
servidor = email[11:]
print(servidor)
servidor = email[posicao:]
print(servidor)
# servidor sem @
servidor = email[posicao+1:]
print(servidor)
nome_email = email[:11]
print(nome_email)
nome_email = email[:posicao]
print(nome_email)

# pegar tamanho do texto
tamanho = len(email)
print(tamanho)

# trocar pedaco do  texto
email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

# transformar a primeira letra em maiusculo do texto
nome = "wagner julio de campos"
print(nome.capitalize()) # converte somente a primeira letra do texto todo para mausculo
print(nome.title()) # converte todas as primeiras letras de cada palavra

# especiais - formatacao numerica
faturamento = 100000000000000
# para formatar para moeda e colocar casas decimais :,.2f (: para indicar formatacao , para mlhares . para casas decimais e 2f para quantidade de casas decimais f significa float)
print(f"faturamento: R${faturamento:,.5f}, custo: USD{custo:.2f}, lucro: {lucro:,}")

# percentual
faturamento = 1000
margem = lucro / faturamento
print(f"Magem {margem:.1%}")
print(f"Magem {margem:.2%}")

# caracteres especiais - enter -> \n (barra ao contrario indica caracter especial)
print(f"faturamento: R${faturamento:,.5f}\n custo: USD{custo:.2f} \n lucro: {lucro:,}")

# exercicios
nome = "wagner julio de campos"
email = "wjcampos@autonomme.com"

#1. extraia o nome do servidor
posicao = email.find("@")
#servidor = email[find(@):]
servidor = email[posicao:]
servidor = email[email.find("@"):]
print(f"exercicio 1 - servidor e: {servidor}")

#3. construa uma mensagem: Usuário primeiro_nome cadastrado com sucesso com o email tal
posicao_primeiro_nome = nome.find(" ")
primeiro_nome = nome[:posicao_primeiro_nome]
print(f"Usuário {primeiro_nome} cadastrado com sucesso com o email {email}")

#4. construa uma mensagem: Enviamos um link de confirmacao para o email j***@gmail.com
posicao_letra_nome = nome.find("w")
letra_primeiro_nome = nome[:posicao_letra_nome+1]
print(f"Enviamos um link com sucesso com o email {email}")
print(f"Enviamos um link com sucesso com o email {letra_primeiro_nome}***{servidor}")
print(f"Enviamos um link com sucesso com o email {nome[:nome.find('a')]}***{servidor}")

posicao = email.find("@")
print(email)
