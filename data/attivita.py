import csv

# ⚙️ CONFIGURAZIONE SPORT E CATEGORIE
config_corsi = {
    "Calcio": {
        "categorie": [("Esordienti", 'U'), ("Allievi", 'M'), ("Allievi", 'F'), ("Juniores", 'M'), ("Juniores", 'F'), ("Prima squadra", 'M'), ("Prima squadra", 'F')],
    },
    "Basket": {
        "categorie": [("Under 12", "U"), ("Under 16", "F"), ("Under 16", "M"), ("Under 18", "F"), ("Under 18", "M"), ("Under 21", "F"), ("Under 21", "M"), ("Senior", "F"), ("Senior", "M")]
    },
    "Pallavolo": {
        "categorie": [("Under 12", "U"), ("Under 16", "F"), ("Under 16", "M"), ("Under 18", "F"), ("Under 18", "M"), ("Senior", "F"), ("Senior", "M")]
    },
    "Nuoto": {
        "categorie": [("Base", "U"), ("Agonisti", "U"), ("Master", "U")]
    },
    "Tennis": {
        "categorie": [("Under 12", "U"), ("Under 18", "M"), ("Under 18", "F"), ("Senior", "M"), ("Senior", "F")]
    },
    "Atletica": {
        "categorie": [("Esordienti", "U"), ("Cadetti", "U"), ("Professionisti", "U")]
    },
    "Yoga": {
        "categorie": [("Principianti", "U"), ("Avanzato", "U")]
    },
    "Arti Marziali": {
        "categorie": [("Cinture Bianche", "U"), ("Cinture Colorate", "U"), ("Cinture Nere", "U")]
    },
    "Scherma": {
        "categorie": [("Under 14", "U"), ("Under 16", "M"), ("Under 16", "F"), ("Senior", "M"), ("Senior", "F")]
    },
    "Arrampicata": {
        "categorie": [("Base", "U"), ("Avanzato", "U")]
    },
    "Rugby": {
        "categorie": [("Under 12", "U"), ("Under 16", "M"), ("Under 16", "F"), ("Under 21", "M"), ("Under 21", "F"), ("Prima squadra", "M"), ("Prima squadra", "F")]
    },
    "Boxe": {
        "categorie": [("Amatori", "M"), ("Agonisti", "M"), ("Agonisti", "F"), ("Pro", "M")]
    },
    "Ping Pong": {
        "categorie": [("Base", "U"), ("Elite", "U")]
    },
    "Pattinaggio": {
        "categorie": [("Under 15", "F"), ("Under 15", "U"), ("Under 18", "F"), ("Under 18", "U"), ("Agonistico", "F"), ("Agonistico", "U")]
    },
    "Hockey su prato": {
        "categorie": [("Under 14", "U"), ("Under 16", "M"), ("Under 16", "F"), ("Under 18", "M"), ("Under 18", "F"), ("Prima Squadra", "M"), ("Prima Squadra", "F")]
    },
    "Judo": {
        "categorie": [("Kyu", "U"), ("Dan", "M"), ("Dan", "F"), ("Cadetti", "M"), ("Cadetti", "F")]
    },
    "Ultimate Frisbee": {
        "categorie": [("Under 14", "U"), ("Under 18", "U"), ("Prima squadra", "M"), ("Prima squadra", "F")]
    },
    "Palestra": {
        "categorie": [("Palestra", "U")]
    },
    "Calisthenics": {
        "categorie": [("Calisthenics", "U")]
    }
}

sport_abbonabili = ["Palestra", "Ping Pong", "Boxe", "Tennis", "Arrampicata", "Nuoto"]
periodi = ["Mensile", "Trimestrale", "Annuale"]
accessi = [5, 10, 20, 30]

# 📦 Contenitori

attivita_rows = []
corso_rows = []
abbonamento_rows = []
periodico_rows = []
accessi_rows = []

# 🔁 Codice progressivo attività
codice_counter = 1


# Genera attività CORSI
for sport, info in config_corsi.items():

    categorie = info["categorie"]
    for categoria in categorie:
        codice = f"AT{codice_counter:03}"
        costo = round(50 + hash(codice) % 100, 2)
        attivita_rows.append({
            "codice_attivita": codice,
            "costo": costo,
            "sport": sport
        })
        codice_counter += 1
        if sport == "Palestra":
            continue
        corso_rows.append({
            "codice_corso": codice,
            "categoria": categoria[0],
            "sesso": categoria[1]
        })
        

# Genera abbonamenti: PERIODICI e LIMITATI
for sport in sport_abbonabili:
    for periodo in periodi:
        codice_per = f"AT{codice_counter:03}"
        costo = round(30 + periodi.index(periodo) * 20 + hash(codice_per) % 30, 2)
        attivita_rows.append({
            "codice_attivita": codice_per,
            "costo": costo,
            "sport": sport
        })
        abbonamento_rows.append({
            "codice_abbonamento": codice_per,
            "tipo": "periodico",
        })
        periodico_rows.append({
            "codice_abbonamento": codice_per,
            "periodo": periodo
        })
        codice_counter += 1

    for n_accessi in accessi:
        codice_acc = f"AT{codice_counter:03}"
        costo = round(5 * n_accessi + hash(codice_acc) % 10, 2)
        attivita_rows.append({
            "codice_attivita": codice_acc,
            "costo": costo,
            "sport": sport
        })
        abbonamento_rows.append({
            "codice_abbonamento": codice_acc,
            "tipo": "limitato",
        })
        accessi_rows.append({
            "codice_abbonamento": codice_acc,
            "n_accessi": n_accessi
        })
        codice_counter += 1

# 📝 Scrittura file
def scrivi_csv(nome_file, intestazioni, righe):
    with open(nome_file, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=intestazioni)
        writer.writeheader()
        writer.writerows(righe)

scrivi_csv("ATTIVITA.csv", ["codice_attivita", "costo", "sport"], attivita_rows)
scrivi_csv("CORSO.csv", ["codice_corso", "categoria", "sesso"], corso_rows)
scrivi_csv("ABBONAMENTO.csv", ["codice_abbonamento", "tipo"], abbonamento_rows)
scrivi_csv("PERIODICO.csv", ["codice_abbonamento", "periodo"], periodico_rows)
scrivi_csv("ACCESSI_LIMITATI.csv", ["codice_abbonamento", "n_accessi"], accessi_rows)
