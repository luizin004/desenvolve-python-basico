from collections import Counter

frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ").lower()
anagramas = []

for palavra in frase.split():
    if Counter(palavra.lower()) == Counter(objetivo):
        anagramas.append(palavra)

print("Anagramas:", anagramas)
