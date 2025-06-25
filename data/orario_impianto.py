import csv
import random


giorni_settimana = ["lunedi", "martedi", "mercoledi", "giovedi", "venerdi", "sabato", "domenica"]
apertura = ['07:00:00', '07:30:00', '08:00:00', '08:30:00', '09:00:00']
chiusura = ['16:30:00', '17:00:00', '17:30:00', '18:00:00', '19:00:00']

'''
orari_apertura = {
    "lunedi": "07:00:00",
    "martedi": "07:00:00",
    "mercoledi": "07:00:00",
    "giovedi": "07:00:00",
    "venerdi": "07:00:00",
    "sabato": "07:00:00",
    "domenica": "07:00:00"
}

orari_chiusura = {
    "lunedi": "22:00:00",
    "martedi": "22:00:00",
    "mercoledi": "22:00:00",
    "giovedi": "22:00:00",
    "venerdi": "22:00:00",
    "sabato": "13:00:00",
    "domenica": "13:00:00"
}
'''



impianti = []
with open("IMPIANTO_SPORTIVO.csv", newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        impianti.append((row["via"], row["comune"]))

righe = []
for via, citta in impianti:
    orario_apertura = random.choice(apertura)
    orario_chiusura = random.choice(chiusura) 
    for giorno in giorni_settimana: 
        if giorno in ["sabato", "domenica"]:
            orario_apertura = random.choice(apertura)
            orario_chiusura = random.choice(chiusura) 
        righe.append({
            "via": via,
            "comune": citta,
            "giorno_settimana": giorno,
            "apertura": orario_apertura,
            "chiusura": orario_chiusura
        })


with open("ORARIO_IMPIANTO.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["via", "comune", "giorno_settimana", "apertura", "chiusura"])
    writer.writeheader()
    for riga in righe:
        writer.writerow(riga)
