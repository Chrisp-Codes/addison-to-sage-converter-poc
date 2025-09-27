# Addison → Sage Konverter (POC)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-POC-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![English](https://img.shields.io/badge/README-English-informational?style=flat-square)](README_en.md)
[![Deutsch](https://img.shields.io/badge/README-Deutsch-informational?style=flat-square)](README.md)

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

## Feldmapping (Addison → Sage)

Das Tool transformiert eine Addison-Exportdatei mit 11 Spalten in eine Sage-kompatible Importdatei mit 10 Spalten.  
Die wichtigste Transformation ist die Aufspaltung des Datumsfeldes in **Monat** und **Jahr**.

⚠️ Hinweis: Eine offizielle Feldbeschreibung von Addison lag nicht vor.  
Das Mapping basiert auf beobachteten Testdaten und ist daher nicht vollständig abgesichert.

| Addison-Spalte (Input)        | Bedeutung (beobachtet/angenommen) | Sage-Spalte (Output)    | Transformation / Kommentar                 |
|-------------------------------|-----------------------------------|-------------------------|--------------------------------------------|
| [0]                           | Firmennummer                      | [0]                     | 1:1 übernommen                             |
| [1]                           | Personalnummer                    | [3]                     | 1:1 übernommen (verschoben)                |
| [2]                           | Lohnart                           | [4]                     | 1:1 übernommen                             |
| [3]                           | Unbekannt (evtl. Abwesenheiten)   | [5]                     | 1:1 übernommen (nur für Struktur erhalten) |
| [4]                           | Unbekannt (evtl. Abwesenheiten)   | [6]                     | 1:1 übernommen (nur für Struktur erhalten) |
| [5]                           | Unbekannt / ungenutzt             | –                       | entfernt                                   |
| [6]                           | Kodiertes Datum (MMYYYY)          | [1] = Monat, [2] = Jahr | in Monat und Jahr aufgespalten             |
| [7]                           | Betrag in €                       | [7]                     | 1:1 übernommen                             |
| [8]                           | Prozentualer Wert                 | [8]                     | 1:1 übernommen                             |
| [9]                           | Unbekannt / reserviert            | [9]                     | 1:1 übernommen (nur für Struktur erhalten) |
| [10]                          | Zuschlagsstunden                  | [10]                    | 1:1 übernommen                             |


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
