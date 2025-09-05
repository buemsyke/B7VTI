# Vertiefung: Runden und Fehlerrechnung

## 🎯 Lernziel
Du lernst korrekt zu runden und Messfehler zu berechnen, um realistische Ergebnisse bei elektrischen Berechnungen zu erhalten.

## 📖 Warum ist korrektes Runden wichtig?

In der **praktischen Elektrotechnik** sind Messwerte **nie exakt**. Multimeter, Oszilloskope und andere Messgeräte haben **begrenzte Genauigkeit**. Daher müssen Berechnungsergebnisse **sinnvoll gerundet** werden.

### ⚠️ Problem: Scheingenauigkeit
```
❌ Falsch (Scheingenauigkeit):
Messung: U = 12,3V, I = 0,5A
Berechnung: P = U × I = 12,3V × 0,5A = 6,15W
Angabe: P = 6,15W (zu genau!)

✅ Richtig (sinnvolle Genauigkeit):  
Messung: U = 12,3V, I = 0,5A
Berechnung: P = U × I = 12,3V × 0,5A = 6,15W
Angabe: P = 6,2W (auf 2 Stellen gerundet)
```

## 🧮 Grundregeln des Rundens

### Rundungsregeln nach DIN
1. **Ziffer < 5:** Abrunden
2. **Ziffer > 5:** Aufrunden  
3. **Ziffer = 5:** Zur nächsten **geraden** Zahl runden

### Rundungsbeispiele
```
Runden auf 2 Dezimalstellen:
12,344 → 12,34 (4 < 5: abrunden)
12,346 → 12,35 (6 > 5: aufrunden)
12,345 → 12,34 (5 → gerade Zahl: 4)
12,355 → 12,36 (5 → gerade Zahl: 6)
```

### Stufenweises Runden vermeiden
```
❌ Falsch (stufenweise):
12,3456 → 12,346 → 12,35 → 12,4

✅ Richtig (direkt):
12,3456 → 12,3 (direkt auf 1 Dezimalstelle)
```

## 📏 Signifikante Stellen

### Was sind signifikante Stellen?
**Signifikante Stellen** sind alle Ziffern, die zur **Genauigkeit** einer Zahl beitragen (außer führende Nullen).

### Regeln für signifikante Stellen
```
Beispiele:
12,3V     → 3 signifikante Stellen
0,0123A   → 3 signifikante Stellen  
1,230kΩ   → 4 signifikante Stellen
1200Ω     → 2 oder 4? (unklar → besser: 1,2kΩ)
```

### Bei Berechnungen
**Ergebnis hat so viele signifikante Stellen wie der ungenaueste Eingangswert.**

```
Beispiel:
U = 12,3V (3 signifikante Stellen)
I = 0,5A  (1 signifikante Stelle!)
P = U × I = 12,3 × 0,5 = 6,15W

Rundung: P = 6W (nur 1 signifikante Stelle)
```

## 🔍 Messgenauigkeit verstehen

### Multimeter-Spezifikationen
```
Typisches Digitalmultimeter:
"±(0,5% vom Messwert + 3 Digits)"

Messung: U = 12,34V
Fehler = 0,5% × 12,34V + 0,003V  
Fehler = 0,062V + 0,003V = 0,065V

Ergebnis: U = 12,34V ± 0,065V
Bereich: 12,275V...12,405V
```

### Absolute vs. relative Fehler
```
Absoluter Fehler: ΔU = ±0,065V
Relativer Fehler: δU = ±0,065V/12,34V = ±0,53%

Bei kleineren Spannungen wird relativer Fehler größer:
U = 1,23V → δU = ±0,065V/1,23V = ±5,3%
```

## 🧮 Fehlerfortpflanzung bei Berechnungen

### Addition/Subtraktion
**Absolute Fehler addieren sich:**
```
U1 = 12,0V ± 0,1V
U2 = 5,0V ± 0,05V
U_ges = U1 + U2 = 17,0V ± (0,1 + 0,05)V = 17,0V ± 0,15V
```

### Multiplikation/Division  
**Relative Fehler addieren sich:**
```
U = 12,0V ± 0,1V → δU = 0,1/12,0 = 0,83%
I = 2,0A ± 0,05A → δI = 0,05/2,0 = 2,5%
P = U × I → δP = δU + δI = 0,83% + 2,5% = 3,33%

P = 12,0V × 2,0A = 24,0W
ΔP = 24,0W × 3,33% = 0,8W
Ergebnis: P = 24,0W ± 0,8W = 24W ± 1W
```

