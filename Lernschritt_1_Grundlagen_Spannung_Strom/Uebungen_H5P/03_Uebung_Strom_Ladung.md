# H5P-Übung: Stromstärke und Ladung (I = Q/t)

## 🎯 Lernziel
Interaktive Übungen zur Formel I = Q/t und dem Verständnis von Stromfluss.

---

## 📝 Quiz: Strom verstehen

### Frage 1: Was ist Stromstärke?
**Die Formel I = Q/t bedeutet:**

- [x] A) Strom = Ladung pro Zeit
- [ ] B) Strom = Spannung pro Zeit
- [ ] C) Strom = Energie pro Zeit  
- [ ] D) Strom = Widerstand pro Zeit

**Feedback:**
- ✅ **Richtig!** Stromstärke ist die Ladungsmenge pro Zeiteinheit
- ❌ **B) Falsch:** Das wäre dU/dt (Spannungsänderung)
- ❌ **C) Falsch:** Energie pro Zeit ist Leistung (P = W/t)
- ❌ **D) Falsch:** Widerstand ist unabhängig von der Zeit

---

### Frage 2: Größenordnung verstehen
**1 Ampere entspricht:**

- [ ] A) 1000 Elektronen pro Sekunde
- [ ] B) 1 Million Elektronen pro Sekunde
- [x] C) 6,24 × 10¹⁸ Elektronen pro Sekunde
- [ ] D) Unendlich viele Elektronen pro Sekunde

**Feedback:**
- ✅ **Richtig!** 1A = 1C/s = 6,24 × 10¹⁸ Elektronen/s
- ❌ **A,B) Falsch:** Viel zu wenige Elektronen
- ❌ **D) Falsch:** Es ist eine endliche, sehr große Zahl

---

### Frage 3: Einheiten-Check
**Welche Einheiten-Beziehung stimmt?**

- [x] A) 1 Ampere = 1 Coulomb/Sekunde
- [ ] B) 1 Ampere = 1 Volt/Sekunde
- [ ] C) 1 Ampere = 1 Joule/Sekunde
- [ ] D) 1 Ampere = 1 Ohm/Sekunde

**Feedback:**
- ✅ **Richtig!** 1A = 1C/s ist die Definition
- ❌ **B) Falsch:** Volt/Sekunde wäre Spannungsänderung
- ❌ **C) Falsch:** Joule/Sekunde ist Watt (Leistung)
- ❌ **D) Falsch:** Ohm ist Widerstand, kein Strom

---

## 🧮 Berechnungs-Trainer: Formel anwenden

### Aufgabe 1: Smartphone-Ladung
**Ein Smartphone wird mit 2A für 1,5 Stunden geladen.**

**Gesucht:** Übertragene Ladung Q = ?

**Schritt 1:** Zeit umrechnen
t = 1,5h = [___] s

- ☐ Eingabe: 5400
- ☐ Eingabe: 5.400  
- ☐ Eingabe: 90

**Lösung:** t = 1,5 × 3600s = 5.400s ✅

**Schritt 2:** Ladung berechnen
Q = I × t = 2A × [5.400s] = [___] C

**Lösung:** Q = 10.800C ✅

**Schritt 3:** In Ah umrechnen
Q = 10.800C ÷ 3600 = [___] Ah

**Lösung:** Q = 3Ah ✅

---

### Aufgabe 2: LED-Analyse
**Eine LED leuchtet 8 Stunden mit 20mA.**

**Automatische Berechnung:**
- I = 20mA = [0,02] A
- t = 8h = [28.800] s  
- Q = I × t = 0,02A × 28.800s = [576] C
- Q in Ah = 576C ÷ 3600 = [0,16] Ah

**Interaktive Eingabe:**
Vervollständige die Berechnung:
- 20mA = [___] A → **0,02** ✅
- 8h = [___] s → **28.800** ✅
- Q = [___] C → **576** ✅
- Q = [___] Ah → **0,16** ✅

---

## 🔋 Drag & Drop: Akku-Entladung

