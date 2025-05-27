import csv

# Elenco di sport realistici
nomi_sport = [
    "Calcio", "Basket", "Pallavolo", "Nuoto", "Tennis",
    "Atletica", "Yoga", "Arti Marziali", "Scherma", "Arrampicata",
    "Rugby", "Boxe", "Ping Pong", "Pattinaggio", "Atletica Leggera",
    "Hockey su prato", "Judo", "Rugby", "Ultimate Frisbee", "Palestra", "Calisthenics"
]

def genera_sport(nomi):
    sport = []
    for i, nome in enumerate(nomi, 1):
        sport.append({
            "codice": f"SP{i:03}",  # codice tipo SP001
            "nome": nome
        })
    return sport

# MAIN
sport = genera_sport(nomi_sport)

with open("SPORT.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["codice", "nome"])
    writer.writeheader()
    for s in sport:
        writer.writerow(s)