## 🔍 Praktische IT-Beispiele

### Netzteil-Effizienz berechnen
```
Messwerte:
P_ein = 115W ± 2W (Messgenauigkeit 2W)
P_aus = 100W ± 1W (Messgenauigkeit 1W)

Wirkungsgrad:
η = P_aus/P_ein = 100W/115W = 0,870 = 87,0%

Fehlerrechnung:
δη = δP_aus + δP_ein = 1/100 + 2/115 = 1% + 1,74% = 2,74%
Δη = 87,0% × 2,74% = 2,4%

Ergebnis: η = 87% ± 2% (sinnvoll gerundet)
```

### Akku-Laufzeit bestimmen
```
Akku-Kapazität: Q = 4000mAh ± 5%
Stromverbrauch: I = 250mA ± 10mA

Laufzeit: t = Q/I = 4000mAh/250mA = 16h

Fehlerrechnung:
δQ = 5% = 0,05
δI = 10mA/250mA = 4% = 0,04  
δt = δQ + δI = 5% + 4% = 9%

Δt = 16h × 9% = 1,4h
Ergebnis: t = 16h ± 1h (praktisch gerundet)
```

## 🧮 Übungsaufgaben

### Aufgabe 1: Korrekt runden
Runde auf die angegebene Stellenzahl:

1. **12,3456V auf 2 Dezimalstellen:** _____
2. **0,2385A auf 3 Dezimalstellen:** _____
3. **1,2345kΩ auf 1 Dezimalstelle:** _____
4. **99,95W auf ganze Zahl:** _____

### Aufgabe 2: Signifikante Stellen
Bestimme die Anzahl signifikanter Stellen:

1. **12,30V:** _____ Stellen
2. **0,0045A:** _____ Stellen  
3. **1200Ω:** _____ Stellen (unklar geschrieben)
4. **2,0 × 10³Hz:** _____ Stellen

### Aufgabe 3: Messgenauigkeit
Ein Multimeter zeigt "±(1% + 2 Digits)" Genauigkeit:

Messung: I = 1,25A
1. **Absoluter Fehler:** ΔI = _____ A
2. **Relativer Fehler:** δI = _____ %
3. **Messbereich:** I = _____ A bis _____ A

### Aufgabe 4: Fehlerfortpflanzung
```
Gegeben:
U = 24V ± 0,5V
R = 12Ω ± 0,2Ω

Berechne: I = U/R

1. Wert: I = _____ A
2. Relativer Fehler: δI = _____ %  
3. Absoluter Fehler: ΔI = _____ A
4. Ergebnis: I = _____ A ± _____ A
```

## 📊 Rundung bei verschiedenen Anwendungen

### Technische Zeichnungen
```
Maße in mm:
- Grob: 15mm (keine Dezimalstelle)
- Normal: 15,2mm (1 Dezimalstelle)  
- Fein: 15,25mm (2 Dezimalstellen)
- Präzision: 15,254mm (3 Dezimalstellen)
```

### Elektrische Berechnungen
```
Widerstandswerte (E-Reihe):
- E6: 1,0; 1,5; 2,2; 3,3; 4,7; 6,8 Ω
- E12: 1,0; 1,2; 1,5; 1,8; 2,2; 2,7; 3,3; 3,9; 4,7; 5,6; 6,8; 8,2 Ω
- E24: noch feiner gestaffelt

Berechnung ergibt 3,17Ω → Nächster E12-Wert: 3,3Ω
```

### Energiekosten
```
Stromverbrauch: 1234,56 kWh/Jahr
Preis: 0,2854 €/kWh

Kosten = 1234,56 × 0,2854 = 352,34€
Rundung für Rechnung: 352€ (Euro-Cent nicht sinnvoll bei Jahreskosten)
```

## 🔬 Messunsicherheit vs. Rundungsfehler

### Messunsicherheit (viel wichtiger!)
```
Digitalmultimeter: ±0,1% Grundgenauigkeit
Analoge Zeiger: ±1-3% Ablesegenauigkeit  
Oszilloskop: ±2-5% je nach Einstellung
Kalibration: ±0,01% (professionelle Geräte)
```

