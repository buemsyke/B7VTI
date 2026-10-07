# Lernschritt 6 – Hinweise für die Lehrkraft

Lernsituation „Alarmzentrale: Welche Tür ist offen?“ – gegliedert nach der Vorlage des Skills *lernsituation-erstellen*.
Der Stundenverlauf für die Doppelstunde steht in [Stundenverlauf.md](./Stundenverlauf.md).

## 1. Einbettung

| Feld | Inhalt |
|---|---|
| Bildungsgang | B7VTI – Fachinformatik Systemintegration / Informationstechnische Assistenz |
| Lernfeld | LF 2 [PRÜFEN: Titel und Zielformulierung laut Rahmenlehrplan bzw. Bildungsplan eintragen] |
| Bezug | Elektrotechnische Grundgrößen in Gleichstromkreisen berechnen und messtechnisch prüfen |
| Vorwissen | LS 2 (ohmsches Gesetz), LS 3 (Leistung), LS 4 (Reihenschaltung), LS 5 (Parallelschaltung) |

## 2. Ausgangssituation

Die NetSys GmbH baut für einen Kunden eine Alarmzentrale für den Serverraum. Zwei Türkontakte (Rack-Tür, Raumtür) liegen in zwei parallelen Zweigen hinter einem Messwiderstand R1. Die Zentrale misst nur U₁ und soll daraus den Türzustand erkennen. Das Prinzip ist authentisch: Einbruchmeldeanlagen werten Meldelinien mit Abschlusswiderständen nach dem Ruhestromprinzip aus.

**Warum dieser Kontext?** Er macht das Kernphänomen der gemischten Schaltung zum Problem: Durch R1 fließt der Gesamtstrom, deshalb verändert jede Änderung in einem Zweig die Anzeige. In LS 5 galt das gerade nicht (Zweige unabhängig) – daraus entsteht der kognitive Konflikt für den Einstieg.

## 3. Handlungsprodukt

**Prüfprotokoll** mit
- Teil A: alle Größen im Normalzustand (berechnet und simuliert),
- Teil B: Auswertetabelle U₁ für fünf Zustände,
- Teil C: begründete Bewertung der Unterscheidbarkeit.

## 4. Kompetenzen

**Fachkompetenz** – Die Lernenden …
- unterscheiden Reihen- und Parallelanteile einer gemischten Schaltung,
- berechnen R_ges, I sowie alle Teilspannungen und Teilströme durch Zusammenfassen und Zurückrechnen,
- kontrollieren Ergebnisse mit Knoten- und Maschenregel,
- leiten ab, wie sich I, U₁ und U₂₃ ändern, wenn ein Zweig unterbrochen wird.

**Methodenkompetenz** – Die Lernenden …
- lesen einen Schaltplan mit Schaltzeichen nach DIN EN 60617 und Zählpfeilen,
- nutzen eine Simulation für den Soll-Ist-Vergleich,
- dokumentieren Ergebnisse in einem Prüfprotokoll.

**Sozialkompetenz** – Die Lernenden prüfen Rechenschritte im Tandem (Rechnen/Prüfen im Wechsel) und geben sich sachliche Rückmeldung.

**Selbstkompetenz** – Die Lernenden wählen Hilfekarten selbst und schätzen ihren Stand mit der Ich-kann-Liste ein.

## 5. Inhalte

Gemischte Schaltung (R in Reihe zu einer Parallelgruppe) · Ersatzwiderstand · Knoten- und Maschenregel · Kontext Ruhestromprinzip · Belastbarkeit (Additum, Wiederholung LS 3)

## 6. Zeitlicher Umfang

- **Kern:** 1 Doppelstunde (90 min), siehe [Stundenverlauf](./Stundenverlauf.md)
- **Optional:** 45 min Übung und Vertiefung (Übungen 1–6, Aufbau in Tinkercad, Additum)

## 7. Verlaufsplanung (vollständige Handlung)

