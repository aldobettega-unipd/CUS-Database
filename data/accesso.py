import csv
import random

def carica_campi(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [row["codice"] for row in csv.DictReader(f)]

def carica_abbonamenti(path):
    with open(path, newline='', encoding='utf-8') as f:
        # L'abbonamento è identificato da sport (chiave esterna)
        return [row["sport"] for row in csv.DictReader(f)]

def genera_accessi(campi, abbonamenti, max_accessi=300):
    accessi = []
    for _ in range(max_accessi):
        campo = random.choice(campi)
        abbonamento = random.choice(abbonamenti)
        accessi.append({
            "campo": campo,
            "abbonamento": abbonamento
        })
    return accessi

def main():
    campi = carica_campi("CAMPO.csv")
    abbonamenti = carica_abbonamenti("ABBONAMENTO.csv")
    accessi = genera_accessi(campi, abbonamenti)

    with open("ACCESSO.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["campo", "abbonamento"])
        writer.writeheader()
        for a in accessi:
            writer.writerow(a)

if __name__ == "__main__":
    main()
