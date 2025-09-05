# Vertiefung: Messung von Strom und Spannung

## 🎯 Lernziel
Du lernst die korrekten Messverfahren für Strom und Spannung kennen und verstehst die Unterschiede zwischen den Messarten.

## 📖 Grundlagen der elektrischen Messung

**Messen** bedeutet, eine **unbekannte Größe** mit einer **bekannten Größe** zu vergleichen. In der Elektrotechnik messen wir hauptsächlich **Spannung**, **Strom** und **Widerstand**.

### 🔧 Das Multimeter - dein wichtigstes Werkzeug

Ein **Multimeter** kann verschiedene elektrische Größen messen:
- **V** = Volt (Spannung)
- **A** = Ampere (Strom)  
- **Ω** = Ohm (Widerstand)
- **Zusätzlich:** Frequenz, Kapazität, Temperatur

## ⚡ Spannungsmessung

### Grundprinzip: Parallel messen
```
Schaltung:
+5V ──▭── ──▷┃── ──┴── GND
     220Ω    LED

Spannungsmessung an LED:
+5V ──▭── ──▷┃── ──┴── GND
             │     │
             │  ┌──▼──┐
             └──│  V  │
                └─────┘
               Voltmeter
```

### 📋 Messvorgang Schritt-für-Schritt

1. **Multimeter auf "V" einstellen**
2. **Messbereich wählen** (z.B. 20V für 5V-Schaltung)
3. **Rote Messleitung** an den **höheren Spannungspunkt** (+)
4. **Schwarze Messleitung** an den **niedrigeren Spannungspunkt** (-)
5. **Parallel zum Bauteil** anschließen
6. **Wert ablesen**

### ⚠️ Wichtige Regeln für Spannungsmessung
- **Immer parallel** zum Bauteil
- **Nie in Reihe** schalten
- **Polarität beachten** (rot = +, schwarz = -)
- **Messbereich richtig wählen**

## 🔌 Strommessung

### Grundprinzip: In Reihe messen
```
Schaltung ohne Messung:
+5V ──▭── ──▷┃── ──┴── GND
     220Ω    LED

Strommessung:
+5V ──▭── ┌───┐ ──▷┃── ──┴── GND
     220Ω │ A │    LED
           └───┘
         Amperemeter
```

### 📋 Messvorgang Schritt-für-Schritt

1. **Schaltung ausschalten**
2. **Leitung unterbrechen** (an der Stelle, wo Strom gemessen werden soll)
3. **Multimeter auf "A" einstellen**
4. **Messbereich wählen** (z.B. 200mA für LED-Schaltung)
5. **Multimeter in die unterbrochene Leitung einfügen**
6. **Schaltung einschalten**
7. **Wert ablesen**

### ⚠️ Wichtige Regeln für Strommessung
- **Immer in Reihe** zur Leitung
- **Schaltung ausschalten** vor Umbau
- **Nie parallel** anschließen (Kurzschluss!)
- **Messbereich vorher schätzen**

## 🧮 Praktische Messaufgaben

### Messaufgabe 1: LED-Grundschaltung
```
Gegeben: +5V ──220Ω── ──LED── ──GND

Messungen durchführen:
1. Gesamtspannung: U_ges = _____ V
2. Spannung am Widerstand: U_R = _____ V  
3. Spannung an LED: U_LED = _____ V
4. Strom im Stromkreis: I = _____ mA

Prüfung: U_ges = U_R + U_LED ?
```

### Messaufgabe 2: Mehrere Bauteile
```
Schaltung: +9V ──R1── ──R2── ──LED── ──GND
                470Ω  220Ω

Gesucht:
- Gesamtstrom I = _____ mA
- Spannung an R1: U_R1 = _____ V
- Spannung an R2: U_R2 = _____ V  
- Spannung an LED: U_LED = _____ V
```

## 🔍 Messfehler vermeiden

### Häufige Fehler bei Spannungsmessung

#### Fehler 1: In Reihe messen statt parallel
```
❌ Falsch:
+5V ──▭── ┌───┐ ──▷┃── ──┴── GND
     220Ω │ V │    LED
           └───┘

✅ Richtig:
+5V ──▭── ──▷┃── ──┴── GND
             │     │
           ┌─▼─────▼─┐
           │    V    │
           └─────────┘
```

#### Fehler 2: Falsche Polarität
```
❌ Falsch: Schwarze Leitung an (+), rote an (-)
Result: Negativer Messwert

✅ Richtig: Rote Leitung an (+), schwarze an (-)  
Result: Positiver Messwert
```

### Häufige Fehler bei Strommessung

#### Fehler 1: Parallel messen statt in Reihe
```
❌ Falsch: Amperemeter parallel → Kurzschluss!
+5V ──▭── ──▷┃── ──┴── GND
         │       │
       ┌─▼───────▼─┐
       │     A     │  ← GEFAHR!
       └───────────┘

✅ Richtig: Amperemeter in Reihe
+5V ──▭── ┌───┐ ──▷┃── ──┴── GND
     220Ω │ A │    LED
           └───┘
```

