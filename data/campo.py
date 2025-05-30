from faker import Faker
import csv
import random

fake = Faker("it_IT")

# Carica i responsabili (codici fiscali) dalla tabella PERSONA
        
def carica_responsabili(file_persona):
    with open(file_persona, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row['codice_fiscale'] for row in reader]

# Carica le coppie (via, citta) dagli impianti sportivi
def carica_impianti(file_impianti):
    with open(file_impianti, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [(row["via"], row["comune"]) for row in reader]

def genera_campo(index, responsabili, impianti):
    via, comune = random.choice(impianti)
    responsabile = random.choice(responsabili)
    responsabili.remove(responsabile)
    return {
        "codice": f"CAMPO{index:03}",
        "prenotabile": random.choice(["true", "false"]),
        "responsabile": responsabile,
        "via": via,
        "comune": comune
    }

# MAIN
responsabili = carica_responsabili("ISTRUTTORE.csv")
impianti = carica_impianti("IMPIANTO_SPORTIVO.csv")

with open("CAMPO.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["codice", "prenotabile", "responsabile", "via", "comune"])
    writer.writeheader()
    for i in range(40): 
        writer.writerow(genera_campo(i+1, responsabili, impianti))
