import os
import json

# Percorso della cartella contenente i CSV
folder_path = './file'
# Nome del file di output che verrà letto dall'HTML
output_file = 'database.js'

def sync():
    db = {}
    
    # Crea la cartella se non esiste
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Cartella '{folder_path}' creata. Inserisci i tuoi file .csv lì dentro.")
        return

    # Scansiona tutti i file .csv
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    if not files:
        print("Nessun file .csv trovato nella cartella /file/")
        return

    for file_name in files:
        # Usa il nome del file (senza estensione) come nome della categoria
        cat_name = os.path.splitext(file_name)[0].replace('_', ' ').upper()
        words = []
        
        try:
            # Legge il file con codifica utf-8 per supportare accenti
            with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as f:
                for line in f:
                    # Supporta sia la virgola che il punto e virgola
                    if ';' in line or ',' in line:
                        separator = ';' if ';' in line else ','
                        parts = line.split(separator)
                        if len(parts) >= 2:
                            words.append({
                                "ita": parts[0].strip(),
                                "eng": parts[1].strip()
                            })
            
            if words:
                db[cat_name] = words
                print(f"✅ Caricato: {file_name} ({len(words)} parole)")
        except Exception as e:
            print(f"❌ Errore nel caricamento di {file_name}: {e}")

    # Genera il file JavaScript
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"const auto_db = {json.dumps(db, ensure_ascii=False, indent=4)};")
    
    print(f"\nSincronizzazione completata! Creato '{output_file}' con {len(db)} categorie.")
    print("Ora puoi aprire o ricaricare index.html")

if __name__ == "__main__":
    sync()