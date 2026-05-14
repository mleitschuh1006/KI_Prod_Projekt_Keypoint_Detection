# 03_code

Dieser Ordner enthält den eigentlichen Programmcode.

## Struktur

```text
03_code/
├── models/        # Modell-Wrapper oder eigene Implementierungen
├── utils/         # Hilfsfunktionen für Daten, Metriken und Visualisierung
├── train.py       # Einstiegspunkt für Training/Nachtraining
├── evaluate.py    # Evaluation gespeicherter Modelle
└── visualize.py   # Visualisierung von Punktwolken und Keypoints
```

Der Code sollte so geschrieben werden, dass jedes Experiment über eine Config-Datei aus `04_experimente/configs/` reproduzierbar gestartet werden kann.
