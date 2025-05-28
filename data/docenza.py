import csv
import random
from collections import defaultdict

def carica_corsi(path_corsi, path_attivita):
    # Mappa codice_corso → sport
    attivita_sport = {}
    with open(path_attivita, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            attivita_sport[row["codice_attivita"]] = row["sport"]

    corsi = []
    with open(path_corsi, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            codice = row["codice_attivita"]
            sport = attivita_sport.get(codice)
            if sport:
                corsi.append({"corso": codice, "sport": sport})
    return corsi

def carica_docenti(path_persone, sport_list):
    # Mappa sport → lista docenti
    # Per semplicità, assegna ogni docente a 1-2 sport casuali
    with open(path_persone, newline='', encoding='utf-8') as f:
        persone = [row["codice_fiscale"] for row in csv.DictReader(f)]

    sport_docenti = defaultdict(list)
    for persona in persone:
        sports = random.sample(sport_list, k=random.randint(1, 2))
        for s in sports:
            sport_docenti[s].append(persona)
    return sport_docenti

def genera_docenza(corsi, sport_docenti):
    docenze = set()
    corsi_per_sport = defaultdict(list)
    for corso in corsi:
        corsi_per_sport[corso["sport"]].append(corso["corso"])

    for sport, corsi_sport in corsi_per_sport.items():
        docenti_sport = sport_docenti.get(sport, [])
        if not docenti_sport:
            continue
        for corso in corsi_sport:
            docente = random.choice(docenti_sport)
            docenze.add((docente, corso))
            # Eventualmente assegna altri corsi allo stesso docente
            altri_corsi = random.sample(corsi_sport, k=random.randint(0, len(corsi_sport)//3))
            for ac in altri_corsi:
                docenze.add((docente, ac))
    return list(docenze)

def main():
    corsi = carica_corsi("CORSO.csv", "ATTIVITA.csv")
    sport_list = list({c["sport"] for c in corsi})
    sport_docenti = carica_docenti("PERSONA.csv", sport_list)
    docenze = genera_docenza(corsi, sport_docenti)

    with open("DOCENZA.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["istruttore", "corso"])
        writer.writeheader()
        for istruttore, corso in docenze:
            writer.writerow({"istruttore": istruttore, "corso": corso})

if __name__ == "__main__":
    main()
