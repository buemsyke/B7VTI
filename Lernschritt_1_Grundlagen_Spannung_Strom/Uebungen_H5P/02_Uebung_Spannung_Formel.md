# H5P-Übung: Elektrische Spannung (U = W/Q)

## 🎯 Lernziel
Interaktive Übungen zur Formel U = W/Q und deren Anwendung in IT-Systemen.

---

## 📝 Quiz: Formelverständnis

### Frage 1: Formel-Bedeutung
**Was bedeutet die Formel U = W/Q?**

- [ ] A) Spannung = Widerstand ÷ Ladung
- [x] B) Spannung = Arbeit ÷ Ladung
- [ ] C) Spannung = Leistung ÷ Ladung
- [ ] D) Spannung = Zeit ÷ Ladung

**Feedback:**
- ✅ **Richtig!** U = W/Q bedeutet: Spannung ist Arbeit pro Ladung
- ❌ **A) Falsch:** Das wäre eine andere Beziehung
- ❌ **C) Falsch:** Leistung ist P = W/t
- ❌ **D) Falsch:** Zeit hat andere Einheit

---

### Frage 2: Einheiten
**Welche Einheiten-Beziehung ist korrekt?**

- [x] A) 1 Volt = 1 Joule/Coulomb
- [ ] B) 1 Volt = 1 Watt/Coulomb
- [ ] C) 1 Volt = 1 Ampere/Coulomb
- [ ] D) 1 Volt = 1 Ohm/Coulomb

**Feedback:**
- ✅ **Richtig!** 1V = 1J/C ist die korrekte Definition
- ❌ **B) Falsch:** Watt ist Leistung, nicht Energie
- ❌ **C) Falsch:** Ampere ist Strom
- ❌ **D) Falsch:** Ohm ist Widerstand

---

### Frage 3: Physikalische Bedeutung
**Hohe Spannung bedeutet:**

- [x] A) Viel Energie pro Ladung
- [ ] B) Viel Ladung pro Energie
- [ ] C) Wenig Energie pro Ladung
- [ ] D) Keine Energie

**Feedback:**
- ✅ **Richtig!** Hohe Spannung = viel Energie wird pro Ladung übertragen
- ❌ **B,C,D) Falsch:** Das widerspricht der Definition U = W/Q

---

## 🧮 Berechnungs-Tool: Formel umstellen

### Aufgabe: Fehlende Werte berechnen
**Wähle die gewünschte Berechnung:**

**Fall 1: Spannung berechnen**
- Gegeben: W = 36 J, Q = 3 C
- Gesucht: U = ?

Eingabe: U = [     ] V

**Automatische Prüfung:**
- ☐ Eingabe: 12
- ☐ Eingabe: 12V
- ☐ Eingabe: 12 Volt

**Lösung:** U = W/Q = 36J/3C = 12V ✅

---

**Fall 2: Arbeit berechnen**
- Gegeben: U = 5V, Q = 2C  
- Gesucht: W = ?

Eingabe: W = [     ] J

**Umstellung:** W = U × Q

**Lösung:** W = 5V × 2C = 10J ✅

---

**Fall 3: Ladung berechnen**
- Gegeben: U = 24V, W = 120J
- Gesucht: Q = ?

Eingabe: Q = [     ] C

**Umstellung:** Q = W ÷ U

**Lösung:** Q = 120J ÷ 24V = 5C ✅

---

## 🔋 Drag & Drop: Akku-Energie berechnen

### Aufgabe: Smartphone-Akku analysieren
**Ziehe die richtigen Werte in die Berechnung:**

**Gegeben:**
[3,7V] [4000mAh] [4Ah] [14.400C] [14,8Wh] [53.280J]

**Berechnung Schritt für Schritt:**

1. **Spannung:** U = [3,7V] ✓

2. **Kapazität umrechnen:** 
   Q = 4000mAh = [4Ah] ✓ = 4 × 3600s = [14.400C] ✓

3. **Energie in Joule:**
   W = U × Q = 3,7V × [14.400C] ✓ = [53.280J] ✓

4. **Energie in Wh:**
   W = 53.280J ÷ 3600 = [14,8Wh] ✓

**Feedback:**
- ✅ **Alle richtig:** Perfekt! Du verstehst die Umrechnungen.
- ❌ **Fehler bei mAh→C:** Denke daran: 1Ah = 3600C
- ❌ **Fehler bei J→Wh:** Denke daran: 1Wh = 3600J

---

## 🏢 Szenario: USV-Berechnung

### IT-Praxis: Rechenzentrum-USV
**Situation:** Du planst eine USV für kritische Server.

**Aufgabe:** Berechne die Überbrückungszeit

**Schritt 1: Gegebene Werte einordnen**
- USV-Batterie: 48V, 100Ah
- Server-Last: 2400W

