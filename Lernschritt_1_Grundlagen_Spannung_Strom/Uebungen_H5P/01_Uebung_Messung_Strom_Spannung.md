# H5P-Übung: Messung von Strom und Spannung

## 🎯 Lernziel
Interaktive Übungen zum korrekten Messen von Strom und Spannung.

---

## 📝 Quiz: Grundlagen der Messung

### Frage 1: Spannungsmessung
**Wie wird Spannung gemessen?**

- [ ] A) In Reihe zum Bauteil
- [x] B) Parallel zum Bauteil  
- [ ] C) Senkrecht zum Bauteil
- [ ] D) Beliebig

**Feedback:**
- ✅ **Richtig!** Spannung wird immer parallel zum Bauteil gemessen.
- ❌ **A) Falsch:** In Reihe würde das Bauteil kurzgeschlossen.
- ❌ **C) Falsch:** Es gibt keine senkrechte Messung.
- ❌ **D) Falsch:** Die Position ist entscheidend.

---

### Frage 2: Strommessung
**Wie wird Strom gemessen?**

- [x] A) In Reihe zur Leitung
- [ ] B) Parallel zur Leitung
- [ ] C) Neben der Leitung
- [ ] D) Über der Leitung

**Feedback:**
- ✅ **Richtig!** Strom wird immer in Reihe gemessen.
- ❌ **B) Falsch:** Parallel würde einen Kurzschluss verursachen!
- ❌ **C,D) Falsch:** Berührungslose Messung nur mit Stromzange.

---

### Frage 3: Multimeter-Einstellung
**Für eine 12V LED-Schaltung wählst du:**

- [ ] A) 2V Messbereich
- [x] B) 20V Messbereich
- [ ] C) 200V Messbereich  
- [ ] D) 2000V Messbereich

**Feedback:**
- ✅ **Richtig!** 20V Bereich ist optimal für 12V Messungen.
- ❌ **A) Falsch:** 2V Bereich wäre zu klein.
- ❌ **C,D) Falsch:** Zu große Bereiche reduzieren die Genauigkeit.

---

## 🔧 Drag & Drop: Messschaltung aufbauen

### Aufgabe: LED-Schaltung verkabeln
**Ziehe die Komponenten an die richtige Position:**

```
Schaltung aufbauen:
+9V ── ? ── ? ── ? ── GND

Verfügbare Komponenten:
[Widerstand 220Ω] [LED] [Voltmeter] [Amperemeter]
```

**Lösung:**
```
Hauptschaltung:
+9V ── [Widerstand 220Ω] ── [LED] ── GND

Spannungsmessung an LED:
         [LED]
         │   │
      [Voltmeter]

Strommessung in Leitung:
+9V ── [Widerstand] ── [Amperemeter] ── [LED] ── GND
```

**Feedback:**
- ✅ **Voltmeter parallel zur LED:** Misst LED-Spannung
- ✅ **Amperemeter in Reihe:** Misst Strom durch LED
- ❌ **Häufiger Fehler:** Amperemeter parallel = Kurzschluss!

---

## 🧮 Interaktive Berechnung

### Aufgabe: Messwerte interpretieren
**Gegeben ist diese Schaltung:**

```
+5V ── 470Ω ── LED ── GND
```

**Deine Messungen:**
- **Batteriespannung:** 5,0V
- **LED-Spannung:** 2,1V  
- **LED-Strom:** 6,2mA

### Aufgabe 1: Widerstandsspannung berechnen
**U_Widerstand = U_Batterie - U_LED**

Eingabe: U_R = [     ] V

- ☐ Eingabe: 2,9
- ☐ Eingabe: 2,90  
- ☐ Eingabe: 2,9V

**Automatische Auswertung:**
- ✅ **2,9V:** Richtig! U_R = 5,0V - 2,1V = 2,9V
- ❌ **Andere Werte:** Prüfe die Berechnung: U_R = U_Batterie - U_LED

### Aufgabe 2: Widerstandswert prüfen
**R = U_R ÷ I**

Eingabe: R = [     ] Ω

- ☐ Eingabe: 468
- ☐ Eingabe: 470
- ☐ Eingabe: 500

**Automatische Auswertung:**
- ✅ **468Ω:** Richtig! R = 2,9V ÷ 0,0062A = 468Ω
- ✅ **470Ω:** Auch richtig! Das ist der Nennwert (Toleranz!)
- ❌ **500Ω:** Zu ungenau, prüfe die Rechnung.

---

## 🎮 Simulation: Virtuelles Labor

### Tinkercad-Aufgabe
**Baue diese Schaltung nach und messe:**

**Aufgabenstellung:**
1. Erstelle in Tinkercad eine 9V-Batterie mit 220Ω Widerstand und roter LED
2. Messe die Spannung an der LED
3. Messe den Strom durch die LED
4. Trage deine Messwerte ein:

**Deine Messergebnisse:**
- LED-Spannung: [     ] V
- LED-Strom: [     ] mA
- Widerstandsspannung: [     ] V

**Erwartete Werte (Tinkercad):**
- LED-Spannung: ~2,0V
- LED-Strom: ~30mA  
- Widerstandsspannung: ~7,0V

**Bewertung:**
- ✅ **±10% Abweichung:** Sehr gut!
- ⚠️ **±20% Abweichung:** Okay, prüfe die Schaltung
- ❌ **>20% Abweichung:** Fehler in der Schaltung

