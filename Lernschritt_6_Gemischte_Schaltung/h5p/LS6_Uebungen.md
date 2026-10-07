# H5P-Quelle – Lektion 6: Gemischte Schaltung

Quelle für `edu-h5p`. Erzeugen: `edu-h5p "Lernschritt_6_Gemischte_Schaltung"` → `h5p/generated/`.
Inhaltlich identisch mit Übung 3–6 in `../Uebungen_H5P.md` (Übung 1–2 brauchen die Abbildung und bleiben im LiaScript-Kurs).

## Übung 3 – Vorhersage: Die Raumtür geht auf (H5P.MultiChoice) | AFB II
**Titel:** Vorhersage: Die Raumtür geht auf

**Frage:** Alarmzentrale: 9 V, R1 = 220 Ω in Reihe mit zwei parallelen Zweigen (S1 + R2 = 470 Ω, S2 + R3 = 1 kΩ). Beide Türen sind zu. Jetzt wird die Raumtür geöffnet (S2 offen). Was passiert? Mehrere Antworten sind richtig.
- [x] Der Gesamtstrom I wird kleiner.
- [x] Die Anzeige U1 an R1 wird kleiner.
- [x] Die Spannung U23 an R2 wird größer.
- [ ] Der Strom I2 durch R2 bleibt gleich.

**Feedback:** Ein Zweig fällt weg, R_ges steigt, I sinkt, also sinkt U1 = R1 · I. Für R2 bleibt mehr Spannung (U23 = 9 V − U1), deshalb steigt auch I2.

## Übung 4 – Neue Platine, gleiche Methode (H5P.MultiChoice) | AFB II
**Titel:** Neue Platine, gleiche Methode

**Frage 1:** U = 9 V, R1 = 330 Ω in Reihe mit R2 = 1 kΩ parallel R3 = 1 kΩ. Wie groß ist der Gesamtstrom I?
- [ ] 3,9 mA
- [x] 10,8 mA
- [ ] 18,0 mA
- [ ] 27,3 mA

**Feedback:** R23 = 500 Ω, R_ges = 830 Ω, I = 9 V / 830 Ω ≈ 10,8 mA.

**Frage 2:** Gleiche Schaltung. Welche Spannung U1 liegt an R1?
- [ ] 1,3 V
- [x] 3,6 V
- [ ] 5,4 V
- [ ] 9,0 V

**Feedback:** U1 = 330 Ω · 10,8 mA ≈ 3,6 V.

**Frage 3:** Gleiche Schaltung. Welcher Strom I2 fließt durch R2?
- [x] 5,4 mA
- [ ] 9,0 mA
- [ ] 10,8 mA

**Feedback:** An R2 liegt nur U23 = 9 V − 3,6 V = 5,4 V, also I2 = 5,4 V / 1 kΩ = 5,4 mA.

## Übung 5 – Fehlersuche (H5P.MultiChoice) | AFB III
**Titel:** Fehlersuche an der Alarmzentrale

**Frage:** Alarmzentrale, beide Türen zu. Erwartet: U1 = 3,67 V und I = 16,7 mA. Gemessen: U1 = 1,17 V und I = 5,3 mA. Welcher Aufbaufehler erklärt die Messwerte?
- [ ] R1 ist unterbrochen.
- [ ] Die Rack-Tür ist doch offen.
- [x] R2 und R3 sind in Reihe statt parallel geschaltet.
- [ ] Die Leitung zwischen A und B ist kurzgeschlossen.

**Feedback:** R_ges = 9 V / 5,3 mA ≈ 1,7 kΩ = 220 Ω + 470 Ω + 1000 Ω. R2 und R3 liegen also in Reihe.

## Übung 6 – Richtig oder falsch? (H5P.TrueFalse) | AFB I
**Titel:** Richtig oder falsch?

| Nr. | Aussage | Lösung |
|---|---|---|
| 1 | In der Alarmzentrale fließt durch R1 immer der Gesamtstrom. | **Wahr** |
| 2 | An jedem Zweig der Parallelgruppe liegt die volle Quellenspannung von 9 V. | **Falsch** – An der Parallelgruppe liegt nur U23 = U − U1. |
| 3 | Es gilt: U1 + U2 + U3 = U. | **Falsch** – U2 und U3 sind dieselbe Spannung U23. Richtig ist U1 + U23 = U. |
| 4 | R_ges ist größer als R1, aber kleiner als R1 + R2. | **Wahr** |
