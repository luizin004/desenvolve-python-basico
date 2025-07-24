N = int(input("Digite a quantidade de pessoas: "))
soma_idades = 0

for i in range(N):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    soma_idades += idade

media = soma_idades / N
print(f"Média das idades: {media:.2f}")
