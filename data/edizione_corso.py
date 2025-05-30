import csv
import random
from datetime import datetime, timedelta

# Carica tutti i corsi (quindi solo attività didattiche)
with open("CORSO.csv", newline='', encoding="utf-8") as f:
    corsi = list(csv.DictReader(f))



# Funzione per generare data d'inizio casuale
def genera_data_inizio(ed_id):
    mese = random.choice([9, 10, 11, 12, 1])
    anno = 2025-ed_id if mese != 1 else 2026-ed_id
    start = datetime.strptime(f"{anno}-{mese:02}", "%Y-%m")
    delta = random.randint(5, 9)
    end_mese = (delta+mese)%13
    end_anno = anno+1 if delta+mese>12 else anno
    end = datetime.strptime(f"{end_anno}-{end_mese}", "%Y-%m")
    return start, end

# Generazione delle edizioni
edizioni = []

codice = 1
for ed_id in range(5, 0, -1):

    for corso in corsi:
    
        codice_attivita = corso["codice_corso"]
        data_inizio, data_fine = genera_data_inizio(ed_id)
        edizioni.append({
            "codice_edizione": f'ED{data_inizio.strftime("%Y"):04}{codice:03}',
            "data_inizio": data_inizio.strftime("%Y-%m"),
            "data_fine": data_fine.strftime("%Y-%m"),
            "n_partecipanti": random.randint(10, 20),
            "codice_attivita": codice_attivita
        })
        codice+=1

        

# Scrittura EDIZIONE_CORSO.csv
with open("EDIZIONE_CORSO.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "codice_edizione", "data_inizio", "data_fine", "n_partecipanti", "codice_attivita"
    ])
    writer.writeheader()
    writer.writerows(edizioni)