---

## 🔍 Fehlersuche: Was ist falsch?

### Szenario 1: LED leuchtet nicht
**Problem:** Du baust die Schaltung auf, aber die LED leuchtet nicht.

**Mögliche Ursachen** (Multiple Choice):
- [x] LED falsch herum eingebaut (Anode/Kathode vertauscht)
- [x] Widerstand zu groß gewählt  
- [x] Batterie leer
- [ ] Voltmeter falsch angeschlossen
- [x] Leitungsbruch

**Feedback:**
- ✅ **LED-Polarität:** Häufigster Fehler! Langes Bein = Anode (+)
- ✅ **Zu großer Widerstand:** >10kΩ können LED zu schwach machen
- ✅ **Leere Batterie:** Spannung prüfen!
- ❌ **Voltmeter:** Beeinflusst Schaltung nicht
- ✅ **Leitungsbruch:** Alle Verbindungen prüfen

### Szenario 2: Amperemeter zeigt 0A
**Problem:** LED leuchtet, aber Amperemeter zeigt 0A.

**Diagnose-Schritte:**
1. **Ist das Amperemeter in Reihe geschaltet?**
   - [ ] Ja → Weiter zu Schritt 2
   - [ ] Nein → Schaltung korrigieren

2. **Ist der Messbereich passend?**
   - [ ] 200mA Bereich für 30mA Strom → OK
   - [ ] 20A Bereich für 30mA Strom → Zu ungenau!

3. **Sind die Messleitungen korrekt?**
   - [ ] Rote Leitung in "A"-Buchse → OK
   - [ ] Rote Leitung in "V"-Buchse → Falsch!

---

## ⚡ Zeitdruck-Quiz: Schnelltest

### 60 Sekunden - 10 Fragen
**Beantworte so schnell wie möglich:**

1. **Spannung messen:** Parallel ☐ / In Reihe ☐
2. **Strom messen:** Parallel ☐ / In Reihe ☐  
3. **LED Anode:** Langes Bein ☐ / Kurzes Bein ☐
4. **12V messen mit:** 2V ☐ / 20V ☐ / 200V ☐
5. **Amperemeter parallel =** OK ☐ / Kurzschluss ☐
6. **Voltmeter in Reihe =** OK ☐ / Unterbrechung ☐
7. **5V - 2V =** 3V ☐ / 7V ☐
8. **20mA =** 0,02A ☐ / 0,2A ☐
9. **USB-Spannung:** 3V ☐ / 5V ☐ / 12V ☐
10. **LED ohne Widerstand:** OK ☐ / Kaputt ☐

**Lösungen:**
1. Parallel ✓, 2. In Reihe ✓, 3. Langes Bein ✓, 4. 20V ✓, 5. Kurzschluss ✓, 6. Unterbrechung ✓, 7. 3V ✓, 8. 0,02A ✓, 9. 5V ✓, 10. Kaputt ✓

**Auswertung:**
- **10/10:** Experte! 🏆
- **8-9/10:** Sehr gut! 🥇
- **6-7/10:** Gut! 🥈  
- **<6/10:** Mehr üben! 📚

---

## 🎯 Praxis-Challenge: Server-Messung

### Szenario: Fehlerhafte Server-Stromversorgung
**Du sollst ein Server-Problem analysieren:**

**Gegeben:**
- Server startet nicht
- 12V-Leitung verdächtig
- Multimeter verfügbar

**Deine Aufgabe:**
Plane die Messungen und trage ein, was du messen würdest:

1. **Erste Messung:** 
   - Was: [Spannung am Netzteil-Ausgang]
   - Wie: [Voltmeter parallel]
   - Soll-Wert: [12V]

2. **Zweite Messung:**
   - Was: [Spannung am Mainboard-Stecker]  
   - Wie: [Voltmeter parallel]
   - Soll-Wert: [12V]

3. **Bei Spannungsabfall:**
   - Was: [Strom in der 12V-Leitung]
   - Wie: [Amperemeter in Reihe]
   - Verdacht: [Überlastung/Kurzschluss]

**Bewertungskriterien:**
- ✅ **Systematisches Vorgehen:** Von Quelle zum Verbraucher
- ✅ **Richtige Messart:** Spannung parallel, Strom in Reihe
- ✅ **Sinnvolle Reihenfolge:** Erst Spannung, dann Strom

---

## 🏆 Abschluss-Zertifikat

**Gratulation! Du hast die H5P-Übung "Messung von Strom und Spannung" erfolgreich abgeschlossen.**

**Deine Leistung:**
- Quiz-Fragen: ___/10 Punkte
- Praktische Aufgaben: ___/5 Punkte  
- Fehlersuche: ___/3 Punkte
- Zeitdruck-Quiz: ___/10 Punkte
- Praxis-Challenge: ___/5 Punkte

**Gesamtpunktzahl: ___/33 Punkte**

**Bewertung:**
- 30-33 Punkte: **Ausgezeichnet** 🏆
- 25-29 Punkte: **Sehr gut** 🥇
- 20-24 Punkte: **Gut** 🥈
- 15-19 Punkte: **Befriedigend** 🥉
- <15 Punkte: **Wiederholen empfohlen** 📚

**Nächster Schritt:** [H5P-Übung: U=W/Q](./02_Uebung_Spannung_Formel.md)