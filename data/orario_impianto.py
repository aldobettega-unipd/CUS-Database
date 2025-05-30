import csv
import random


giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
apertura = ['07:00', '07:30', '08:00', '08:30', '09:00']
chiusura = ['16:30', '17:00', '17:30', '18:00', '19:00']

'''
orari_apertura = {
    "Lunedì": "07:00",
    "Martedì": "07:00",
    "Mercoledì": "07:00",
    "Giovedì": "07:00",
    "Venerdì": "07:00",
    "Sabato": "07:00",
    "Domenica": "07:00"
}

orari_chiusura = {
    "Lunedì": "22:00",
    "Martedì": "22:00",
    "Mercoledì": "22:00",
    "Giovedì": "22:00",
    "Venerdì": "22:00",
    "Sabato": "13:00",
    "Domenica": "13:00"
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
        if giorno in ["Sabato", "Domenica"]:
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
