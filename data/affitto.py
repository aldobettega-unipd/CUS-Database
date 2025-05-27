import csv
import random
from datetime import datetime, timedelta

def carica_persone(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice_fiscale"] for row in csv.DictReader(f)]

def carica_campi(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice"] for row in csv.DictReader(f)]

def carica_lezioni(path):
    lezioni = {}
    # struttura: lezioni[campo] = list of (inizio, fine) in ore interi
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            campo = row["campo"]
            # orario es. "10:00"
            ora = int(row["orario"].split(":")[0])
            # durata 1 ora fissa (se vuoi puoi adattare)
            inizio = ora
            fine = ora + 1
            if campo not in lezioni:
                lezioni[campo] = []
            lezioni[campo].append((inizio, fine))
    return lezioni

def orari_sovrapposti(i1, f1, i2, f2):
    # restituisce True se gli intervalli si sovrappongono
    return max(i1, i2) < min(f1, f2)

def campo_libero(campo, ora_inizio, ora_fine, lezioni):
    if campo not in lezioni:
        return True
    for (li, lf) in lezioni[campo]:
        if orari_sovrapposti(ora_inizio, ora_fine, li, lf):
            return False
    return True

def genera_orari():
    # Orari tra 8 e 20, durata 1-3 ore
    ora_inizio = random.randint(8, 18)
    durata = random.randint(1, 3)
    ora_fine = min(ora_inizio + durata, 20)
    return ora_inizio, ora_fine

def genera_affitti(persone, campi, lezioni, max_affitti=300):
    affitti = []
    tentativi = 0
    max_tentativi = max_affitti * 10  # per non entrare in loop infinito
    while len(affitti) < max_affitti and tentativi < max_tentativi:
        persona = random.choice(persone)
        campo = random.choice(campi)
        ora_inizio, ora_fine = genera_orari()
        if campo_libero(campo, ora_inizio, ora_fine, lezioni):
            durata = ora_fine - ora_inizio
            tariffa = round(10 * durata + random.uniform(0, 5), 2)
            affitti.append({
                "persona": persona,
                "campo": campo,
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
    affitti = genera_affitti(persone, campi, lezioni)

    with open("AFFITTO.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["persona", "campo", "ora_inizio", "ora_fine", "tariffa"])
        writer.writeheader()
        for a in affitti:
            writer.writerow(a)

if __name__ == "__main__":
    main()