### Aufgabe: Verschiedene Verbrauchsszenarien
**Ziehe die passenden Werte zu den Anwendungen:**

**Smartphone-Akku: 3000mAh = 3Ah**

**Verfügbare Werte:**
[0,01A] [0,5A] [1,5A] [3A] [300h] [6h] [2h] [1h]

**Szenarien:**

1. **Standby-Modus:**
   - Strom: [0,01A] ✓
   - Laufzeit: t = Q÷I = 3Ah÷0,01A = [300h] ✓

2. **Normaler Betrieb:**
   - Strom: [0,5A] ✓  
   - Laufzeit: t = 3Ah÷0,5A = [6h] ✓

3. **Gaming/Video:**
   - Strom: [1,5A] ✓
   - Laufzeit: t = 3Ah÷1,5A = [2h] ✓

4. **Volllast (GPS+Video+WLAN):**
   - Strom: [3A] ✓
   - Laufzeit: t = 3Ah÷3A = [1h] ✓

**Erkenntnis:** Höherer Strom → kürzere Laufzeit!

---

## ⚡ Multiple Choice: Stromarten erkennen

### Aufgabe: Welcher Strom fließt wo?

**Gleichstrom (DC):**
- [x] Batterie-Entladung
- [x] USB-Ladekabel  
- [x] LED-Betrieb
- [ ] Netzstrom 230V

**Wechselstrom (AC):**
- [ ] Smartphone-Akku
- [x] Steckdose 230V
- [ ] Auto-Batterie 12V
- [x] Transformator-Primärseite

**Impulsstrom:**
- [x] Schaltnetzteile
- [x] Prozessor-Takt
- [ ] Gleichspannungsnetzteil
- [x] PWM-Steuerung

**Feedback:**
- ✅ **DC:** Konstante Stromrichtung, typisch für Batterien/Elektronik
- ✅ **AC:** Wechselnde Stromrichtung, 50Hz in Deutschland  
- ✅ **Impulsstrom:** Schaltvorgänge, sehr schnelle Änderungen

---

## 🏢 Szenario: Server-Stromanalyse

### IT-Praxis: Rechenzentrum-Monitoring
**Du überwachst einen Server-Rack über 24h:**

**Gegebene Daten:**
- Server ziehen konstant 5A aus 12V-Leitung
- Überwachungszeit: 24h

**Aufgabe 1: Ladungstransport pro Tag**

**Schritt-für-Schritt Berechnung:**
1. **Zeit umrechnen:**
   t = 24h = [86.400] s

2. **Ladung berechnen:**  
   Q = I × t = 5A × [86.400s] = [432.000] C

3. **In Ah umrechnen:**
   Q = 432.000C ÷ 3600 = [120] Ah

**Aufgabe 2: Anzahl Elektronen**
Q = 432.000C × 6,24 × 10¹⁸ = [2,7 × 10²⁴] Elektronen

**Das ist eine unvorstellbare Zahl:**
2.700.000.000.000.000.000.000.000 Elektronen pro Tag!

**Multiple Choice: Ist das viel?**
- [x] Ja, astronomisch viele Elektronen
- [ ] Nein, relativ wenige für einen Server
- [x] Normal für elektrische Ströme
- [ ] Zu wenige, Server defekt

---

## 🧮 Interaktive Berechnung: Kondensator-Entladung

### Aufgabe: Blitzlicht-Kondensator
**Ein Kamera-Blitz entlädt sich in 0,001s (1ms) mit 50A.**

**Deine Berechnung:**

**Schritt 1: Transportierte Ladung**
Q = I × t = [50A] × [0,001s] = [___] C

Eingabe: [0,05] ✅

**Schritt 2: Interpretation**
Diese Ladung wurde in nur 1ms bewegt!

**Vergleich mit anderen Zeiten:**
- Bei 1s: I = 0,05C ÷ 1s = 0,05A = 50mA
- Bei 1min: I = 0,05C ÷ 60s = 0,83mA
- Bei 1h: I = 0,05C ÷ 3600s = 0,014mA

**Erkenntnis:** Gleiche Ladung, verschiedene Zeiten = verschiedene Ströme!

