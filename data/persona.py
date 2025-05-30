from faker import Faker
import csv
import random
'''
from codicefiscale import build
cf = build('Rossi', 'Mario', 'M', '1980-05-22','Roma')
print(cf)
'''
fake = Faker("it_IT")


def genera_studenti():
    sesso = random.choice(["M", "F"])
    if sesso == "M":
        nome = fake.first_name_male()
    else:
        nome = fake.first_name_female()
        
    eta = random.randint(12, 30)
    if eta >18:
        imm = random.choice(['true', 'false', 'true', 'true', 'true', 'true', 'true'])
    else:
        imm = 'false'
    return {
        "codice_fiscale": fake.ssn(),
        "nome": nome,
        "cognome": fake.last_name(),
        "eta": eta,
        "sesso": sesso,
        "immatricolato": imm
    }
    
def genera_gestori_istruttori():
    sesso = random.choice(["M", "F"])
    if sesso == "M":
        nome = fake.first_name_male()
    else:
        nome = fake.first_name_female()
        
    eta = random.randint(25, 50)
    
    if eta <32:
        imm = random.choice(['true', 'false', 'true', 'true', 'true', 'true', 'true'])
    else:
        imm = 'false'

    return {
        "codice_fiscale": fake.ssn(),
        "nome": nome,
        "cognome": fake.last_name(),
        "eta": eta,
        "sesso": sesso,
        "immatricolato":imm
    }
    
persone = []
        
with open("STUDENTE.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["codice_fiscale", "nome", "cognome", "eta", "sesso", "immatricolato"])
    writer.writeheader()
    for _ in range(600):
        studente = genera_studenti()
        writer.writerow(studente)
        persone.append(studente)
  
with open("ISTRUTTORE.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["codice_fiscale", "nome", "cognome", "eta", "sesso", "immatricolato"])
    writer.writeheader()
    for _ in range(80):
        istruttore =genera_gestori_istruttori()
        writer.writerow(istruttore)
        persone.append(istruttore)


with open("PERSONA.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["codice_fiscale", "nome", "cognome", "eta", "sesso", "immatricolato"])
    writer.writeheader()
    for p in persone:
        writer.writerow(p)

 
             

