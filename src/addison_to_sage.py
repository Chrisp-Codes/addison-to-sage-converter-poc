import pandas as pd
import tkinter as tk
from tkinter import filedialog

def convert_addison_to_sage(input_file, output_file):
    # Addison-Export laden (Semikolon-getrennt, keine Kopfzeile, alle Spalten als String)
    df = pd.read_csv(input_file, sep=";", header=None, dtype=str)
    
    # Sicherstellen, dass alle Spalten existieren (Fehlende Spalten mit leeren Strings auffüllen)
    df = df.reindex(columns=range(11), fill_value="")
    
    # Monat und Jahr aus der siebten Spalte extrahieren (Index 6)
    df["Monat"] = df[6].str[2:4]  # 3. und 4. Ziffer extrahieren
    df["Jahr"] = df[6].str[4:8]   # 5. bis 8. Ziffer extrahieren
    
    # Entferne die ursprüngliche Datumsspalte
    df = df.drop(columns=[6])
    
    # Spalten in die korrekte Reihenfolge bringen (basierend auf Sage_Export)
    df = df[[0, "Monat", "Jahr", 2, 3, 5, 7, 8, 9, 10]]  # Spalte 5 bleibt erhalten, 6 entfernt
    
    # Datei als Sage-kompatible Textdatei speichern
    df.to_csv(output_file, sep=";", index=False, header=False)
    print(f"Konvertierung abgeschlossen! Datei gespeichert unter: {output_file}")

# Beginn der GUI für Dateiauswahl
def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Wähle die Addison-Exportdatei", filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")])
    if file_path:
        output_path = filedialog.asksaveasfilename(title="Speichern unter", defaultextension=".txt", filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")])
        if output_path:
            convert_addison_to_sage(file_path, output_path)

def main():
    select_file()

if __name__ == "__main__":
    main()
