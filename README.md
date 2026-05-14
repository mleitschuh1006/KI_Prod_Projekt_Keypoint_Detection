# 3D Keypoint Detection – Projektübersicht

Dieses Repository dient der strukturierten Recherche, Umsetzung und Bewertung von Verfahren zur 3D Keypoint Detection im Modul **KI in der Produktion**.

## Ziel des Projekts

1. Aktuelle State-of-the-Art-Verfahren zu 3D Keypoint Detection recherchieren.
2. Die Verfahren wissenschaftlich vergleichen und nachvollziehbar dokumentieren.
3. Ein bis zwei geeignete Methoden auswählen.
4. Diese Methoden mit einem passenden Datensatz ausprobieren, nachtrainieren und evaluieren.
5. Ergebnisse verständlich bewerten und dokumentieren.

## Repository-Struktur

```text
.
├── 01_recherche/      # Literaturrecherche, Paper-Zusammenfassungen und LaTeX-Dokumentation
├── 02_daten/          # Hinweise, Download-Skripte und Struktur für verwendete Datensätze
├── 03_code/           # Eigener Python-Code für Modelle, Training, Evaluation und Visualisierung
├── 04_experimente/    # Konfigurationen und Protokolle einzelner Trainings-/Testläufe
├── 05_ergebnisse/     # Plots, Tabellen, Metriken und finale Auswertungen
└── README.md          # Einstiegspunkt und Projektbeschreibung
```

## Empfohlener Arbeitsablauf

1. Paper in `01_recherche/paper_matrix.csv` sammeln.
2. Pro wichtigem Paper eine kurze Notiz in `01_recherche/paper-notizen/` schreiben.
3. Die Recherche in `01_recherche/latex/main.tex` zusammenführen.
4. Geeignete Methoden anhand von Verständlichkeit, Code-Verfügbarkeit, Datensatzanforderungen und Evaluierbarkeit auswählen.
5. Datensatz in `02_daten/` dokumentieren.
6. Experimente über Dateien in `04_experimente/configs/` definieren.
7. Ergebnisse in `05_ergebnisse/` speichern und bewerten.

## Kandidaten für die Umsetzung

Für einen realistischen Projektumfang eignen sich besonders:

- klassische geometrische Baseline, z. B. ISS/SIFT-3D
- USIP als unüberwachtes 3D-Keypoint-Verfahren
- D3Feat als lernbasiertes Verfahren für Detektion und Deskriptoren

KeypointDETR oder andere Transformer-Verfahren sind wissenschaftlich interessant, aber vermutlich aufwendiger umzusetzen.
