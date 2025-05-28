import csv
import random
from datetime import datetime

def carica_persone(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice_fiscale"] for row in csv.DictReader(f)]

def carica_campi(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [
            {
                "codice": row["codice"],
                "prenotabile": row["prenotabile"].strip().lower() in ["true", "1", "yes", "y", "sì"],
                "via": row["via"],
                "citta": row["citta"]
            }
            for row in reader
        ]

def carica_lezioni(path):
    lezioni = {}
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            campo = row["campo"]
            ora = int(row["orario"].split(":")[0])
            inizio = ora
            fine = ora + 1
            if campo not in lezioni:
                lezioni[campo] = []
            lezioni[campo].append((inizio, fine))
    return lezioni

def carica_orari(path):
    orari = {}
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            chiave = (row["via"], row["citta"], row["giorno_settimana"].lower())
            apertura = int(row["apertura"].split(":")[0])
            chiusura = int(row["chiusura"].split(":")[0])
            orari[chiave] = (apertura, chiusura)
    return orari

def orari_sovrapposti(i1, f1, i2, f2):
    return max(i1, i2) < min(f1, f2)

def campo_libero(campo_id, ora_inizio, ora_fine, lezioni):
    if campo_id not in lezioni:
        return True
    for (li, lf) in lezioni[campo_id]:
        if orari_sovrapposti(ora_inizio, ora_fine, li, lf):
            return False
    return True

def genera_orari():
    ora_inizio = random.randint(8, 18)
    durata = random.randint(1, 3)
    ora_fine = min(ora_inizio + durata, 20)
    return ora_inizio, ora_fine

def genera_affitti(persone, campi, lezioni, orari_impianto, max_affitti=300):
    affitti = []
    tentativi = 0
    giorno = "lunedi"  # puoi parametrizzarlo
    max_tentativi = max_affitti * 10
    while len(affitti) < max_affitti and tentativi < max_tentativi:
        persona = random.choice(persone)
        campo = random.choice(campi)
        if not campo["prenotabile"]:
            tentativi += 1
            continue

        ora_inizio, ora_fine = genera_orari()
        codice_campo = campo["codice"]

        if not campo_libero(codice_campo, ora_inizio, ora_fine, lezioni):
            tentativi += 1
            continue

        chiave_orario = (campo["via"], campo["citta"], giorno)
        if chiave_orario in orari_impianto:
            apertura, chiusura = orari_impianto[chiave_orario]
            if not (apertura <= ora_inizio and ora_fine <= chiusura):
                tentativi += 1
                continue

        durata = ora_fine - ora_inizio
        tariffa = round(10 * durata + random.uniform(0, 5), 2)
        affitti.append({
            "persona": persona,
            "campo": codice_campo,
            "ora_inizio": f"{ora_inizio:02}:00",
            "ora_fine": f"{ora_fine:02}:00",
            "tariffa": tariffa
        })
        tentativi += 1
    return affitti

def main():
    persone = carica_persone("PERSONA.csv")
    campi = carica_campi("CAMPO.csv")
    lezioni = carica_lezioni("LEZIONE.csv")
    orari = carica_orari("ORARIO_IMPIANTO.csv")
    affitti = genera_affitti(persone, campi, lezioni, orari)

    with open("AFFITTO.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["persona", "campo", "ora_inizio", "ora_fine", "tariffa"])
        writer.writeheader()
        for a in affitti:
            writer.writerow(a)

if __name__ == "__main__":
    main()
