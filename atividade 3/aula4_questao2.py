# Solicitar frase do usuário
frase = input("Digite uma frase: ")

# Lista de vogais (minúsculas, ordenadas)
vogais = sorted([c for c in frase if c.lower() in 'aeiou'])
print("Vogais:", vogais)

# Lista de consoantes (sem espaços)
consoantes = [c for c in frase if c.lower().isalpha() and c.lower() not in 'aeiou']
print("Consoantes:", consoantes)
