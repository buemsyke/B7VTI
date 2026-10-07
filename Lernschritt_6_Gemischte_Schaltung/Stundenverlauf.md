# Stundenverlauf – Lernschritt 6: Gemischte Schaltung

## Kopf

| Feld | Inhalt |
|---|---|
| Klasse / Bildungsgang | B7VTI – FISI / ITA |
| Lernfeld / Lernsituation | LF 2 · LS 6 „Alarmzentrale: Welche Tür ist offen?“ · alle sechs Phasen der vollständigen Handlung in einer Doppelstunde |
| Stunde | Doppelstunde, 90 min *(Annahme – bei 45 min: siehe Sollbruchstelle)* |
| **Stundenziel** | Die Lernenden können für eine gemischte Schaltung (Widerstand in Reihe zu einer Parallelgruppe) R_ges, den Gesamtstrom, alle Teilspannungen und alle Teilströme durch schrittweises Zusammenfassen und Zurückrechnen bestimmen und das Ergebnis mit Knoten- und Maschenregel kontrollieren. |
| Teilziele | Einstieg: Phänomen „ein Zweig ändert alles“ beschreiben · Planen: Reihen- und Parallelteil markieren · Ausführen: Teil A berechnen · Kontrollieren: Soll-Ist-Vergleich mit der Simulation · Bewerten: Unterscheidbarkeit begründen |
| Vorbereitung | Beamer mit [Versuch 06](../versuche/06_gemischte_schaltung.html) (läuft offline) · [Handlungssituation](./Handlungssituation.md) als Arbeitsblatt (1 pro Person) · Schaltplan zusätzlich auf A3 für die Tafel · Farbstifte · 1 Rechner oder Tablet pro Paar · [Ich-kann-Liste](./Ich_kann_Liste.md) |

## Verlauf

