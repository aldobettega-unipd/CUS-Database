import csv
import random

# Carica ABBONAMENTO.csv dalla stessa cartella
with open("ABBONAMENTO.csv", newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    abbonamenti = list(reader)

# Genera dati per ACCESSI_LIMITATI
accessi_limitati = []
for abbonamento in abbonamenti:
    accessi_limitati.append({
        "abbonamento": abbonamento["codice"],
        "n_accessi": random.choice([5, 10, 15, 20, 30])
    })

# Scrivi ACCESSI_LIMITATI.csv nella stessa cartella
with open("ACCESSI_LIMITATI.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["abbonamento","n_accessi"])
    writer.writeheader()
    writer.writerows(accessi_limitati)
