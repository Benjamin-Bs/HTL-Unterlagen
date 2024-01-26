### Erklärung des Codes (in deutscher Sprache)

Der bereitgestellte Code ist in Python verfasst und dient dazu, Videoaufnahmen zu verarbeiten und bestimmte Aktionen basierend auf den erkannten Körperlandmarken (Landmarks) durchzuführen. Der Code ist in zwei Hauptfunktionen unterteilt: `process_frame_right` und `process_frame_left`.

#### `process_frame_right` Funktion:
Diese Funktion verarbeitet Videobilder, die das rechte Bein einer Person zeigen.


#### `process_frame_left` Funktion:
Die `process_frame_left` Funktion hat eine ähnliche Struktur wie `process_frame_right`, jedoch für das linke Bein.


### Beschreibung der Funktionen
Diese Funktionen verarbeiten Videobilder, die das rechte/linke Bein einer Person zeigen.

1. **Extraktion von Landmarken:** Die Position der rechten/linken Landmarken wie das rechte/linken Knie (`right_knee`), 
    der rechte Knöchel (`right_ankle`), die rechte Ferse (`right_heel`) und der rechte Fußindex (`right_foot_index`) 
    aus den übergebenen Landmarken wird extrahiert.

2. **Berechnung der Distanz:** Die vertikale Distanz zwischen dem rechten Knie und dem rechten Knöchel wird berechnet. 
     Diese Distanz wird benötigt, um später den Zoom-Faktor zu bestimmen.

3. **Berechnung der Bounding Box:** Es werden die minimalen und maximalen X- und Y-Koordinaten der rechten Ferse, des 
    rechten Fußindex und des rechten Knöchels ermittelt. Diese Koordinaten werden dann auf die Größe des Videoframes skaliert.

4. **Anpassung des Seitenverhältnisses:** Je nach Unterschied zwischen der Breite (X) und der Höhe (Y) der Bounding Box 
      wird das Seitenverhältnis der Bounding Box angepasst. Dadurch wird sichergestellt, dass die Bounding Box das Bein 
      effizient einschließt.

5. **Zoom-Berechnung:** Ein Zoom-Faktor wird basierend auf der berechneten Distanz zwischen dem Knie und dem Knöchel 
      angewendet. Dieser Zoom wird verwendet, um die Bounding Box zu erweitern.

6. **Prüfung auf Grenzen:** Es wird überprüft, ob die Bounding Box innerhalb der Grenzen des Videoframes liegt. Wenn die 
       Bounding Box außerhalb dieser Grenzen liegt, wird die Funktion beendet.

7. **Ausschneiden und Verkleinern des Bildes:** Das Bild wird basierend auf den berechneten Koordinaten ausgeschnitten 
    und auf eine Größe von 256x256 Pixeln verkleinert.

8. **Weiterverarbeitung:** Die verarbeitete Bildausschnitt wird an eine Funktion namens `process` übergeben, die hier 
          nicht näher definiert ist. Dies könnte die Anwendung weiterer Bildverarbeitungsschritte oder 
       Analyseoperationen darstellen.
