import csv
import random
from collections import defaultdict
        
# 4. Carica COMPATIBILITA.csv (campo -> [sport compatibili])
campo_per_sport = defaultdict(list)
with open("COMPATIBILITA.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row["sport"] in ["Palestra", "Ping Pong", "Boxe", "Tennis", "Arrampicata", "Nuoto"]:
            campo_per_sport[row["sport"].strip()].append(row["campo"].strip())

sport_per_attivita = {}
with open("ATTIVITA.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        sport_per_attivita[row["codice_attivita"]] = row["sport"]
    
abbonamenti= []
with open('ABBONAMENTO.csv', newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        abbonamenti.append(row["codice_abbonamento"])
        
        
accessi =[]
for abb in abbonamenti:
    abb_sport = sport_per_attivita[abb]
    for campo in campo_per_sport[abb_sport]:
        accessi.append({
            "campo": campo,
            "abbonamento": abb,
        })


with open("ACCESSO.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["campo", "abbonamento"])
    writer.writeheader()
    for r in accessi:
        writer.writerow(r)

