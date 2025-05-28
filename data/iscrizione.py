import csv
import random
from datetime import datetime, timedelta

def carica_persone(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice_fiscale"] for row in csv.DictReader(f)]

def carica_attivita(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice_attivita"] for row in csv.DictReader(f)]

def genera_data_iscrizione():
    oggi = datetime.now()
    giorni_fa = random.randint(0, 365 * 3)  # negli ultimi 3 anni
    data = oggi - timedelta(days=giorni_fa)
    return data.strftime("%Y-%m-%d")

def genera_iscrizioni(persone, attivita, max_iscrizioni=500):
    iscrizioni = set()
    tentativi = 0
    while len(iscrizioni) < max_iscrizioni and tentativi < max_iscrizioni * 10:
        persona = random.choice(persone)
        attivita_scelta = random.choice(attivita)
        chiave = (persona, attivita_scelta)
        if chiave not in iscrizioni:
            iscrizioni.add(chiave)
        tentativi += 1
    return [
        {
            "studente": studente,
            "codice_attivita": attivita,
            "data": genera_data_iscrizione()
        }
        for studente, attivita in iscrizioni
    ]

def main():
    persone = carica_persone("PERSONA.csv")
    attivita = carica_attivita("ATTIVITA.csv")
    iscrizioni = genera_iscrizioni(persone, attivita)

    with open("ISCRIZIONE.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["studente", "codice_attivita", "data"])
        writer.writeheader()
        for i in iscrizioni:
            writer.writerow(i)

if __name__ == "__main__":
    main()
