import csv
import random

def carica_campi(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice"] for row in csv.DictReader(f)]

def carica_abbonamenti(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice_attivita"] for row in csv.DictReader(f)]

def genera_accessi(campi, abbonamenti, max_accessi=500):
    accessi = set()
    tentativi = 0
    while len(accessi) < max_accessi and tentativi < max_accessi * 10:
        campo = random.choice(campi)
        abbonamento = random.choice(abbonamenti)
        chiave = (campo, abbonamento)
        if chiave not in accessi:
            accessi.add(chiave)
        tentativi += 1
    return [{"campo": c, "abbonamento": a} for c, a in accessi]

def main():
    campi = carica_campi("CAMPO.csv")
    abbonamenti = carica_abbonamenti("ABBONAMENTO.csv")
    accessi = genera_accessi(campi, abbonamenti)

    with open("ACCESSO.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["campo", "abbonamento"])
        writer.writeheader()
        for r in accessi:
            writer.writerow(r)

if __name__ == "__main__":
    main()
