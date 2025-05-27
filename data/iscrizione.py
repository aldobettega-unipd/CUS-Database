import csv
import random
from datetime import datetime, timedelta

def carica_studenti(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice_fiscale"] for row in csv.DictReader(f)]

def carica_sport(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice"] for row in csv.DictReader(f)]

def data_iscrizione():
    oggi = datetime.today()
    inizio = oggi - timedelta(days=365*2)  # ultimi 2 anni
    delta = oggi - inizio
    random_days = random.randint(0, delta.days)
    return (inizio + timedelta(days=random_days)).date()

def genera_iscrizioni(studenti, sport_list):
    iscrizioni = []
    for studente in studenti:
        # Ogni studente ha probabilità di 70% di avere almeno 1 iscrizione
        if random.random() < 0.7:
            n_sport = random.randint(1, 3)  # da 1 a 3 iscrizioni
            sport_scelti = random.sample(sport_list, n_sport)
            for sport in sport_scelti:
                iscrizioni.append({
                    "studente": studente,
                    "sport": sport,
                    "data": data_iscrizione(),
                    "costo": round(random.uniform(50, 300), 2)
                })
    return iscrizioni

def main():
    studenti = carica_studenti("PERSONA.csv")
    sport_list = carica_sport("SPORT.csv")

    iscrizioni = genera_iscrizioni(studenti, sport_list)

    with open("ISCRIZIONE.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["studente", "sport", "data", "costo"])
        writer.writeheader()
        for i in iscrizioni:
            writer.writerow(i)

if __name__ == "__main__":
    main()
