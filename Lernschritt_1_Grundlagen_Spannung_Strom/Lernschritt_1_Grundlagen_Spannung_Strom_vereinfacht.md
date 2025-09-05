# Lernschritt 1: Grundlagen - Spannung und Strom
## 🎯 Deine Aufgabe

Du arbeitest im neuen Rechenzentrum. Heute lernst du die Grundlagen von **Spannung** und **Strom**.

**Lernziele:**
- Spannung und Strom verstehen
- LED richtig anschließen (Anode/Kathode)
- Einfache Messung durchführen

## 📖 Grundwissen

### Spannung (Voltage) - Symbol: U
**Spannung = elektrischer "Druck"**
- Einheit: **Volt (V)**
- Beispiele: USB = 5V, Steckdose = 230V

### Strom (Current) - Symbol: I  
**Strom = fließende Elektrizität**
- Einheit: **Ampere (A)**
- Beispiele: LED = 0,02A, PC = 5A

### LED verstehen
**LED = Leuchtdiode (Light Emitting Diode)**

🔴 **Wichtig: LED hat eine Richtung!**
- **Anode (+)** = längeres Bein → an Plus
- **Kathode (-)** = kürzeres Bein → an Minus
- **Falsch angeschlossen = LED leuchtet nicht**

![LED-Polarität]
```
    Anode (+)     Kathode (-)
        |             |
    ----+----     ----+----
   |         |   |         |
   |    ↗    |   |    ↖    |  
   |         |   |         |
    ---------     ---------
   Längeres Bein  Kürzeres Bein
```

## 🔧 Tinkercad-Übung: LED zum Leuchten bringen

### Aufgabe 1: LED richtig anschließen

**Komponenten:**
- 1x 9V Batterie
- 1x LED (rot)  
- 1x Widerstand 220Ω
- Kabel

**Schaltung:**
```
Batterie (+) → Widerstand → LED Anode (+) → LED Kathode (-) → Batterie (-)
```

### Schritt-für-Schritt:

1. **Batterie platzieren**
2. **LED hinzufügen** - **Achtung: Langes Bein = Anode (+)**
3. **Widerstand einfügen** (verhindert Überstrom)
4. **Kabel verbinden:**
   - Rot: Batterie (+) → Widerstand → LED Anode
   - Schwarz: LED Kathode → Batterie (-)

### ✅ Funktionskontrolle:
- **LED leuchtet:** ✅ Richtig angeschlossen
- **LED leuchtet nicht:** ❌ Prüfe Anode/Kathode

## 🔍 Messung 1: Spannung messen

**Spannung wird parallel gemessen**

1. **Multimeter auf "V" stellen**
2. **Spannungsmessung an LED:**
   - Rote Leitung → LED Anode (+)
   - Schwarze Leitung → LED Kathode (-)
3. **Erwarteter Wert:** ca. 2V

### Warum weniger als 9V?
- LED "verbraucht" nur 2V
- Rest fällt am Widerstand ab

## 🧮 Einfache Rechnung

**Einheiten umrechnen:**

| Angabe | Umrechnung | Ergebnis |
|--------|------------|----------|
| 20mA | ÷ 1000 | 0,02A |
| 2000mV | ÷ 1000 | 2V |
| 5kV | × 1000 | 5000V |

## 🚨 Häufige Fehler vermeiden

### Problem: LED leuchtet nicht
**Lösung:** LED umdrehen (Anode/Kathode vertauscht)

### Problem: LED zu dunkel
**Lösung:** Widerstandswert prüfen (sollte 220Ω sein)

### Problem: Messung zeigt 0V
**Lösung:** Multimeter parallel zur LED anschließen, nicht in Reihe

## ✅ Selbsttest

**Teste dein Verständnis:**

1. **LED-Anschluss:** Langes Bein = _____ (Anode/Kathode)
2. **Spannung messen:** _____ zum Bauteil (parallel/in Reihe)  
3. **20mA in A:** _____ A
4. **LED leuchtet nicht:** Wahrscheinlich _____ vertauscht

## 🎯 Lösungen

1. **Anode**
2. **parallel**  
3. **0,02A**
4. **Anode/Kathode**

---

## 📝 Meine Ergebnisse

```
Messwerte:
- Batteriespannung: _____ V
- LED-Spannung: _____ V
- LED leuchtet: ☐ Ja ☐ Nein

Erkenntnisse:
- LED Anode = längeres Bein
- Spannung parallel messen
- 1A = 1000mA
```

**✅ Aufgabe geschafft? → Weiter zu Lernschritt 2!**

---

### 🌐 English Quick Reference
- **Voltage (Spannung):** electrical "pressure" in Volts
- **Current (Strom):** electrical flow in Amperes  
- **Anode:** positive terminal (long leg on LED)
- **Cathode:** negative terminal (short leg on LED)
