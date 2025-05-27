import csv
import random
from datetime import datetime, timedelta

def carica_persone(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice_fiscale"] for row in csv.DictReader(f)]

def carica_campi(path):
    campi = []
    prenotabili = {}
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            codice = row["codice"]
            campi.append(codice)
            prenotabili[codice] = row["prenotabile"].strip().lower() in ["true", "1", "t", "yes"]
    return campi, prenotabili

def carica_lezioni(path):
    lezioni = {}
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            campo = row["campo"]
            giorno = row["giorno"]
            ora = int(row["orario"].split(":")[0])
            inizio = datetime.strptime(f"{giorno} {ora:02}:00", "%Y-%m-%d %H:%M")
            fine = inizio + timedelta(hours=1)
            if campo not in lezioni:
                lezioni[campo] = []
            lezioni[campo].append((inizio, fine))
    return lezioni

def orari_sovrapposti(i1, f1, i2, f2):
    return max(i1, i2) < min(f1, f2)

def campo_libero(campo, inizio, fine, lezioni):
    if campo not in lezioni:
        return True
    for li, lf in lezioni[campo]:
        if orari_sovrapposti(inizio, fine, li, lf):
            return False
    return True

def genera_orari():
    # Genera data casuale nelle prossime 30 giornate
    giorno = datetime.today().date() + timedelta(days=random.randint(0, 30))
    ora_inizio = random.randint(8, 18)
    durata = random.randint(1, 3)
    ora_fine = min(ora_inizio + durata, 20)
    dt_inizio = datetime.combine(giorno, datetime.min.time()) + timedelta(hours=ora_inizio)
    dt_fine = datetime.combine(giorno, datetime.min.time()) + timedelta(hours=ora_fine)
    return dt_inizio, dt_fine

def genera_affitti(persone, campi, prenotabili, lezioni, max_affitti=300):
    affitti = []
    tentativi = 0
    max_tentativi = max_affitti * 10
    while len(affitti) < max_affitti and tentativi < max_tentativi:
        persona = random.choice(persone)
        campo = random.choice(campi)
        if not prenotabili.get(campo, False):
            tentativi += 1
            continue
        inizio, fine = genera_orari()
        if campo_libero(campo, inizio, fine, lezioni):
            durata_ore = (fine - inizio).seconds / 3600
            tariffa = round(10 * durata_ore + random.uniform(0, 5), 2)
            affitti.append({
                "persona": persona,
                "campo": campo,
                "ora_inizio": inizio.strftime("%Y-%m-%d %H:%M:%S"),
                "ora_fine": fine.strftime("%Y-%m-%d %H:%M:%S"),
                "tariffa": tariffa
            })
        tentativi += 1
    return affitti

def main():
    persone = carica_persone("PERSONA.csv")
    campi, prenotabili = carica_campi("CAMPO.csv")
    lezioni = carica_lezioni("LEZIONE.csv")
    affitti = genera_affitti(persone, campi, prenotabili, lezioni)

    with open("AFFITTO.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["persona", "campo", "ora_inizio", "ora_fine", "tariffa"])
        writer.writeheader()
        for a in affitti:
            writer.writerow(a)

if __name__ == "__main__":
    main()
