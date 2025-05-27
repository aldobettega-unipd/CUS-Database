import csv
import random

giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"]
fasce_orarie = [f"{h:02}:00" for h in range(8, 21)]  # 08:00 - 20:00

# Carica codici edizioni corso
def carica_edizioni(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice"] for row in csv.DictReader(f)]

# Carica codici campo
def carica_campi(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice"] for row in csv.DictReader(f)]

# Genera lezioni
def genera_lezioni(edizioni, campi):
    lezioni = []
    for edizione in edizioni:
        n_lezioni = random.randint(2, 4)
        giorni_usati = random.sample(giorni_settimana, k=n_lezioni)
        campo = random.choice(campi)
        for giorno in giorni_usati:
            orario = random.choice(fasce_orarie)
            lezioni.append({
                "orario": orario,
                "giorno": giorno,
                "campo": campo,
                "edizione_corso": edizione
            })
    return lezioni

# MAIN
edizioni = carica_edizioni("EDIZIONE_CORSO.csv")
campi = carica_campi("CAMPO.csv")

lezioni = genera_lezioni(edizioni, campi)

with open("LEZIONE.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["orario", "giorno", "campo", "edizione_corso"])
    writer.writeheader()
    for l in lezioni:
        writer.writerow(l)
