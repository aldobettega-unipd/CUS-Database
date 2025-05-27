import csv
import random
from datetime import datetime, timedelta

# Carica tutti i nomi dei corsi da CORSO.csv
def carica_corsi(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row["nome"] for row in reader]

# Genera date casuali coerenti
def date_casuali():
    start = datetime.strptime("2023-01-01", "%Y-%m-%d")
    end = datetime.strptime("2024-12-31", "%Y-%m-%d")
    data_inizio = start + timedelta(days=random.randint(0, (end - start).days))
    durata_giorni = random.randint(30, 90)  # da 1 a 3 mesi
    data_fine = data_inizio + timedelta(days=durata_giorni)
    return data_inizio.date(), data_fine.date()

# Genera edizioni
def genera_edizioni(corsi):
    edizioni = []
    ed_id = 1
    for corso in corsi:
        n_edizioni = random.randint(5, 10)
        for _ in range(n_edizioni):
            data_inizio, data_fine = date_casuali()
            edizioni.append({
                "codice": f"ED{ed_id:03}",
                "data_inizio": data_inizio,
                "data_fine": data_fine,
                "n_partecipanti": random.randint(5, 20),
                "costo": round(random.uniform(50, 250), 2),
                "corso": corso
            })
            ed_id += 1
    return edizioni

# MAIN
corsi = carica_corsi("CORSO.csv")
edizioni = genera_edizioni(corsi)

with open("EDIZIONE_CORSO.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["codice", "data_inizio", "data_fine", "n_partecipanti", "costo", "corso"])
    writer.writeheader()
    for ed in edizioni:
        writer.writerow(ed)
