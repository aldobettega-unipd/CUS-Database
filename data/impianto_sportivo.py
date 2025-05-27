from faker import Faker
import csv
import random

fake = Faker("it_IT")

# Carica le università dal CSV
def carica_universita(filename):
    universita = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            universita.append(row)  # ogni row ha 'nome' e 'citta'
    return universita

def genera_impianto(universita):
    # Scegliamo una università esistente come gestione
    scelta_uni = random.choice(universita)
    via = fake.street_name()
    citta = scelta_uni["citta"]  # coerente con l’università
    return {
        "via": via,
        "citta": citta,
        "n_campi": random.randint(1, 10),
        "contatto_segreteria": fake.phone_number(),
        "gestione": scelta_uni["nome"]
    }

# MAIN
universita = carica_universita("UNIVERSITA.csv")

with open("IMPIANTO_SPORTIVO.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["via", "citta", "n_campi", "contatto_segreteria", "gestione"])
    writer.writeheader()
    for _ in range(20):  # Genera 20 impianti sportivi
        writer.writerow(genera_impianto(universita))
