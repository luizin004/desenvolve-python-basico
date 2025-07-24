livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", "2003", "368"],
    ["Torto Arado", "Itamar Vieira Junior", "2019", "264"],
    ["Dom Casmurro", "Machado de Assis", "1899", "256"],
    ["Grande Sertão: Veredas", "João Guimarães Rosa", "1956", "496"],
    ["Memórias Póstumas de Brás Cubas", "Machado de Assis", "1881", "224"],
    ["Vidas Secas", "Graciliano Ramos", "1938", "174"],
    ["Capitães da Areia", "Jorge Amado", "1937", "272"],
    ["A Hora da Estrela", "Clarice Lispector", "1977", "96"],
    ["Senhora", "José de Alencar", "1875", "320"],
    ["O Primo Basílio", "José Maria de Eça de Queirós", "1878", "352"]
]

with open("meus_livros.csv", "w", encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        linha = ",".join(livro)
        f.write(linha + "\n")
