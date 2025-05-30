import csv
import random
from collections import defaultdict

# Definizione gruppi compatibili
gruppi = {
    "G1": ["Calcio", "Hockey su prato", "Atletica", "Ultimate Frisbee"], #7+7+3+4 = 21 
    "G2": ["Basket", "Pallavolo"], #17
    "G3": ["Yoga", "Arti Marziali", "Scherma", "Boxe", "Judo"], #19
    "G4": ["Palestra", "Calisthenics"], #2
    "G5": ["Rugby", "Ultimate Frisbee"], #11
    "G6": ["Basket"], #9
    "G7": ["Pallavolo"],#7
    "G8": ["Nuoto"],#3
    "G9": ["Tennis"],#5
    "G10": ["Atletica"],#3
    "G11": ["Arrampicata"],#2
    "G12": ["Boxe"],#4
    "G13": ["Ping Pong"],#2
    "G14": ["Pattinaggio"],#6
    "G15": ["Calisthenics"]#1
}



# Carica CAMPO.csv (200 campi)
with open("CAMPO.csv", newline='', encoding="utf-8") as f:
    codici_campo = [row["codice"] for row in csv.DictReader(f)]

# Assegna i campi
random.shuffle(codici_campo)
N = len(codici_campo)
campi_gruppi = {
    "G1": codici_campo[:10],
    "G2": codici_campo[10:17],
    "G3": codici_campo[17:25],
    "G4": codici_campo[25:28],
    "G5": codici_campo[28:34],
    "G6": codici_campo[34:36],
    "G7": codici_campo[36:38],
    "G8": codici_campo[38:41],
    "G9": codici_campo[41:43],
    "G10": codici_campo[43:45],
    "G11": codici_campo[45:46],
    "G12": codici_campo[46:48],
    "G13": codici_campo[48:50],
    "G14": codici_campo[50:53],
    "G15": codici_campo[53:55], 
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
