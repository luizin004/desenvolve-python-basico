# Lê o valor total em reais
valor = int(input())

# Lista com os valores das notas
notas = [100, 50, 20, 10, 5, 2, 1]

# Para cada nota, calcula quantas são necessárias e imprime
for nota in notas:
    qtd = valor // nota
    print(f"{qtd} nota(s) de R${nota},00")
    valor = valor % nota
