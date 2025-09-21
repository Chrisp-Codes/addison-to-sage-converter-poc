# Addison → Sage Konverter (POC)

[🇬🇧 English Version](README_en.md)

⚠️ **Hinweis**  
Dies ist eine **Machbarkeitsstudie (Proof of Concept)** basierend auf der Sage-Importspezifikation.  
Das Tool wurde **nie in einer realen Produktivumgebung** mit Sage getestet.  
Nutzung erfolgt auf eigene Verantwortung.

## Überblick
Dieses Repository enthält ein kleines Python-Tool, das Addison-Lohnexportdateien  
in ein Sage-kompatibles Importformat umwandelt.  
Es wurde entwickelt, um einen früheren Excel/VBA-Makro-Workflow zu ersetzen,  
der manuelle Ordnerstrukturen, Dateiumbenennungen und Pfadanpassungen erforderte.

## Funktionsumfang
- Eingabe: Addison-Exportdatei (`.txt`, 11 Spalten, Semikolon-getrennt)  
- Ausgabe: Sage-kompatible Textdatei (`.txt`)  
- Automatische Extraktion von Monat und Jahr  
- Spalten werden in die von Sage erwartete Reihenfolge gebracht  
- Dateiauswahl über GUI (Tkinter) – keine manuelle Pfadanpassung mehr notwendig  
- Optional: Kompilierbar als portable `.exe` (mit PyInstaller)

## Motivation
Der ursprüngliche Excel/VBA-Makro-Prozess war fehleranfällig und für den B2B-Einsatz ungeeignet:
- Harte Pfade im Code
- Manuelles Umbenennen der Eingabedateien
- Strikte Ordnerstrukturen erforderlich
- Abhängigkeit von Excel und VBA-Know-how

Diese Python-Version vereinfacht den Prozess durch:
- Eigenständiges Tool
- Flexible Eingabe- und Ausgabepfade
- Saubere und robustere Umwandlungslogik

## Status
- Proof of Concept (POC)  
- Nur mit Dummy-Daten getestet  
- Nicht für den produktiven Einsatz vorgesehen

## Technologien
- Python  
- Pandas  
- Tkinter  

## Verwendung
1. Tool starten (`python src/addison_to_sage.py` oder kompilierte `.exe`).  
2. Addison-Exportdatei über die GUI auswählen.  
3. Speicherort für die Ausgabedatei festlegen.  
4. Die konvertierte Sage-kompatible Datei wird automatisch erstellt.

## Beispieldaten
Zur Demonstration ist eine Beispieldatei im Ordner `examples/dummy_addison_export.txt` enthalten.  
Diese enthält Fake-Daten im Addison-Export-Format (11 Spalten, Semikolon-getrennt).

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz veröffentlicht.  
Details siehe [LICENSE](LICENSE).