#### Fehler 2: Zu kleinen Messbereich wählen
```
❌ Falsch: 2mA-Bereich für 50mA Strom → Überlastung
✅ Richtig: 200mA-Bereich für 50mA Strom
```

## 📱 Digitale vs. Analoge Messgeräte

### Digitalmultimeter (DMM)
```
Anzeige: [1.234] V
```
**Vorteile:**
- Sehr genau (0,1% Genauigkeit)
- Einfach abzulesen
- Viele Zusatzfunktionen

**Nachteile:**
- Zeigt nur Momentanwert
- Schwankungen schlecht erkennbar

### Analogmultimeter  
```
Anzeige:    ↗
         ─────────
        0    1    2 V
```
**Vorteile:**
- Schwankungen gut sichtbar
- Trends erkennbar
- Robuster

**Nachteile:**
- Weniger genau
- Ablesefehler möglich

## 🔬 Erweiterte Messtechnik

### Oszilloskop - für zeitabhängige Signale
```
Bildschirm:
Spannung ↑
        │   ∩     ∩     ∩
    2V  │  ∩ ∩   ∩ ∩   ∩ ∩
        │ ∩   ∩ ∩   ∩ ∩   ∩
    0V  │────────────────────→ Zeit
        │ │     │     │
        0 1ms   2ms   3ms
```
**Anwendung:** Wechselspannung, Digitalssignale, Störungen

### Stromzange - berührungslose Strommessung
```
        ┌─────────┐
Leiter  ││       ││  Stromzange
 ───────┤│   A   ││ 
        ││       ││
        └─────────┘
```
**Vorteil:** Leitung muss nicht unterbrochen werden

## 🧮 Übung: Messproblem lösen

**Problem:** Ein Computer startet nicht. Du vermutest ein Problem mit der 12V-Leitung.

**Messplan:**
1. **Spannungsmessung am Netzteil-Ausgang:**
   - Soll: 12V
   - Ist: _____ V

2. **Spannungsmessung am Mainboard-Stecker:**
   - Soll: 12V  
   - Ist: _____ V

3. **Strommessung in der 12V-Leitung:**
   - Normal: 2-5A
   - Ist: _____ A

**Diagnose-Matrix:**
| Netzteil | Mainboard | Strom | Diagnose |
|----------|-----------|-------|----------|
| 12V OK | 12V OK | 3A | Alles OK |
| 12V OK | 0V | 0A | Leitungsbruch |
| 12V OK | 6V | 10A | Kurzschluss |
| 0V | 0V | 0A | Netzteil defekt |

## ✅ Selbsttest

**Kreuze die richtigen Antworten an:**

1. **Spannung wird gemessen:**
   - ☐ In Reihe zum Bauteil
   - ☐ Parallel zum Bauteil ✓
   - ☐ Senkrecht zum Bauteil
   - ☐ Vor dem Bauteil

2. **Strom wird gemessen:**
   - ☐ Parallel zur Leitung
   - ☐ In Reihe zur Leitung ✓
   - ☐ Neben der Leitung  
   - ☐ Über der Leitung

3. **Ein Amperemeter parallel geschaltet:**
   - ☐ Misst korrekt
   - ☐ Verursacht Kurzschluss ✓
   - ☐ Zeigt zu hohe Werte
   - ☐ Geht kaputt

## 🎯 Praxistipps

```
Messung vorbereiten:
□ Schaltplan studieren
□ Erwartete Werte abschätzen  
□ Messbereich vorwählen
□ Sicherheit prüfen (Spannung < 50V?)

Während der Messung:
□ Polarität beachten (rot = +)
□ Festen Kontakt sicherstellen
□ Multimeter nicht bewegen
□ Wert notieren

Nach der Messung:
□ Messwert bewerten (sinnvoll?)
□ Mit Erwartung vergleichen
□ Bei Abweichung: Messung wiederholen
□ Messgerät ausschalten
```

## 📝 Merkregeln

```
Spannungsmessung:
□ Parallel zum Bauteil
□ Rot an (+), Schwarz an (-)
□ Schaltung kann eingeschaltet bleiben
□ Hoher Eingangswiderstand des Voltmeters

Strommessung:
□ In Reihe zur Leitung
□ Schaltung für Umbau ausschalten
□ Niedriger Eingangswiderstand des Amperemeters
□ NIEMALS parallel anschließen!

Sicherheit:
□ Bei > 50V: Vorsicht!
□ Bei > 230V: Fachmann rufen!
□ Nie unter Spannung umbauen
□ Messbereich vorher schätzen
```

---

**▶️ Nächste Vertiefung:** [Elektrische Spannung U=W/Q](./07_Elektrische_Spannung_Formel.md)