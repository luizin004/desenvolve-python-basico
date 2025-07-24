import os

frase = input("Digite uma frase: ")

with open("frase.txt", "w", encoding="utf-8") as f:
    f.write(frase)

caminho = os.path.abspath("frase.txt")
print(f"Frase salva em {caminho}")
