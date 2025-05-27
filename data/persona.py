from faker import Faker
import csv
import random

fake = Faker("it_IT")

universita = ["Università di Padova", "La Sapienza", "Politecnico di Milano", "Università di Trento", "Politecnico di Torino"]

def genera_persona():
    sesso = random.choice(["M", "F"])
    if sesso == "M":
        nome = fake.first_name_male()
    else:
        nome = fake.first_name_female()
    return {
        "codice_fiscale": fake.ssn(),
        "nome": nome,
        "cognome": fake.last_name(),
        "eta": random.randint(18, 35),
        "sesso": sesso,
        "universita": random.choice(universita)
    }

with open("PERSONA.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["codice_fiscale", "nome", "cognome", "eta", "sesso", "universita"])
    writer.writeheader()
    for _ in range(100):
        writer.writerow(genera_persona())