| Phase | Lernhandlung | Sozialform | Material | Zeit |
|---|---|---|---|---|
| Informieren | Phänomen an der Simulation beobachten, Auftrag erfassen | Plenum | Versuch 06 (Beamer) | 8 min |
| Planen | Reihen- und Parallelteil im Schaltplan markieren, Rechenweg festlegen | EA → PA | Schaltplan, Farbstifte | 9 min |
| Entscheiden | Arbeitsweg wählen: Wissensbaustein allein oder mit Hilfekarten; Rollen verteilen | PA | Hilfekarten | 2 min |
| Ausführen | Teil A berechnen, danach Teil B | PA | Prüfprotokoll, Wissensbaustein | 23 + 11 min |
| Kontrollieren | Werte in der Simulation prüfen, Knoten- und Maschenregel | PA | Versuch 06 | 9 min |
| Bewerten | Auswertetabelle präsentieren, Teil C diskutieren, Ich-kann-Liste | Plenum, EA | Tafel, Ich-kann-Liste | 19 min |

## 8. Material und Medien

- [Handlungssituation](./Handlungssituation.md) mit Prüfprotokoll und Hilfekarten (als Arbeitsblatt drucken)
- [Wissensbaustein](./Fachwissen.md)
- [Versuch 06](../versuche/06_gemischte_schaltung.html) – Falstad-Simulation, offline lauffähig
- [Übungen](./Uebungen_H5P.md) (LiaScript) und `h5p/generated/LS6_Uebungen.h5p` (Moodle)
- Abbildungen in `Ressourcen/` (SVG). Sie lassen sich mit `Ressourcen/zeichne_schaltplaene.py` neu erzeugen (Python + schemdraw).

## 9. Leistungsbewertung

Empfehlung: in dieser Stunde **formativ** (Rückmeldung, keine Note). Das Raster passt auch, wenn das Protokoll eingesammelt wird.

| Kriterium | Erwartung | Punkte |
|---|---|---|
| Struktur erkannt | Reihen- und Parallelteil korrekt markiert | 2 |
| Zusammenfassen | R₂₃, R_ges, I korrekt | 3 |
| Zurückrechnen | U₁, U₂₃, I₂, I₃ korrekt | 4 |
| Kontrolle | Knoten- und Maschenregel angewendet, Simulationswerte eingetragen | 3 |
| Auswertetabelle | 5 Zustände mit richtigem U₁ und sinnvoller Meldung | 5 |
| Bewertung (Teil C) | Aussage plus fachliche Begründung | 3 |
| **Summe** | | **20** |

Mit den Hilfekarten 1–3 sind alle Kriterien voll erreichbar. Hilfekarte 4 ist eine Kontrollhilfe, keine Lösung. Das Additum bringt keine Pflichtpunkte, sondern eine Rückmeldung zum Anforderungsbereich III.

## 10. Differenzierung

- **Mehr Unterstützung:** fünf Hilfekarten in der Handlungssituation (Impuls → Strategie → Teilschritt → Kontrolle, dazu eine Karte zu Teil B). Die Lernenden wählen selbst. Bei Sprachhürden hilft der Satzanfang zu Teil C.
- **Mehr Herausforderung:** Additum A1 (Belastbarkeit von R1 – Entscheiden) und A2 (Ruhestromprinzip – Bewerten). Beide heben den Anforderungsbereich, statt mehr gleichartige Aufgaben zu stellen.

## 11. Anknüpfung Moodle

- **Kursabschnitt:** LS 6 Alarmzentrale
- **Seite:** Auftrag und Schaltplan (Handlungssituation), Wissensbaustein
- **URL/Datei:** Versuch 06
- **Aufgabe (Abgabe):** Foto oder PDF des Prüfprotokolls, Bewertung mit dem Raster aus Feld 9
- **H5P:** `h5p/generated/LS6_Uebungen.h5p` (Übungen 3–6, 9 Fragen)
- **Feedback:** Ich-kann-Liste als Feedback-Aktivität (Exit-Ticket)

---

## Erwartungshorizont

**Teil A – Normalzustand**

