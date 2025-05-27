import csv
import random
from datetime import datetime, timedelta

# Carica tutti i corsi (quindi solo attività didattiche)
with open("CORSO.csv", newline='', encoding="utf-8") as f:
    corsi = list(csv.DictReader(f))

# Carica i costi delle attività
costi_attivita = {}
with open("ATTIVITA.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        costi_attivita[row["codice_attivita"]] = float(row["costo"])

# Funzione per generare data d'inizio casuale
def genera_data_inizio():
    start = datetime.strptime("2023-01-01", "%Y-%m-%d")
    end = datetime.strptime("2025-12-31", "%Y-%m-%d")
    delta = random.randint(0, (end - start).days)
    return start + timedelta(days=delta)

# Generazione delle edizioni
edizioni = []
ed_id = 1

for corso in corsi:
    codice_attivita = corso["codice_attivita"]
    costo_base = costi_attivita.get(codice_attivita, 100.0)

    for _ in range(5):
        data_inizio = genera_data_inizio()
        durata = random.randint(30, 90)
        data_fine = data_inizio + timedelta(days=durata)

        edizioni.append({
            "codice_edizione": f"ED{ed_id:03}",
            "data_inizio": data_inizio.strftime("%Y-%m-%d"),
            "data_fine": data_fine.strftime("%Y-%m-%d"),
            "n_partecipanti": random.randint(5, 20),
            "costo": round(costo_base + random.uniform(-10, 20), 2),
            "codice_attivita": codice_attivita
        })

        ed_id += 1

# Scrittura EDIZIONE_CORSO.csv
with open("EDIZIONE_CORSO.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "codice_edizione", "data_inizio", "data_fine", "n_partecipanti", "costo", "codice_attivita"
    ])
    writer.writeheader()
    writer.writerows(edizioni)
