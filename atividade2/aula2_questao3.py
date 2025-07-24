import string

def limpar_texto(texto):
    texto = texto.lower()
    return ''.join(c for c in texto if c.isalnum())

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break
    texto_limpo = limpar_texto(frase)
    if texto_limpo == texto_limpo[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
