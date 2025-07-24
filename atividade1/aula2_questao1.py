import random

# Gera lista com 20 números aleatórios entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# Imprime a lista ordenada (sem alterar a original)
print("Lista ordenada:", sorted(lista))

# Imprime a lista original
print("Lista original:", lista)

# Índice do maior valor
print("Índice do maior valor:", lista.index(max(lista)))

# Índice do menor valor
print("Índice do menor valor:", lista.index(min(lista)))
