# Lernschritt 2: Strom messen und Widerstand verstehen
## 🎯 Deine Aufgabe

Heute lernst du **Strom messen** und verstehst, warum **Widerstände** wichtig sind.

**Lernziele:**
- Strom richtig messen (in Reihe)
- Widerstand und seine Funktion verstehen
- Ohmsches Gesetz anwenden

## 📖 Grundwissen

### Strom messen
**Strom wird in Reihe gemessen**
- Leitung unterbrechen
- Multimeter dazwischenschalten
- Strom fließt durch das Messgerät

```
Batterie (+) → [Amperemeter] → LED → Batterie (-)
```

### Widerstand (Resistance) - Symbol: R
**Widerstand = "Bremse" für Strom**
- Einheit: **Ohm (Ω)**
- Funktion: Strom begrenzen, Spannung aufteilen

### Farbcode-System für Widerstände
**220Ω Widerstand erkennen:**
- 1. Ring: Rot = 2
- 2. Ring: Rot = 2  
- 3. Ring: Braun = ×10
- Ergebnis: 22 × 10 = 220Ω

| Farbe | Wert | Farbe | Wert |
|-------|------|-------|------|
| Schwarz | 0 | Grün | 5 |
| Braun | 1 | Blau | 6 |
| Rot | 2 | Violett | 7 |
| Orange | 3 | Grau | 8 |
| Gelb | 4 | Weiß | 9 |

## 🔧 Tinkercad-Übung: Strom messen

### Schaltung aus Lernschritt 1 verwenden
```
Batterie (9V) → Widerstand (220Ω) → LED → Batterie (-)
```

### Schritt-für-Schritt Strommessung:

1. **Multimeter auf "A" (Ampere) stellen**
2. **Leitung zwischen Widerstand und LED unterbrechen**
3. **Amperemeter einbauen:**
   - Rote Leitung: von Widerstand
   - Schwarze Leitung: zur LED Anode
4. **Simulation starten**
5. **Stromwert ablesen:** ca. 30-40mA

### ⚠️ Wichtig:
- **Amperemeter nie parallel anschließen!**
- **Kann Kurzschluss verursachen**

## 🧮 Ohmsches Gesetz

**Grundformel:** U = R × I

### Beispielrechnung:
- **Gegeben:** R = 220Ω, I = 30mA = 0,03A
- **Gesucht:** Spannung am Widerstand
- **Rechnung:** U = 220Ω × 0,03A = 6,6V

### Umstellungen:
- **I = U ÷ R** (Strom berechnen)
- **R = U ÷ I** (Widerstand berechnen)

## 🔬 Experimente

### Experiment 1: Verschiedene Widerstände
**Teste verschiedene Widerstandswerte:**

| Widerstand | Erwarteter Strom | Gemessener Strom |
|------------|------------------|------------------|
| 220Ω | ~40mA | _____ mA |
| 470Ω | ~20mA | _____ mA |
| 1kΩ | ~10mA | _____ mA |

**Beobachtung:** Größerer Widerstand → kleinerer Strom

### Experiment 2: LED ohne Widerstand
**⚠️ Nur in Tinkercad testen!**

1. **LED direkt an 9V Batterie anschließen**
2. **Was passiert?** LED wird überlastet
3. **Warum Widerstand nötig?** Schutz vor Überstrom

## 🚨 Häufige Fehler

### Problem: Amperemeter zeigt 0A
**Lösung:** Multimeter in Reihe, nicht parallel anschließen

### Problem: Simulation funktioniert nicht
**Lösung:** Alle Verbindungen prüfen, besonders Amperemeter

### Problem: Widerstandswert ablesen
**Lösung:** Farbcode von links nach rechts lesen

## ✅ Praktische Anwendung

**Server-Netzgerät Analyse:**
- **Input:** 230V AC, 2A
- **Output:** 12V DC, 10A

**Fragen:**
1. Welche Leistung nimmt das Netzgerät auf?
2. Welche Leistung gibt es ab?

**Antworten:**
1. P = U × I = 230V × 2A = **460W**
2. P = U × I = 12V × 10A = **120W**

## 🧮 Rechenübungen

**Aufgabe 1:** LED-Schaltung
- Batterie: 5V
- LED-Spannung: 2V
- Gewünschter Strom: 20mA
- **Gesucht:** Widerstandswert

**Lösung:**
1. Spannung am Widerstand: 5V - 2V = 3V
2. R = U ÷ I = 3V ÷ 0,02A = **150Ω**

**Aufgabe 2:** Einheiten umrechnen
- 5kΩ = _____ Ω
- 0,05A = _____ mA
- 2000mV = _____ V

## ✅ Selbsttest

1. **Strom messen:** _____ zum Stromkreis (parallel/in Reihe)
2. **220Ω Widerstand:** Farben Rot-Rot-_____ (Braun/Grün)
3. **Ohmsches Gesetz:** U = _____ × _____ (R×I/I×R)
4. **5000Ω = _____ kΩ**

## 🎯 Lösungen

### Rechenübungen:
- **5kΩ = 5000Ω**
- **0,05A = 50mA** 
- **2000mV = 2V**

### Selbsttest:
1. **in Reihe**
2. **Braun**
3. **R × I**
4. **5kΩ**

---

## 📝 Meine Messergebnisse

```
Strommessung:
- 220Ω: _____ mA
- 470Ω: _____ mA  
- 1kΩ: _____ mA

Beobachtungen:
- Strom in Reihe messen
- Größerer Widerstand = kleinerer Strom
- Widerstand schützt LED
```

**✅ Bereit für komplexere Schaltungen? → Lernschritt 3!**

---

### 🌐 English Quick Reference
- **Current (Strom):** measured in series, unit: Ampere (A)
- **Resistance (Widerstand):** opposes current flow, unit: Ohm (Ω)
- **Ohm's Law:** U = R × I
- **Color code:** sequence of colors indicates resistance value