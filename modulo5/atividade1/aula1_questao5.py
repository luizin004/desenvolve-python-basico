import emoji # type: ignore

print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

frase = input("Digite uma frase e ela será emojizada:\n")
print("\nFrase emojizada:")
print(emoji.emojize(frase, language="alias"))