# 02_daten

Dieser Ordner beschreibt die Datengrundlage des Projekts. Er dient nicht als Speicherort für große Rohdaten, sondern als zentrale Dokumentation für Datenquelle, Download, lokale Ablagestruktur, Vorverarbeitung und verwendete Splits.

Für das Nachtrainieren und Evaluieren der 3D-Keypoint-Detection-Methoden verwenden wir primär den Datensatz **KeypointNet**.

## Ziel dieses Ordners

In diesem Ordner soll nachvollziehbar dokumentiert werden,

- woher die Daten stammen,
- welche Daten tatsächlich verwendet wurden,
- wie die Daten lokal abgelegt werden,
- welche Vorverarbeitungsschritte durchgeführt wurden,
- welche Trainings-, Validierungs- und Test-Splits genutzt werden,
- und welche Daten für welche Experimente verwendet wurden.

Damit soll sichergestellt werden, dass Training und Evaluation reproduzierbar bleiben.

## Verwendeter Datensatz: KeypointNet

**KeypointNet** ist ein Datensatz für semantische 3D-Keypoint-Detection auf Shape-Modellen. Der Datensatz basiert auf ShapeNet-Modellen und enthält menschlich annotierte 3D-Keypoints für verschiedene Objektkategorien.

Offizielles Repository:

```text
https://github.com/qq456cvb/KeypointNet