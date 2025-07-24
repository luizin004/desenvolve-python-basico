import re

with open("frase.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# Remove tudo que não seja letra ou espaço
texto_limpo = re.sub(r'[^A-Za-zÀ-ÿ\s]', '', texto)

# Separa em palavras
palavras = texto_limpo.split()

with open("palavras.txt", "w", encoding="utf-8") as f:
    for p in palavras:
        f.write(p + "\n")

# Imprime o conteúdo do arquivo
with open("palavras.txt", "r", encoding="utf-8") as f:
    print(f.read())
