import csv
import random

# Categorie e sesso disponibili
categorie = ["Base", "Intermedio", "Avanzato"]
sessi = ["M", "F", "U"]  # M = Maschi, F = Femmine, U = Unisex

# Carica codici e nomi sport da SPORT.csv
def carica_sport(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [(row["codice"], row["nome"]) for row in reader]

# Genera corsi
def genera_corsi(sport_list):
    corsi = []
    for codice, nome_sport in sport_list:
        n = random.randint(2, 4)  # numero di corsi per sport
        for _ in range(n):
            categoria = random.choice(categorie)
            sesso = random.choice(sessi)
            nome_corso = f"Corso {categoria} di {nome_sport}"
            corsi.append({
                "sport": codice,
                "nome": nome_corso,
                "categoria": categoria,
                "sesso": sesso
            })
    return corsi

# MAIN
sport_list = carica_sport("SPORT.csv")
corsi = genera_corsi(sport_list)

with open("CORSO.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["sport", "nome", "categoria", "sesso"])
    writer.writeheader()
    for c in corsi:
        writer.writerow(c)