| Zeit | Phase | Lehr- und Lernaktivität | Sozialform | Medien | Didaktischer Kommentar |
|---|---|---|---|---|---|
| 0–8 | Einstieg (Informieren) | L zeigt die Alarmzentrale in der Simulation, öffnet erst S1, dann S2. Die Anzeige springt von 3,67 V auf 1,62 V bzw. 2,87 V. **Impuls:** „Die Zentrale misst nur eine einzige Spannung. Woher weiß sie, welche Tür offen ist?“ Vermutungen sammeln (Blitzlicht). | Plenum | Beamer, Versuch 06 | Kognitiver Konflikt zu LS 5: Dort waren die Zweige unabhängig, hier ändert jede Tür die Anzeige. Die Frage bleibt offen und trägt die Stunde. |
| 8–17 | Zielklärung, Planen | Auftrag und Prüfprotokoll vorstellen. S markieren im Schaltplan Reihen- und Parallelteil (EA, 3 min), Abgleich mit dem Nachbarn (PA, 3 min). Kurze Klärung im Plenum. **Impuls:** „Durch welchen Widerstand muss jedes Elektron?“ → R1 führt den Gesamtstrom. | EA → PA → Plenum | Arbeitsblatt, A3-Schaltplan, Farbstifte | Strukturerkennung ist die Schlüsselhürde und wird vor dem Rechnen gesichert. |
| 17–19 | Entscheiden | Paare wählen ihren Weg: Wissensbaustein allein oder mit Hilfekarten. Rollen: Rechnen und Prüfen wechseln bei jeder Größe. | PA | Hilfekarten (im Arbeitsblatt) | Selbstwahl statt Zuweisung, keine Etikettierung. |
| 19–42 | Ausführen I | Teil A: Normalzustand berechnen. L geht herum und achtet auf die typischen Fehler (siehe [Hinweise](./Hinweise_Lehrkraft.md#typische-fehler-diagnose)). Schnelle Paare gehen zu Teil B. | PA | Wissensbaustein, Hilfekarten 1–4 | Größter Block, Lernende aktiv. L gibt Impulse statt Lösungen. |
| 42–51 | Kontrollieren | Werte in der Simulation ablesen (Maus über das Bauteil, P1 zeigt U₁, Amperemeter zeigt I), mit der Rechnung vergleichen, Knoten- und Maschenregel prüfen. Abweichung über 1 %: Fehler suchen. | PA | Versuch 06 | Die Simulation dient als Prüfmittel, nicht als Lösungsquelle. Deshalb erst rechnen, dann simulieren. |
| 51–62 | Ausführen II | Teil B: Auswertetabelle. Die Restschaltungen sind Reihenschaltungen (LS 4). Schnelle: Additum A1/A2. | PA | Arbeitsblatt, Simulation | Transfer: Zweig weg → bekannte Schaltung. **Sollbruchstelle** |
| 62–75 | Sicherung (Bewerten) | Zwei Paare zeigen ihre Auswertetabelle. Gemeinsames Tafelbild (siehe unten). Teil C im Plenum: „Kann die Zentrale sicher unterscheiden?“ → Rückbezug zur Einstiegsfrage. | Plenum | Tafel, Dokumentenkamera | Wird nie gekürzt. Die Einstiegsfrage wird hier beantwortet. |
| 75–81 | Reflexion | Ich-kann-Liste Nr. 1–4 ankreuzen. Exit-Ticket: „Meine größte Hürde heute war …“ | EA | Ich-kann-Liste | Rückmeldung für die Planung der nächsten Stunde. |
| 81–90 | Puffer | — | — | — | 10 % ungeplant |

## Sollbruchstelle

Wird die Zeit knapp, wird Teil B auf die Zustände 2 (Rack-Tür offen) und 5 (Sabotage) gekürzt. Der Rest von Teil B und das Additum werden Hausaufgabe.
**Bei nur 45 min:** Stunde endet nach „Kontrollieren“ mit einer Kurzsicherung (Tafelbild Schritte 1–4). Teil B, Teil C und die Sicherung folgen in der nächsten Stunde.

## Hausaufgabe / Ausblick

- [Übungen 1–6](./Uebungen_H5P.md) bzw. H5P in Moodle, Rest von Teil B
- **Ausblick LS 7:** „R1 und die Parallelgruppe teilen die 9 V unter sich auf – genau das ist ein Spannungsteiler. Nächste Stunde dimensionieren wir einen gezielt.“

## Anhang

### Tafelbild

```text
Gemischte Schaltung = Reihen- UND Parallelschaltung

1  Zusammenfassen     R23  = R2 · R3 / (R2 + R3)
2  Gesamtwiderstand   Rges = R1 + R23
3  Gesamtstrom        I    = U / Rges
4  Zurückrechnen      U1 = R1 · I   U23 = R23 · I   I2 = U23 / R2   I3 = U23 / R3

Kontrolle:  U1 + U23 = U   (Masche)      I2 + I3 = I   (Knoten)

Merke: R1 führt den Gesamtstrom.
       Ändert sich ein Zweig, ändern sich I, U1 und U23.
       Darauf beruht die Alarmzentrale.
```

Rechts daneben: die Auswertetabelle aus Teil B (Zustand → U₁ → Meldung).

### Gelenkstellen – Impulse und erwartete Antworten

| Stelle | Impuls (wörtlich) | Erwartete Antwort / Reaktion |
|---|---|---|
| Einstieg | „Die Zentrale misst nur eine einzige Spannung. Woher weiß sie, welche Tür offen ist?“ | „Der Strom ändert sich.“ / „Der Widerstand wird größer.“ → festhalten, nicht auflösen |
| Planen → Ausführen | „Ihr wisst jetzt, was in Reihe und was parallel liegt. Womit fangt ihr an?“ | „Erst R2 und R3 zusammenfassen.“ |
| Kontrollieren | „Eure Rechnung und die Simulation zeigen verschiedene Werte. Wer hat recht?“ | „Wir prüfen mit der Maschenregel, wo der Fehler liegt.“ |
| Sicherung | „Jetzt zurück zur Frage vom Anfang: Woher weiß die Zentrale, welche Tür offen ist?“ | „Jede Tür verändert R_ges anders, deshalb hat jeder Zustand seine eigene Spannung U₁.“ |

### Eingesetzte Materialien

`Ressourcen/LS6_Alarmzentrale_Schaltplan.svg` · `Ressourcen/LS6_Ersatzschaltbilder.svg` · `versuche/06_gemischte_schaltung.html` · `h5p/generated/LS6_Uebungen.h5p`
