# Solicita dados do participante
idade = int(input("Digite sua idade: "))
ja_jogou_3_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ") == "True"
vitorias = int(input("Quantos jogos já venceu? "))

# Verifica as condições para ingresso no clube
apto = (16 <= idade <= 18) and ja_jogou_3_jogos and vitorias >= 1
print("Apto para ingressar no clube de jogos de tabuleiro:", apto)
