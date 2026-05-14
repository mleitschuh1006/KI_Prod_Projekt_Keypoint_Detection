# 02_daten

Dieser Ordner dokumentiert die Datengrundlage des Projekts.

Für das Nachtrainieren und Evaluieren der 3D-Keypoint-Detection-Methoden verwenden wir primär den Datensatz **KeypointNet**. Große Datendateien werden nicht direkt in dieses GitHub-Repository hochgeladen. Stattdessen werden hier Quelle, Download, lokale Ablagestruktur, Vorverarbeitung und verwendete Splits dokumentiert.

## Verwendeter Datensatz: KeypointNet

**KeypointNet** ist ein 3D-Keypoint-Datensatz für Shape-Modelle aus mehreren Objektkategorien. Der Datensatz basiert auf ShapeNet-Modellen und enthält annotierte semantische 3D-Keypoints. Er eignet sich damit gut für unser Projekt, da wir Verfahren zur 3D-Keypoint-Detection nicht nur theoretisch betrachten, sondern auch auf einem passenden Datensatz nachtrainieren und bewerten möchten.

Offizielles Repository:

```text
https://github.com/qq456cvb/KeypointNet