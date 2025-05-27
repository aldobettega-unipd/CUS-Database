import csv

# Giorni della settimana
giorni_settimana = [
    "Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"
]

# Orari fissi
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

# Legge impianti da IMPIANTO_SPORTIVO.csv
impianti = []
with open("IMPIANTO_SPORTIVO.csv", newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        impianti.append((row["via"], row["citta"]))

# Genera righe per ogni giorno e impianto
righe = []
for via, citta in impianti:
    for giorno in giorni_settimana:
        righe.append({
            "via": via,
            "citta": citta,
            "giorno_settimana": giorno,
            "apertura": orari_apertura[giorno],
            "chiusura": orari_chiusura[giorno]
        })

# Scrive il file CSV
with open("ORARIO_IMPIANTO.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["via", "citta", "giorno_settimana", "apertura", "chiusura"])
    writer.writeheader()
    for riga in righe:
        writer.writerow(riga)