**Schritt 2: Gespeicherte Energie berechnen**

Eingabe der Formel:
- W = [U] × [Q]
- W = [48V] × [360.000C]  
- W = [17.280.000J] = [4.800Wh]

**Schritt 3: Überbrückungszeit berechnen**

Eingabe:
- t = W ÷ P  
- t = [4.800Wh] ÷ [2.400W]
- t = [2h] = [120min]

**Interaktive Bewertung:**
- ✅ **2h (120min):** Richtig! Die USV hält 2 Stunden.
- ❌ **Andere Werte:** Prüfe: t = Energie ÷ Leistung

**Zusatzfrage:** Ist das ausreichend?
- [x] Ja, für kontrollierten Shutdown
- [x] Ja, bis Generator anspringt
- [ ] Nein, zu kurz für 24h Betrieb
- [ ] Nein, Server brauchen mehr

---

## ⚡ Multiple Choice: Gefahr durch Spannung

### Frage: Warum ist hohe Spannung gefährlich?
**Basis: U = W/Q**

- [x] A) Hohe Spannung = viel Energie pro Ladung = mehr Schaden
- [ ] B) Hohe Spannung = viel Ladung = mehr Stromfluss
- [ ] C) Hohe Spannung = viel Zeit = längere Einwirkung
- [ ] D) Hohe Spannung = wenig Widerstand = mehr Strom

**Erweiterte Erklärung:**
**Bei U = 230V wird pro Coulomb Ladung 230J Energie übertragen.**
**Bei U = 12V werden nur 12J pro Coulomb übertragen.**

**Daher:** Höhere Spannung → mehr Energie → größere Gefahr!

**Gefahrengrenzen:**
- < 50V: Ungefährlich ✅
- 50-120V: Vorsicht! ⚠️  
- > 120V: Gefahr! ⛔

---

## 🎮 Simulation: Energieverteilung im PC

### Aufgabe: PC-Komponenten analysieren
**Ein Gaming-PC hat verschiedene Spannungsschienen:**

**Gegeben:**
- +12V Schiene: 30A
- +5V Schiene: 10A  
- +3,3V Schiene: 15A

**Deine Aufgabe:** Berechne die übertragene Energie pro Stunde

**Interaktive Eingabe:**

**+12V Schiene:**
- Ladung pro Stunde: Q₁ = I × t = 30A × 3600s = [108.000C]
- Energie: W₁ = U × Q = 12V × [108.000C] = [1.296.000J] = [360Wh]

**+5V Schiene:**  
- Ladung pro Stunde: Q₂ = [18.000C]
- Energie: W₂ = [90.000J] = [25Wh]

**+3,3V Schiene:**
- Ladung pro Stunde: Q₃ = [54.000C]  
- Energie: W₃ = [178.200J] = [49,5Wh]

**Gesamtenergie pro Stunde:**
W_ges = 360Wh + 25Wh + 49,5Wh = [434,5Wh]

**Stromkosten (0,30€/kWh):**
Kosten = 0,4345kWh × 0,30€ = [0,13€] pro Stunde

---

## 🔍 Fehleranalyse: Typische Rechenfehler

### Szenario: Student berechnet Laptop-Akku
**Aufgabe:** Finde die Fehler in dieser Rechnung!

**Schüler-Lösung:**
```
Gegeben: Laptop-Akku 19V, 4,74Ah
Gesucht: Gespeicherte Energie

Rechnung:
W = U × Q = 19V × 4,74Ah = 90,06 VAh = 90,06J ❌
```

**Fehlersuche** (Multiple Selection):
- [x] Einheit falsch: VAh ≠ J  
- [x] Fehlende Umrechnung: Ah → C
- [ ] Falsche Formel verwendet
- [x] Endeinheit falsch

**Korrekte Lösung:**
```
W = U × Q
Q = 4,74Ah = 4,74 × 3600C = 17.064C  
W = 19V × 17.064C = 324.216J = 90,06Wh ✅
```

**Häufige Fehlerquellen:**
1. **Ah nicht in C umrechnen** ❌
2. **VAh statt Wh schreiben** ❌
3. **J und Wh verwechseln** ❌
4. **Formeln vertauschen** ❌

---

## ⏱️ Speed-Challenge: Schnellrechnen

### 90 Sekunden - 8 Aufgaben
**Berechne so schnell wie möglich:**

1. **U = 12V, Q = 2C → W = ?**
   Antwort: [24J] ✓

2. **W = 50J, Q = 5C → U = ?**  
   Antwort: [10V] ✓

3. **U = 5V, W = 15J → Q = ?**
   Antwort: [3C] ✓

4. **2000mAh bei 3,7V → W = ?**
   Antwort: [7,4Wh] ✓

