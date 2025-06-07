# exercicios
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

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
posicao_letra_nome = nome.find("g")
letra_primeiro_nome = nome[:posicao_letra_nome+1]
print(f"Enviamos um link com sucesso com o email {email}")
print(f"Enviamos um link com sucesso com o email {letra_primeiro_nome}***{servidor}")
print(f"Enviamos um link com sucesso com o email {nome[:nome.find('a')]}***{servidor}")