Kurze Erklärung:
Day, Month, Player ist in jeder Zeile und gibt an welche Versuchsperson an welchem Tag gespielt hat.
Die Studie war so ausgelegt, dass jeder der 5 Personen immer Montags und Mittwochs jede Woche spielen sollte. (3 Wochen + 1 Woche Pause + 3 Wochen)

Bei jeder Spielesession sollten 12 Missionen gespielt werden.

Data_C: 
•	Wahrscheinlich am interessantesten für dich
•	Wenn du nur die Zeilen für ein festes Day/Month/Player anguckst bekommst du die Bewegungsdaten für diese Session. Gametime ist die Zeit des CaptureFrames in Sekunden (Beginnt nicht bei 0, sondern bei aufnahmestart). Camx,y,z ist die position vom Fotoapparat in der Hand. Headx,y,z die Position des Kopfes/VR Brille.

Data_A:
•	Zeigt für jeden Spieler und jede Mission an, wie lange die Person gebraucht hat die Mission zu beenden.

Data_B:
•	Zeigt für jede Session die kumulierten Daten an. Insb. Die „Total Hand Distance Travelld“ = Strecke die der Fotoapparat zurückgelegt hat.

Alle 


Die letzten 3 Spalten sind neu. 
•	Gamestate: Status vom Spiel, insb, „MissionIntroduction“ (Einleitung läuft) , „MissionActive“ (Spieler kann Foto machen), „MissionFinished“ (Das fertige Foto wird angezeigt), „IdlingInScene“ (Freies Erkunden)
•	Scene: Die aktuelle Szene (Jede Szene enthält mehrere Missionen)
•	Mission: Name jeder Mission, (!! Wenn der gamestate Idling anzeigt, dann hab ich diesen Wert auf „IDLE“ gesetzt. D.h. wenn hier eine Mission steht, dann ist entweder Intro, Active oder Finished im gamestate. )


==============================
Auswerteideen:
♦ Ratio/correct-zu-total photos
♦ x,y,z-Daten separat auswerten
♦ Nur erste und letzte Messung
♦ cam & head folgen gleicher Bewegung
♦ cam insbesondere hohe horizontal, hohe vertikal Werte