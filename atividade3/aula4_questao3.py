import re

with open("estomago.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

# Primeiras 25 linhas
print("Primeiras 25 linhas:")
print("".join(linhas[:25]))

print(f"\nNúmero de linhas: {len(linhas)}")

# Linha com maior número de caracteres
linha_maior = max(linhas, key=lambda l: len(l.strip()))
print("\nLinha com maior número de caracteres:")
print(linha_maior.strip())

# Contar menções a "Nonato" e "Íria" (várias formas e evitando substrings erradas)
texto = "".join(linhas).lower()

# Função para contar ocorrências isoladas da palavra, ignorando substrings
def conta_palavra(texto, palavra):
    pattern = rf'\b{re.escape(palavra.lower())}\b'
    return len(re.findall(pattern, texto))

print(f'\nMenções a "Nonato": {conta_palavra(texto, "nonato")}')
print(f'Menções a "Íria": {conta_palavra(texto, "íria")}')
