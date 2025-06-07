# Lista de vendas
# esta lista tem um unico item
# produtos = ["iphone, ipad, airpod"]
# produtos = ["iphone","ipad","airpod"]
# lista o primeiro item da lista
# nome = ["Wagner J Campos"]
# nome[0]

# primeiro elemento eh o 0, o ultimo elemento eh o -1, os numeros negativos iniciam da direita pra esquerda

vendas = [100, 30, 400, 250]

print(vendas[0])

      
# da pra somar o total de vendas 
sum_vendas = sum(vendas)
min_vendas = min(vendas)
max_vendas = max(vendas)

print(sum_vendas)
print(sum(vendas))
# numero de vendas, ou seja o nuero de itens dentro da lista
print(len(vendas))
print(sum_vendas, min_vendas, max_vendas)

print(vendas[1:])
# operador true or false - vaor está contido na lista
print(100 in vendas)
print(100 in vendas)

produtos = ["iphone", "ipad", "airpod"]
precos = [1000, 2000, 3000]

# editar o valor da lista

precos[0] = 1200
precos[0] = precos[0] *1.2
print(precos)
precos[0] = precos[0] + 5000
print(precos)

# adicionar um novo item na lista
precos.append(4000)
print(precos)   

# remover um item da lista
precos.remove(2000)
print(precos)
# remover o ultimo item da lista
precos.pop()    
print(precos)
# remover o primeiro item da lista  
precos.pop(0)
print(precos)

# adicionar um novo item na lista
precos.insert(0, 1000)
print(precos)

# contar quantas vezes um item aparece na lista
print(precos.count(1000))
# ordenar a lista
precos.sort()
print(precos)
# inverter a lista
precos.reverse()
print(precos)
# limpar a lista
precos.clear()
print(precos)
# copiar a lista
precos2 = precos.copy()
print(precos2)
# verificar se a lista está vazia
print(len(precos) == 0)
# verificar se a lista está vazia
print(not precos)
# verificar se a lista está vazia
print(precos == [])



