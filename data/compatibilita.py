import csv
import random
from collections import defaultdict

# Definizione gruppi compatibili
gruppi = {
    "G1": ["Calcio", "Hockey su prato", "Atletica", "Ultimate Frisbee"],
    "G2": ["Basket", "Pallavolo"],
    "G3": ["Yoga", "Arti Marziali", "Scherma", "Boxe", "Judo"],
    "G4": ["Palestra", "Calisthenics"],
    "G5": ["Rugby", "Ultimate Frisbee"],
    "G6": ["Basket"],
    "G7": ["Pallavolo"],
    "G8": ["Nuoto"],
    "G9": ["Tennis"],
    "G10": ["Atletica"],
    "G11": ["Arrampicata"],
    "G12": ["Boxe"],
    "G13": ["Ping Pong"],
    "G14": ["Pattinaggio"],
    "G15": ["Calisthenics"]
}



# Carica CAMPO.csv (200 campi)
with open("CAMPO.csv", newline='', encoding="utf-8") as f:
    codici_campo = [row["codice"] for row in csv.DictReader(f)]

# Assegna i campi
random.shuffle(codici_campo)
N = len(codici_campo)
campi_gruppi = {
    "G1": codici_campo[:5],
    "G2": codici_campo[5:10],
    "G3": codici_campo[10:13],
    "G4": codici_campo[13:16],
    "G5": codici_campo[16:19],
    "G6": codici_campo[19:21],
    "G7": codici_campo[21:23],
    "G8": codici_campo[23:27],
    "G9": codici_campo[27:32],
    "G10": codici_campo[32:33],
    "G11": codici_campo[33:36],
    "G12": codici_campo[36:37],
    "G13": codici_campo[37:38],
    "G14": codici_campo[38:39],
    "G15": codici_campo[39:40], 
}

# Mappa finale: campo → lista di sport compatibili
compatibilita = defaultdict(list)

# Gruppi multipli
for gruppo, sport_list in gruppi.items():
    for campo in campi_gruppi[gruppo]:
        for sport in sport_list:
            compatibilita[campo].append(sport)


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
