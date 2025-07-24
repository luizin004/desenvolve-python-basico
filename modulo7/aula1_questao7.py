import random

def encrypt(lista):
    chave = random.randint(1, 10)
    criptografados = []
    for nome in lista:
        criptografado = ''.join(
            chr(((ord(c) - 33 + chave) % 94) + 33) for c in nome
        )
        criptografados.append(criptografado)
    return criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
criptografados, chave = encrypt(nomes)
print("Chave:", chave)
print("Criptografados:", criptografados)