---

## 🎮 Simulation: Stromdichte verstehen

### Aufgabe: Kabel dimensionieren
**Du planst die Verkabelung für verschiedene Geräte:**

**Gegebene Ströme:**
- LED: 20mA
- USB-Gerät: 2A  
- Desktop-PC: 8A
- Server: 20A

**Kabel-Querschnitte verfügbar:**
[0,1mm²] [1mm²] [2,5mm²] [6mm²]

**Regel:** Max. 3A pro mm²

**Zuordnung:**
1. **LED (20mA):** [0,1mm²] ✓ (0,02A ÷ 0,1mm² = 0,2A/mm²)
2. **USB (2A):** [1mm²] ✓ (2A ÷ 1mm² = 2A/mm²)  
3. **PC (8A):** [2,5mm²] ✓ (8A ÷ 2,5mm² = 3,2A/mm²)
4. **Server (20A):** [6mm²] ✓ (20A ÷ 6mm² = 3,3A/mm²)

**Feedback:**
- ✅ **Richtig dimensioniert:** Kabel werden nicht zu heiß
- ❌ **Zu dünne Kabel:** Überhitzung, Brandgefahr!
- ❌ **Zu dicke Kabel:** Verschwendung, teuer

---

## ⏱️ Speed-Quiz: Schnelle Umrechnungen

### 60 Sekunden - 10 Aufgaben
**Rechne so schnell wie möglich um:**

1. **2A für 30min = ? C**
   Antwort: [3600] ✓

2. **1800C in 15min = ? A**  
   Antwort: [2] ✓

3. **5mA = ? A**
   Antwort: [0,005] ✓

4. **7200C = ? Ah**
   Antwort: [2] ✓

5. **3Ah in 2h = ? A**
   Antwort: [1,5] ✓

6. **1000mA für 1h = ? C**
   Antwort: [3600] ✓

7. **4C in 0,5s = ? A**
   Antwort: [8] ✓

8. **10A für 6min = ? C**  
   Antwort: [3600] ✓

9. **0,1A = ? mA**
   Antwort: [100] ✓

10. **5400C ÷ 3600 = ? Ah**
    Antwort: [1,5] ✓

**Auswertung:**
- 10/10: **Strom-Rechnen-Profi!** ⚡
- 8-9/10: **Sehr schnell!** 🏆  
- 6-7/10: **Gut!** ✅
- <6/10: **Mehr üben!** 📚

---

## 🔍 Problemlösung: Akku-Diagnose

### Szenario: Laptop-Akku schwächelt
**Problem:** Laptop-Akku hält nicht mehr so lange wie früher.

**Deine Diagnose-Tools:**
- Multimeter
- Stoppuhr  
- Leistungsmessgerät

**Aufgabe:** Finde heraus, was das Problem ist!

**Test 1: Nennkapazität prüfen**
- **Sollwert:** 4,4Ah (Herstellerangabe)
- **Messung:** Vollladung → komplette Entladung bei 2,2A
- **Zeit gemessen:** [___] h

Eingabe: [1,8] h

**Berechnung:** Q = I × t = 2,2A × 1,8h = 3,96Ah
**Kapazitätsverlust:** (4,4-3,96)/4,4 = 10% ✓

**Test 2: Stromaufnahme prüfen**
- **Normalverbrauch:** 2,2A
- **Gemessener Verbrauch:** [___] A

Eingabe: [2,2] A (normal) oder [3,5] A (zu hoch)

**Diagnose-Matrix:**
| Kapazität | Stromverbrauch | Diagnose |
|-----------|----------------|----------|
| Normal | Normal | Akku OK ✅ |
| Niedrig | Normal | Akku altert 📉 |
| Normal | Hoch | Software-Problem 💻 |
| Niedrig | Hoch | Akku + Software 🔧 |

---

## 📊 Vergleichs-Tool: Verschiedene Ströme

### Aufgabe: IT-Ströme einordnen
**Sortiere diese Geräte nach Stromaufnahme (kleinster zuerst):**

