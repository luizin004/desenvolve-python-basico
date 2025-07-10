# Solicita a distância e o peso do pacote
distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))

# Define o valor por kg de acordo com a distância
if distancia <= 100:
    valor_por_kg = 1.00
elif distancia <= 300:
    valor_por_kg = 1.50
else:
    valor_por_kg = 2.00

# Calcula o valor base do frete
frete = peso * valor_por_kg

# Adiciona taxa extra se o peso for superior a 10 kg
if peso > 10:
    frete += 10.00

# Imprime o valor do frete
print(f"Valor do frete: R${frete:.2f}")
