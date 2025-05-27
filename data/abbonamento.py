import csv

# Nomi degli sport da cui generare abbonamenti
nomi_abbonamento = [
    "Palestra", "Ping Pong", "Arrampicata", "Nuoto", "Tennis"
]

# Associa codici simulati (SP001, SP002, ...)
sport_list = [(f"SP{i+1:03}", nome) for i, nome in enumerate(nomi_abbonamento)]

# Genera abbonamenti per ogni sport
def genera_abbonamenti(sport_list, tipi_abbonamento):
    abbonamenti = []
    for codice, nome_sport in sport_list:
        for tipo in tipi_abbonamento:
            abbonamenti.append({
                "sport": codice,
                "nome": f"{tipo} {nome_sport}"
            })
    return abbonamenti

# MAIN
tipi_abbonamento = ["Mensile", "Trimestrale", "Annuale"]
abbonamenti = genera_abbonamenti(sport_list, tipi_abbonamento)

with open("ABBONAMENTO.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["sport", "nome"])
    writer.writeheader()
    for a in abbonamenti:
        writer.writerow(a)
