import csv
import random
from datetime import datetime
from collections import defaultdict

# Costanti
GIORNI_SETTIMANA = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"]
ORARI_DISPONIBILI = [f"{h:02}:00" for h in range(8, 21)]  # 08:00 - 20:00
MAX_LEZIONI = 10

# 1. Carica EDIZIONE_CORSO (solo 2024-2025)
with open("EDIZIONE_CORSO.csv", newline='', encoding="utf-8") as f:
    edizioni = [row for row in csv.DictReader(f)
                if datetime.strptime(row["data_inizio"], "%Y-%m-%d").year in [2024, 2025]]

# 2. Carica CORSO.csv per associare ogni edizione allo sport
corso_per_attivita = {}
with open("CORSO.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        corso_per_attivita[row["codice_attivita"]] = row

# 3. Carica ATTIVITA.csv per sapere lo sport del corso
sport_per_attivita = {}
with open("ATTIVITA.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        sport_per_attivita[row["codice_attivita"]] = row["sport"]

# 4. Carica COMPATIBILITA.csv (campo -> [sport compatibili])
sport_per_campo = defaultdict(set)
with open("COMPATIBILITA.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        sport_per_campo[row["campo"].strip()].add(row["sport"].strip())

# 5. Carica CAMPO.csv per lista completa dei campi
campi = set()
with open("CAMPO.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        campi.add(row["codice"].strip())

# 6. Inizializza struttura per occupazione campi
# struttura: campo -> giorno -> orari occupati
occupazione = defaultdict(lambda: defaultdict(set))

lezioni = []
for edizione in edizioni:
    codice_edizione = edizione["codice_edizione"]
    codice_attivita = edizione["codice_attivita"]
    sport = sport_per_attivita.get(codice_attivita)

    # Trova i campi compatibili con questo sport
    campi_validi = [c for c in campi if sport in sport_per_campo.get(c, set())]
    if not campi_validi:
        continue  # Nessun campo disponibile per questo sport

    # Scegli un campo random compatibile
    campo_scelto = random.choice(campi_validi)

    lezioni_assegnate = 0
    tentativi = 0
    while lezioni_assegnate < MAX_LEZIONI and tentativi < 100:
        giorno = random.choice(GIORNI_SETTIMANA)
        orario = random.choice(ORARI_DISPONIBILI)

        if orario not in occupazione[campo_scelto][giorno]:
            lezioni.append({
                "orario": orario,
                "giorno": giorno,
                "campo": campo_scelto,
                "codice_edizione": codice_edizione
            })
            occupazione[campo_scelto][giorno].add(orario)
            lezioni_assegnate += 1
        tentativi += 1

# 7. Scrivi LEZIONE.csv
with open("LEZIONE.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["orario", "giorno", "campo", "codice_edizione"])
    writer.writeheader()
    writer.writerows(lezioni)