| Größe | Wert |
|---|---|
| R₂₃ | 470 · 1000 / 1470 ≈ **319,7 Ω** |
| R_ges | 220 + 319,7 ≈ **539,7 Ω** |
| I | 9 V / 539,7 Ω ≈ **16,68 mA** |
| U₁ | 220 Ω · 16,68 mA ≈ **3,67 V** |
| U₂₃ | 319,7 Ω · 16,68 mA ≈ **5,33 V** |
| I₂ | 5,33 V / 470 Ω ≈ **11,34 mA** |
| I₃ | 5,33 V / 1000 Ω ≈ **5,33 mA** |
| Kontrolle | 3,67 V + 5,33 V = 9,00 V ✓ · 11,34 mA + 5,33 mA = 16,67 mA ✓ |

Die Simulation zeigt U₁ = 3,669 V und I = 16,675 mA (geprüft).

**Teil B – Auswertetabelle**

| Zustand | Restschaltung | I | U₁ | Meldung |
|---|---|---|---|---|
| 1 beide zu | R1 + (R2 ∥ R3) | 16,68 mA | **3,67 V** | alles in Ordnung |
| 2 Rack-Tür offen | R1 + R3 (Reihe) | 7,38 mA | **1,62 V** | Alarm Rack-Tür |
| 3 Raumtür offen | R1 + R2 (Reihe) | 13,04 mA | **2,87 V** | Alarm Raumtür |
| 4 beide offen | Stromkreis unterbrochen | 0 mA | **0 V** | Alarm beide Türen (oder Leitungsbruch) |
| 5 Sabotage (A–B kurzgeschlossen) | nur R1 | 40,9 mA | **9,00 V** | Sabotagealarm |

Zustände 2 und 3 wurden in der Simulation geprüft (Zustand 2: 1,623 V / 7,377 mA).

**Teil C – Modellantwort:** Ja. Die fünf Werte liegen weit genug auseinander (kleinster Abstand 0,8 V zwischen Zustand 1 und 3). Auch mit ±5 % Bauteiltoleranz überlappen sie nicht (Zustand 1: 3,45–3,89 V, Zustand 3: 2,68–3,07 V). Unterscheidbar ist das nur, weil R2 und R3 verschieden groß sind.
*Vertiefung für starke Lernende:* Sinkt die Batteriespannung (9-V-Block entladen sich auf etwa 7 V), verschieben sich alle Werte. Abhilfe: stabilisierte Versorgung (→ LS 9) oder das Verhältnis U₁/U auswerten.

**Additum A1:** Im Sabotagefall gilt P = 9 V · 40,9 mA ≈ 0,37 W > 0,25 W. Der 0,25-W-Widerstand wird überlastet → einen 0,5-W- oder 0,6-W-Typ bestellen. Im Normalzustand reichen 61 mW.
**Additum A2:** Kein Sicherheitsproblem. Nach dem Ruhestromprinzip löst jede Unterbrechung Alarm aus, auch ein durchtrenntes Kabel. Die Zentrale kann nur nicht sagen, *welche* Ursache vorliegt.

## Typische Fehler (Diagnose)

| Fehler | Erkennbar an | Impuls |
|---|---|---|
| R2 und R3 addiert statt parallel | R_ges = 1690 Ω, I ≈ 5,3 mA | „Wie viele Wege hat der Strom ab Knoten A?“ |
| Volle Spannung an der Parallelgruppe angenommen (Übertrag aus LS 5) | I₂ = 9 V / 470 Ω = 19,1 mA | „Welche Spannung bleibt nach R1 noch übrig?“ |
| U₁ + U₂ + U₃ = 9 V angesetzt | Maschenregel „geht nicht auf“ | „Zeig mit dem Finger einen Weg von + nach −.“ |
| Teilströme nicht zurückgerechnet, sondern geschätzt | I₂ = I₃ = I/2 | „Sind R2 und R3 gleich groß?“ |
| mA und A vermischt | Ergebnisse um Faktor 1000 daneben | Einheiten in jede Zeile schreiben lassen |

---

**Zurück zur Übersicht:** [README](../README.md)
