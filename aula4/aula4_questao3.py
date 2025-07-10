# Solicita o ano
ano = int(input("Digite um ano: "))

# Verifica as regras de ano bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")