5. **24V, 100Ah → W in kWh?**
   Antwort: [2,4kWh] ✓

6. **1V = ? J/C**
   Antwort: [1] ✓

7. **3600C = ? Ah**  
   Antwort: [1Ah] ✓

8. **120J ÷ 12V = ? C**
   Antwort: [10C] ✓

**Auswertung:**
- 8/8 in 90s: **Energieformel-Experte!** ⚡
- 6-7/8: **Sehr gut!** 🏆
- 4-5/8: **Gut!** ✅  
- <4/8: **Mehr üben!** 📚

---

## 📊 Vergleichs-Tool: Energiespeicher

### Aufgabe: Verschiedene Technologien bewerten
**Berechne die Energiedichte verschiedener Systeme:**

**Interaktive Tabelle:**

| Technologie | Spannung | Kapazität | Masse | Energie | Energiedichte |
|-------------|----------|-----------|-------|---------|---------------|
| **Smartphone** | 3,7V | 3000mAh | 50g | [11,1Wh] | [222 Wh/kg] |
| **Laptop** | 11,1V | 4400mAh | 300g | [48,8Wh] | [163 Wh/kg] |
| **E-Auto** | 400V | 200Ah | 500kg | [80kWh] | [160 Wh/kg] |
| **USV** | 12V | 100Ah | 30kg | [1,2kWh] | [40 Wh/kg] |

**Eingabe-Felder** (zum Ausfüllen):
- Smartphone: W = 3,7V × 3Ah = [11,1] Wh
- Laptop: W = 11,1V × 4,4Ah = [48,8] Wh  
- E-Auto: W = 400V × 200Ah = [80.000] Wh = [80] kWh
- USV: W = 12V × 100Ah = [1200] Wh = [1,2] kWh

**Erkenntnisse:**
- ✅ **Smartphone:** Beste Energiedichte (Li-Po)
- ✅ **E-Auto:** Große Energie, gute Dichte (Li-Ion)  
- ❌ **USV:** Schlechte Energiedichte (Blei-Gel)

---

## 🏆 Abschluss-Projekt: Energy-Calculator

### Aufgabe: Eigenen Rechner programmieren
**Erstelle eine "Formel-Maschine" für U = W/Q**

**Schritt 1: Interface planen**
```
┌─────────────────────────────────┐
│     Energy Calculator          │
├─────────────────────────────────┤
│ Gegeben:                        │
│ ☐ Spannung U = [___] V          │
│ ☐ Arbeit   W = [___] J          │  
│ ☐ Ladung   Q = [___] C          │
├─────────────────────────────────┤
│ Gesucht:                        │
│ ☐ U  ☐ W  ☐ Q                   │
├─────────────────────────────────┤
│ [BERECHNEN]                     │
└─────────────────────────────────┘
```

**Schritt 2: Formeln implementieren**
- **U berechnen:** U = W ÷ Q
- **W berechnen:** W = U × Q
- **Q berechnen:** Q = W ÷ U

**Schritt 3: Validierung**
- ✅ **Einheiten prüfen:** V, J, C
- ✅ **Plausibilität:** Ergebnis sinnvoll?
- ✅ **Rundung:** 3 signifikante Stellen

**Test-Cases:**
1. U=12V, Q=5C → W=60J ✓
2. W=100J, Q=4C → U=25V ✓  
3. U=230V, W=460J → Q=2C ✓

---

## 🎯 Zertifikat: Energieformel-Spezialist

**Herzlichen Glückwunsch! Du hast die H5P-Übung "U = W/Q" erfolgreich gemeistert.**

**Deine Kompetenzen:**
- ✅ **Formel verstehen:** U = Arbeit ÷ Ladung
- ✅ **Einheiten beherrschen:** 1V = 1J/C
- ✅ **Umrechnen können:** mAh ↔ C, J ↔ Wh
- ✅ **Praxis anwenden:** Akku-Energie, USV-Auslegung
- ✅ **Gefahren einschätzen:** Hohe Spannung = hohe Energie

**Deine Punktzahl:**
- Quiz: ___/15 Punkte
- Berechnungen: ___/20 Punkte
- Praxis-Aufgaben: ___/15 Punkte  
- Speed-Challenge: ___/8 Punkte
- Projekt: ___/10 Punkte

**Gesamt: ___/68 Punkte**

**Level erreicht:**
- 60-68 Punkte: **Energieformel-Experte** ⚡🏆
- 50-59 Punkte: **Sehr gut** 🥇
- 40-49 Punkte: **Gut** 🥈
- 30-39 Punkte: **Befriedigend** 🥉
- <30 Punkte: **Wiederholen** 📚

**Nächster Schritt:** [H5P-Übung: I=Q/t](./03_Uebung_Strom_Ladung.md)