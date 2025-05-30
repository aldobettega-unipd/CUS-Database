import csv
import random
from datetime import datetime, timedelta
from collections import defaultdict

# Costanti
GIORNI_SETTIMANA = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
ORARI_DISPONIBILI = [f"{h:02}:00" for h in range(8, 21)]  # 08:00 - 20:00
MAX_LEZIONI = 3


with open("EDIZIONE_CORSO.csv", newline='', encoding="utf-8") as f:
    edizioni = [row for row in csv.DictReader(f)
                if datetime.strptime(row["data_fine"], "%Y-%m").year in [2025]]


# 3. Carica ATTIVITA.csv per sapere lo sport del corso
sport_per_attivita = {}
with open("ATTIVITA.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        sport_per_attivita[row["codice_attivita"]] = row["sport"]
        

# 4. Carica COMPATIBILITA.csv (campo -> [sport compatibili])
sport_per_campo = defaultdict(list)
with open("COMPATIBILITA.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        sport_per_campo[row["campo"].strip()].append(row["sport"].strip())
        
orari_imp = defaultdict(lambda: defaultdict(list))
with open("ORARIO_IMPIANTO.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        orari_imp[row["via"]][row['giorno_settimana']].extend([row['apertura'], row['chiusura']])
    
campi = []
with open("CAMPO.csv", newline='', encoding="utf-8") as f:
    for row in csv.DictReader(f):
        campi.append(row)
        
orario_campi = defaultdict(dict) #dict con {codice_campo : [inizio, fine]}
for campo in campi:
    for giorno in GIORNI_SETTIMANA:
        orario_campi[campo['codice']].update({giorno : orari_imp[campo['via']][giorno]})
        
#print(orario_campi)

        
lezioni = []
for edizione in edizioni:
    possibili_giorni = GIORNI_SETTIMANA[:-2]
    codice_edizione = edizione["codice_edizione"]
    codice_attivita = edizione["codice_attivita"]
    sport = sport_per_attivita[codice_attivita]

    # Trova i campi compatibili con questo sport
    campi_validi = [c['codice'] for c in campi if sport in sport_per_campo.get(c['codice'], [])]
    if not campi_validi:
        continue  # Nessun campo disponibile per questo sport
    
    change_campo = True
    tentativi2 = 0
    while change_campo and tentativi2 < 5*4:
        campo_scelto = random.choice(campi_validi)
        lezioni_assegnate = 0
        tentativi = 0
        while lezioni_assegnate < MAX_LEZIONI and tentativi < len(possibili_giorni):
            giorno = possibili_giorni[tentativi]
            #if sport in ['Nuoto', 'Arrampicata', 'Boxe', 'Pattinaggio', 'Judo', 'Atletica']:
            orario_inizio = orario_campi[campo_scelto][giorno][0]
            orario_fine = (datetime.strptime(orario_inizio, "%H:%M") + timedelta(hours=1, minutes = 30)).strftime("%H:%M")
            if orario_fine > orario_campi[campo_scelto][giorno][1]:
                print(campo_scelto, giorno, tentativi2, orario_fine, orario_campi[campo_scelto][giorno][1])
                tentativi +=1
                tentativi2 +=1
                
                continue
            orario_campi[campo_scelto][giorno][0] = orario_fine
            '''   
            else:
                orario_fine = orario_campi[campo_scelto][giorno][1]
                orario_inizio = (datetime.strptime(orario_fine, "%H:%M") - timedelta(hours=1, minutes = 30)).strftime("%H:%M")
                if orario_inizio < orario_campi[campo_scelto][giorno][0]:
                    #print(campo_scelto, giorno, tentativi2)
                    tentativi +=1
                    tentativi2 +=1
                    continue
                orario_campi[campo_scelto][giorno][1] = orario_inizio
            '''
            change_campo = False
            possibili_giorni.remove(giorno)
                
            lezioni.append({
                "giorno": giorno,
                "orario_inizio": orario_inizio,
                "orario_fine": orario_fine,
                "campo": campo_scelto,
                "codice_edizione": codice_edizione
            })
                
            lezioni_assegnate += 1
        

# 7. Scrivi LEZIONE.csv
with open("LEZIONE.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["giorno", "orario_inizio", "orario_fine", "campo", "codice_edizione"])
    writer.writeheader()
    writer.writerows(lezioni)
