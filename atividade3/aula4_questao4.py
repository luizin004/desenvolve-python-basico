import random

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

# Lê as palavras possíveis
with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip().lower() for linha in f if linha.strip()]

# Lê os estágios do enforcado, separados por linhas em branco
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Quebra em blocos pelo separador de duas linhas em branco ou múltiplas linhas em branco
estagios = [bloco.strip('\n') for bloco in conteudo.split('\n\n\n') if bloco]

palavra = random.choice(palavras)
letras_descobertas = ['_' for _ in palavra]
tentativas_erradas = 0
tentativas_max = len(estagios) - 1
letras_chutadas = set()

print(f"Palavra: {' '.join(letras_descobertas)}")

while tentativas_erradas < tentativas_max and '_' in letras_descobertas:
    chute = input("Digite uma letra: ").lower()
    if len(chute) != 1 or not chute.isalpha():
        print("Digite apenas uma letra válida.")
        continue
    if chute in letras_chutadas:
        print("Você já tentou essa letra.")
        continue
    letras_chutadas.add(chute)
    if chute in palavra:
        for i, letra in enumerate(palavra):
            if letra == chute:
                letras_descobertas[i] = chute
        print(f"Acertou! {' '.join(letras_descobertas)}")
    else:
        tentativas_erradas += 1
        print(f"Errou! Você tem {tentativas_max - tentativas_erradas} tentativas restantes.")
        imprime_enforcado(tentativas_erradas, estagios)
        print(f"Palavra: {' '.join(letras_descobertas)}")

if '_' not in letras_descobertas:
    print("Parabéns! Você ganhou!")
else:
    print(f"Você perdeu! A palavra era: {palavra}")
