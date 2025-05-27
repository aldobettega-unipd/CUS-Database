import csv

# ⚙️ CONFIGURAZIONE SPORT E CATEGORIE
config_corsi = {
    "Calcio": {
        "categorie": ["Juniores", "Allievi", "Prima squadra"],
        "sessi": ["M", "U"]
    },
    "Basket": {
        "categorie": ["Under 18", "Under 21", "Senior"],
        "sessi": ["F", "M"]
    },
    "Pallavolo": {
        "categorie": ["Under 16", "Under 18", "Senior"],
        "sessi": ["F", "M", "U"]
    },
    "Nuoto": {
        "categorie": ["Base", "Agonisti", "Master"],
        "sessi": ["U"]
    },
    "Tennis": {
        "categorie": ["Under 12", "Under 18", "Senior"],
        "sessi": ["M", "F"]
    },
    "Atletica": {
        "categorie": ["Esordienti", "Cadetti", "Professionisti"],
        "sessi": ["U"]
    },
    "Yoga": {
        "categorie": ["Principianti", "Intermedio", "Avanzato"],
        "sessi": ["U"]
    },
    "Arti Marziali": {
        "categorie": ["Cinture Bianche", "Cinture Colorate", "Cinture Nere"],
        "sessi": ["M", "F", "U"]
    },
    "Scherma": {
        "categorie": ["Under 14", "Under 17", "Senior"],
        "sessi": ["M", "F"]
    },
    "Arrampicata": {
        "categorie": ["Indoor Base", "Indoor Avanzato", "Outdoor Tecnico"],
        "sessi": ["U"]
    },
    "Rugby": {
        "categorie": ["Under 16", "Under 20", "Prima squadra"],
        "sessi": ["M", "F"]
    },
    "Boxe": {
        "categorie": ["Amatori", "Agonisti", "Pro"],
        "sessi": ["M"]
    },
    "Ping Pong": {
        "categorie": ["Base", "Club", "Torneo"],
        "sessi": ["U"]
    },
    "Pattinaggio": {
        "categorie": ["Artistico", "Velocità", "Agonistico"],
        "sessi": ["F", "U"]
    },
    "Atletica Leggera": {
        "categorie": ["Giovanile", "Promesse", "Elite"],
        "sessi": ["M", "F", "U"]
    },
    "Hockey su prato": {
        "categorie": ["Under 14", "Under 16", "Under 18", "Prima Squadra"],
        "sessi": ["M", "F"]
    },
    "Judo": {
        "categorie": ["Kyu", "Dan", "Cadetti"],
        "sessi": ["M", "F", "U"]
    },
    "Ultimate Frisbee": {
        "categorie": ["Recreational", "Competitivo", "Elite"],
        "sessi": ["U"]
    },
    "Palestra": {
        "categorie": ["Sala Pesi", "Cardio", "Circuito Funzionale"],
        "sessi": ["U"]
    },
    "Calisthenics": {
        "categorie": ["Base", "Intermedio", "Avanzato"],
        "sessi": ["U"]
    }
}

sport_abbonabili = ["Palestra", "Ping Pong", "Boxe", "Tennis"]
periodi = ["Mensile", "Trimestrale", "Annuale"]
accessi = [1, 2, 5, 10, 20]

# 📦 Contenitori
sport_rows = []
attivita_rows = []
corso_rows = []
abbonamento_rows = []
periodico_rows = []
accessi_rows = []

# 🔁 Codice progressivo attività
codice_counter = 1

# Aggiungi tutti gli sport alla tabella SPORT
for nome_sport in config_corsi.keys():
    sport_rows.append({"nome_sport": nome_sport})

# Genera attività CORSI
for sport, info in config_corsi.items():
    categorie = info["categorie"]
    sessi = info["sessi"]
    for categoria in categorie:
        for sesso in sessi:
            codice = f"AT{codice_counter:03}"
            costo = round(50 + hash(codice) % 100, 2)
            attivita_rows.append({
                "codice_attivita": codice,
                "costo": costo,
                "sport": sport
            })
            corso_rows.append({
                "codice_attivita": codice,
                "categoria": categoria,
                "sesso": sesso
            })
            codice_counter += 1

# Genera abbonamenti: PERIODICI e LIMITATI
for sport in sport_abbonabili:
    for periodo in periodi:
        codice = f"AT{codice_counter:03}"
        costo = round(30 + periodi.index(periodo) * 20 + hash(codice) % 30, 2)
        attivita_rows.append({
            "codice_attivita": codice,
            "costo": costo,
            "sport": sport
        })
        abbonamento_rows.append({
            "codice_attivita": codice,
            "tipo": "periodico",
            "sport": sport
        })
        periodico_rows.append({
            "codice_attivita": codice,
            "periodo": periodo
        })
        codice_counter += 1

    for n_accessi in accessi:
        codice = f"AT{codice_counter:03}"
        costo = round(5 * n_accessi + hash(codice) % 10, 2)
        attivita_rows.append({
            "codice_attivita": codice,
            "costo": costo,
            "sport": sport
        })
        abbonamento_rows.append({
            "codice_attivita": codice,
            "tipo": "limitato",
            "sport": sport
        })
        accessi_rows.append({
            "codice_attivita": codice,
            "n_accessi": n_accessi
        })
        codice_counter += 1

# 📝 Scrittura file
def scrivi_csv(nome_file, intestazioni, righe):
    with open(nome_file, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=intestazioni)
        writer.writeheader()
        writer.writerows(righe)

scrivi_csv("SPORT.csv", ["nome_sport"], sport_rows)
scrivi_csv("ATTIVITA.csv", ["codice_attivita", "costo", "sport"], attivita_rows)
scrivi_csv("CORSO.csv", ["codice_attivita", "categoria", "sesso"], corso_rows)
scrivi_csv("ABBONAMENTO.csv", ["codice_attivita", "tipo", "sport"], abbonamento_rows)
scrivi_csv("PERIODICO.csv", ["codice_attivita", "periodo"], periodico_rows)
scrivi_csv("ACCESSI_LIMITATI.csv", ["codice_attivita", "n_accessi"], accessi_rows)
