import csv
import random
from collections import defaultdict
from datetime import datetime, timedelta
        
studenti = []
with open("STUDENTE.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        studenti.append([row['codice_fiscale'], row["immatricolato"]])
        
def data_casuale() -> str:
    data_inizio = datetime(2021, 1, 1)
    data_fine = datetime(2025, 1, 1)
    delta = (data_fine - data_inizio).days
    giorni_casuali = random.randint(0, delta)
    data = data_inizio + timedelta(days=giorni_casuali)
    return data.strftime("%Y-%m-%d")
    
    
tessere = []
for stud in studenti:
    if stud[1] == 'true':
        costo = 0
    else:
        costo = 15
    
    tessere.append({
        "persona": stud[0],
        "data": data_casuale(),
        "costo": costo
    })


with open("TESSERA.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["persona", "data", "costo"])
    writer.writeheader()
    for r in tessere:
        writer.writerow(r)