**Geräte-Liste:**
[LED-Statusanzeige] [CMOS-Speicher] [USB-Stick] [Smartphone] [Laptop] [Server]

**Ströme:**  
[10μA] [20mA] [100mA] [1A] [3A] [25A]

**Richtige Zuordnung:**
1. **CMOS-Speicher:** [10μA] ✓
2. **LED-Statusanzeige:** [20mA] ✓  
3. **USB-Stick:** [100mA] ✓
4. **Smartphone (Laden):** [1A] ✓
5. **Laptop:** [3A] ✓
6. **Server:** [25A] ✓

**Interaktive Darstellung:**
```
Stromskala (logarithmisch):
      μA        mA         A         
      │         │          │         
   10μA────────20mA──100mA──1A──3A──25A
    CMOS      LED   USB  Phone Laptop Server
```

**Erkenntnisse:**
- ✅ **Mikroelektronik:** μA-Bereich (sehr sparsam)
- ✅ **LEDs/kleine Verbraucher:** mA-Bereich
- ✅ **Aktive Geräte:** A-Bereich (Hauptverbraucher)

---

## 🏆 Abschluss-Challenge: Strom-Detective

### Mission: Unbekanntes Gerät analysieren
**Du findest ein Gerät mit folgenden Messwerten:**

**Gegeben:**
- Spannung: 5V
- Leistung: 10W
- Betriebszeit: 8h/Tag
- Messung: Nach 5min sind 600C geflossen

**Deine Aufgaben:**

**1. Stromstärke aus Leistung berechnen:**
I = P ÷ U = 10W ÷ 5V = [2] A

**2. Stromstärke aus Ladung/Zeit prüfen:**  
I = Q ÷ t = 600C ÷ 300s = [2] A ✓

**3. Täglichen Ladungsumsatz berechnen:**
Q_Tag = I × t = 2A × (8 × 3600s) = [57.600] C = [16] Ah

**4. Gerät identifizieren:**
5V, 2A, 8h Betrieb → Was könnte das sein?
- [x] Tablet im Dauerbetrieb
- [ ] Smartphone  
- [x] USB-Hub mit vielen Geräten
- [ ] LED-Beleuchtung
- [x] Raspberry Pi mit Zubehör

**Zusatzfrage:** Ist der Stromverbrauch problematisch?
- [ ] Ja, viel zu hoch
- [x] Nein, normal für die Leistung
- [ ] Ja, Gerät defekt
- [x] Nein, aber Dauerverbrauch beachten

---

## 🎯 Meisterschafts-Zertifikat

**Gratulation! Du bist jetzt ein zertifizierter "Strom-und-Ladung-Spezialist"!**

**Deine erworbenen Fähigkeiten:**
- ✅ **Formel beherrschen:** I = Q/t in allen Varianten
- ✅ **Einheiten umrechnen:** A ↔ mA, C ↔ Ah, s ↔ h
- ✅ **Größenordnungen einschätzen:** μA bis A-Bereich  
- ✅ **Praxis anwenden:** Akku-Laufzeit, Kabel-Dimensionierung
- ✅ **Probleme lösen:** Strom-Diagnose, Geräte-Analyse

**Punkteverteilung:**
- Grundlagen-Quiz: ___/15 Punkte
- Berechnungen: ___/25 Punkte  
- Praxis-Szenarien: ___/20 Punkte
- Speed-Quiz: ___/10 Punkte
- Abschluss-Challenge: ___/15 Punkte

**Gesamtpunktzahl: ___/85 Punkte**

**Dein Level:**
- 75-85 Punkte: **Strom-Meister** ⚡🏆
- 65-74 Punkte: **Sehr gut** 🥇
- 55-64 Punkte: **Gut** 🥈  
- 45-54 Punkte: **Befriedigend** 🥉
- <45 Punkte: **Wiederholen empfohlen** 📚

**Badge erhalten:** 🏅 **"I = Q/t Experte"**

**Nächste Herausforderung:** [H5P-Übung: R = 1/G](./04_Uebung_Widerstand_Leitwert.md)