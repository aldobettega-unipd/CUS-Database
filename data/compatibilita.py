import csv
import random
from collections import defaultdict

# Definizione gruppi compatibili
gruppi = {
    "G1": ["Calcio", "Hockey su prato", "Atletica", "Ultimate Frisbee"],
    "G2": ["Basket", "Pallavolo"],
    "G3": ["Yoga", "Arti Marziali", "Scherma", "Boxe", "Judo"],
    "G4": ["Palestra", "Calisthenics"]
}

# Sport già coperti da gruppi
sport_gruppati = set(sum(gruppi.values(), []))

# Tutti gli sport da ATTIVITA.csv
sport_usati = set()
with open("ATTIVITA.csv", newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sport_usati.add(row["sport"])

# Sport con campo esclusivo
sport_singoli = sorted(sport_usati - sport_gruppati)

# Carica CAMPO.csv (200 campi)
with open("CAMPO.csv", newline='', encoding="utf-8") as f:
    codici_campo = [row["codice"] for row in csv.DictReader(f)]

# Assegna i campi
random.shuffle(codici_campo)
campi_gruppi = {
    "G1": codici_campo[:40],
    "G2": codici_campo[40:60],
    "G3": codici_campo[60:90],
    "G4": codici_campo[90:110],
}
campi_singoli = codici_campo[110:]

# Mappa finale: campo → lista di sport compatibili
compatibilita = defaultdict(list)

# Gruppi multipli
for gruppo, sport_list in gruppi.items():
    for campo in campi_gruppi[gruppo]:
        for sport in sport_list:
            compatibilita[campo].append(sport)

# Singoli: circa N campi per sport
n_campi_per_sport = len(campi_singoli) // len(sport_singoli)
i = 0
for sport in sport_singoli:
    for _ in range(n_campi_per_sport):
        compatibilita[campi_singoli[i]].append(sport)
        i += 1

# Scrivi COMPATIBILITA.csv
with open("COMPATIBILITA.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["campo", "sport"])
    writer.writeheader()
    for campo, sport_list in compatibilita.items():
        for sport in sport_list:
            writer.writerow({
                "campo": campo,
                "sport": sport
            })
