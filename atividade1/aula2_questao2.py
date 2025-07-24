# Gera número aleatório de elementos entre 5 e 20
import random


num_elementos = random.randint(5, 20)

# Gera lista de valores entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Imprime lista
print("Lista:", elementos)

# Soma dos elementos
soma = sum(elementos)
print("Soma:", soma)

# Média
media = soma / len(elementos)
print("Média:", media)
