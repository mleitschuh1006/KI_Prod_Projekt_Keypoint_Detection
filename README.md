# 3D Keypoint Detection

Dieses Repository enthält die Projektarbeit zur **3D Keypoint Detection** im Modul **KI in der Produktion**.

Ziel ist es, ausgewählte Verfahren zur Erkennung von Keypoints auf 3D-Punktwolken zu verstehen, praktisch umzusetzen und anhand eines geeigneten Datensatzes zu bewerten. Als Datengrundlage wird hauptsächlich **KeypointNet** verwendet.

## Projektziel

Im Projekt sollen nicht möglichst viele Methoden vollständig umgesetzt werden. Stattdessen liegt der Fokus darauf, eine geeignete Methode fundiert auszuwählen, nachvollziehbar zu erklären, nachzutrainieren und zu evaluieren.

Die Arbeit umfasst:

- Recherche relevanter Paper und öffentlicher Repositories
- Dokumentation der Verfahren in LaTeX
- Auswahl einer geeigneten Methode für die Umsetzung
- Vorbereitung und Nutzung des KeypointNet-Datensatzes
- Training, Evaluation und Bewertung der Ergebnisse

## Repository-Struktur

```text
.
├── 01_recherche/      # Paper, LaTeX-Dokumentation und wissenschaftliche Grundlagen
├── 02_daten/          # Dokumentation zu KeypointNet, Datenstruktur und Splits
├── 03_code/           # Eigener Code für Training, Evaluation und Visualisierung
├── 04_experimente/    # Konfigurationen und Protokolle der Versuche
├── 05_ergebnisse/     # Metriken, Plots, Tabellen und Auswertung
└── README.md          # Allgemeine Projektübersicht
```

## Datensatz

Für Training und Evaluation wird primär **KeypointNet** genutzt:

```text
https://github.com/qq456cvb/KeypointNet
```

Große Datendateien werden nicht direkt im Repository gespeichert. Stattdessen werden Download, Ablagestruktur, Vorverarbeitung und Splits im Ordner `02_daten/` dokumentiert.

## Betrachtete Methoden

In der Recherche werden unter anderem folgende Verfahren betrachtet:

- **UKPGAN**
- **Skeleton Merger**
- **SC3K**
- **KeypointDETR**
- **FL3K**
- **3DFeat-Net**

Wichtig für die finale Auswahl sind Verständlichkeit, wissenschaftliche Relevanz, öffentliche Code-Verfügbarkeit und die Möglichkeit, das Modell mit KeypointNet nachzutrainieren oder zu evaluieren.

## Empfohlener Arbeitsablauf

1. Paper und Repositories in `01_recherche/` dokumentieren.
2. KeypointNet lokal vorbereiten und Splits in `02_daten/` festhalten.
3. Eine Methode für die Umsetzung auswählen.
4. Training und Evaluation über `03_code/` und `04_experimente/` durchführen.
5. Ergebnisse in `05_ergebnisse/` speichern und bewerten.

## Hinweis

Dieses Repository ist als strukturierte Arbeitsbasis für Recherche, Umsetzung und Präsentation gedacht. Die finale Bewertung soll zeigen, wie gut die gewählte Methode 3D-Keypoints erkennt und wie nachvollziehbar Training, Evaluation und Ergebnisse dokumentiert wurden.