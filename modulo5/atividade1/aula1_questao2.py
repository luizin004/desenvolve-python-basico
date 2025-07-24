import random
import math

n = int(input("Digite a quantidade de números a serem gerados: "))
soma = 0

for _ in range(n):
    numero = random.randint(0, 100)
    soma += numero

raiz = math.sqrt(soma)
print(f"A raiz quadrada da soma dos valores é: {raiz:.2f}")