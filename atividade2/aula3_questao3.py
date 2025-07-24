# Parte 3: Lista aleatória e deleção do maior intervalo de negativos

import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("\nLista original:", lista)

# Encontrar maior sequência de números negativos
maior_inicio = maior_fim = 0
inicio = fim = 0

while fim < len(lista):
    if lista[fim] < 0:
        inicio = fim
        while fim < len(lista) and lista[fim] < 0:
            fim += 1
        if (fim - inicio) > (maior_fim - maior_inicio):
            maior_inicio, maior_fim = inicio, fim
    else:
        fim += 1

if maior_fim > maior_inicio:
    del lista[maior_inicio:maior_fim]

print("Lista editada:", lista)