### Rundungsfehler (meist vernachlässigbar)
```
Rundung von 12,345 auf 12,3:
Relativer Fehler = 0,045/12,345 = 0,36%

Dies ist meist kleiner als die Messungenauigkeit!
```

## ⚠️ Häufige Fehler vermeiden

### Fehler 1: Zu viele Stellen angeben
```
❌ Falsch: P = 12,123456789W (Scheingenauigkeit)
✅ Richtig: P = 12,1W (entsprechend Messgenauigkeit)
```

### Fehler 2: Zwischenergebnisse runden
```
❌ Falsch:
U1 = 12,345V → 12,3V (gerundet)
U2 = 5,678V → 5,7V (gerundet)  
U_ges = 12,3 + 5,7 = 18,0V

✅ Richtig:
U1 = 12,345V (vollständig rechnen)
U2 = 5,678V (vollständig rechnen)
U_ges = 12,345 + 5,678 = 18,023V → 18,0V (am Ende runden)
```

### Fehler 3: Einheitenvorsätze ignorieren
```
❌ Falsch: 1234,5mA → 1235mA (falsche Stellenzahl)
✅ Richtig: 1234,5mA → 1,23A (sinnvolle Einheit und Rundung)
```

## ✅ Selbsttest

**Kreuze die richtigen Antworten an:**

1. **12,345 gerundet auf 2 Dezimalstellen:**
   - ☐ 12,34 ✓
   - ☐ 12,35
   - ☐ 12,3
   - ☐ 12,4

2. **Bei Multiplikation addieren sich:**
   - ☐ Absolute Fehler
   - ☐ Relative Fehler ✓
   - ☐ Quadratische Fehler
   - ☐ Keine Fehler

3. **0,0123A hat wie viele signifikante Stellen?**
   - ☐ 2
   - ☐ 3 ✓
   - ☐ 4
   - ☐ 6

## 🎯 Lösungen

### Aufgabe 1:
1. **12,35V** (6 > 5: aufrunden)
2. **0,239A** (5 → gerade Zahl: 8 → aufrunden)
3. **1,2kΩ** (3 < 5: abrunden)
4. **100W** (9 ≥ 5: aufrunden)

### Aufgabe 2:
1. **4 Stellen** (Null nach Komma ist signifikant)
2. **2 Stellen** (führende Nullen nicht signifikant)
3. **2-4 Stellen** (unklar, besser: 1,2kΩ)
4. **2 Stellen** (wissenschaftliche Notation zeigt es klar)

### Aufgabe 3:
1. **ΔI = 1% × 1,25A + 0,002A = 0,0125A + 0,002A = 0,015A**
2. **δI = 0,015A/1,25A = 1,2%**
3. **I = 1,235A bis 1,265A**

### Aufgabe 4:
1. **I = 24V/12Ω = 2,0A**
2. **δI = δU + δR = 0,5/24 + 0,2/12 = 2,1% + 1,7% = 3,8%**
3. **ΔI = 2,0A × 3,8% = 0,076A ≈ 0,08A**
4. **I = 2,0A ± 0,08A**

## 📝 Merkregeln

```
Rundungsregeln:
□ < 5: abrunden
□ > 5: aufrunden
□ = 5: zur geraden Zahl
□ Nie stufenweise runden

Signifikante Stellen:
□ Alle Ziffern außer führende Nullen
□ Ergebnis: so genau wie ungenauester Wert
□ Bei Unsicherheit: wissenschaftliche Notation

Fehlerrechnung:
□ Addition: absolute Fehler addieren
□ Multiplikation: relative Fehler addieren
□ Messunsicherheit > Rundungsfehler
□ Zwischenergebnisse nicht runden

Praxis-Tipps:
□ Messgenauigkeit beachten
□ Sinnvolle Stellenzahl wählen
□ Einheitenvorsätze nutzen
□ Scheingenauigkeit vermeiden

IT-Anwendung:
□ Widerstandswerte: E-Reihen
□ Energiekosten: Euro, nicht Cent
□ Prozessor-Takt: 3 signifikante Stellen
□ Speichergrößen: binäre Vorsätze
```

---

**🎉 Alle Vertiefungen abgeschlossen!**  
**▶️ Weiter zu den [H5P-Übungen](../Uebungen/)**