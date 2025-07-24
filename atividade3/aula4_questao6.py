import csv

anos_alvo = list(range(2012, 2023))
mais_tocadas = {ano: ["", "", ano, 0] for ano in anos_alvo}  # track_name, artist(s)_name, year, streams

def linha_valida(row):
    # Ignorar linhas onde algum campo possui aspas que indicam múltiplos artistas (complexo)
    # Linha inválida se track_name ou artist(s)_name começam e terminam com aspas
    return not (row[0].startswith('"') and row[0].endswith('"')) and not (row[1].startswith('"') and row[1].endswith('"'))

with open("spotify-2023.csv", "r", encoding="latin-1") as f:
    leitor = csv.reader(f)
    next(leitor)  # pular cabeçalho
    for row in leitor:
        if len(row) < 9:
            continue
        if not linha_valida(row):
            continue

        try:
            track_name = row[0]
            artist_name = row[1]
            released_year = int(row[3])
            streams = int(row[8])
        except ValueError:
            continue

        if released_year in anos_alvo:
            if streams > mais_tocadas[released_year][3]:
                mais_tocadas[released_year] = [track_name, artist_name, released_year, streams]

resultado = [mais_tocadas[ano] for ano in anos_alvo]
print(resultado)
