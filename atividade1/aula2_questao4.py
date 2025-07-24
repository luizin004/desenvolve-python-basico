# Recebe entradas do usuário
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {n1} elementos da lista 1:")
lista1 = [int(input()) for _ in range(n1)]

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {n2} elementos da lista 2:")
lista2 = [int(input()) for _ in range(n2)]

# Intercala listas
intercalada = []
for i in range(max(n1, n2)):
    if i < n1:
        intercalada.append(lista1[i])
    if i < n2:
        intercalada.append(lista2[i])

# Resultado
print("Lista intercalada:", intercalada)
