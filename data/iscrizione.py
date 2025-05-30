import csv
import random
from collections import defaultdict
from datetime import datetime, timedelta

def data_casuale_attorno(data_centrale: datetime) -> str:
    data_inizio = data_centrale - timedelta(days=30)
    data_fine = data_centrale + timedelta(days=30)
    delta = (data_fine - data_inizio).days
    giorni_casuali = random.randint(0, delta)
    data = data_inizio + timedelta(days=giorni_casuali)
    return data.strftime("%Y-%m-%d")


# Mappa categorie -> range età
categorie_eta = {
    "Under 12": (6, 12),
    "Under 14": (12, 14),
    "Under 16": (14, 16),
    "Under 18": (16, 18),
    "Under 21": (17, 21),
    "Juniores": (14, 17),
    "Allievi": (16, 18),
    "Senior": (18, 40),
    "Professionisti": (20, 50),
    "Cadetti": (15, 18),
    "Esordienti": (8, 12),
    "Base": (10, 60),
    "Agonisti": (14, 35),
    "Master": (30, 60),
    "Kyu": (10, 15),
    "Dan": (16, 60),
    "Principiante":(6, 20),
    "Avanzato":(15,40),
    "Cinture Bianche": (8, 14),
    "Cinture Colorate": (12, 16),
    "Cinture Nere": (16, 50),
    "Prima squadra": (18, 40),
    "Promesse": (18, 22),
    "Elite": (20, 35),
    "Amatori": (14, 99),
    "Pro": (18, 35),
    "default": (10, 99)
}

# 1. Carica PERSONA.csv
with open("STUDENTE.csv", newline='', encoding="utf-8") as f:
    studenti = list(csv.DictReader(f))

# 2. Carica CORSO.csv
corsi = {}
with open("CORSO.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        corsi[row["codice_corso"]] = row

# 3. Carica ATTIVITA.csv (per sport)
sport_per_attivita = {}
with open("ATTIVITA.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        sport_per_attivita[row["codice_attivita"]] = row["sport"]

# 5. Genera ISCRIZIONI
iscrizioni = []
for codice_attivita, corso in corsi.items():

    categoria = corso["categoria"]
    sesso_corso = corso["sesso"]

    eta_min, eta_max = categorie_eta.get(categoria, categorie_eta["default"])

    candidati = []
    for persona in studenti:
        eta = int(persona["eta"])
        sesso = persona["sesso"]

        if eta_min <= eta <= eta_max:
            if sesso_corso == "U" or sesso_corso == sesso:
                candidati.append(persona["codice_fiscale"])

    n_max = random.randint(13, 20)
    iscritti = random.sample(candidati, min(len(candidati), n_max))

    inizio_corso  = datetime(2024, 9, 15)
    data = data_casuale_attorno(inizio_corso)
    for cf in iscritti:
        iscrizioni.append({
            "studente": cf,
            "codice_attivita": codice_attivita,
            "data": data
        })

# 6. Scrivi ISCRIZIONE.csv
with open("ISCRIZIONE.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["studente", "codice_attivita", "data"])
    writer.writeheader()
    writer.writerows(iscrizioni)
