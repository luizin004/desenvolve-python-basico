from collections import Counter

# Listas fixas para o exemplo
lista1 = [10, 10, 28, 10, 29, 20, 30, 10, 29, 11]
lista2 = [11, 16, 26, 44, 11, 10, 20, 29, 10, 12]

# Interseção sem duplicatas
interseccao = sorted(list(set(lista1) & set(lista2)))

# Contagem dos elementos
cont_lista1 = Counter(lista1)
cont_lista2 = Counter(lista2)

# Impressões
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção:", interseccao)
print("\nContagem:")

for elemento in interseccao:
    print(f"{elemento}: (lista1={cont_lista1[elemento]}, lista2={cont_lista2[elemento]})")
