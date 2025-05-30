from faker import Faker
import csv
import random

fake = Faker("it_IT")

impianti = ["Arena Vitalis", "Centro Sportivo Le Vette", "Stadio Aurora", "Palasport Zenith",  "Cittadella dello Sport"]
comuni = ["Padova","Padova","Padova","Padova","Padova", "Albigansego", "Vigodarzere"]
def genera_impianto(nome):
    via = fake.street_name()
    comune = random.choice(comuni) 
    return {
        "via": via,
        "comune": comune,
        "nome": nome,
        "contatto_segreteria": fake.phone_number()
    }


with open("IMPIANTO_SPORTIVO.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["via", "comune", "nome", "contatto_segreteria"])
    writer.writeheader()
    for nome in impianti:
        writer.writerow(genera_impianto(nome))
        

