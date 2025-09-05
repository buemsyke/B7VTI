# Vertiefung: Einheiten

## 🎯 Lernziel
Du lernst die wichtigsten elektrischen Einheiten kennen und verstehst das internationale Einheitensystem (SI).

## 📖 Das SI-Einheitensystem

Das **Internationale Einheitensystem (SI)** sorgt weltweit für einheitliche Messungen. Alle elektrischen Einheiten sind aus **Grundeinheiten** abgeleitet.

### 🏗️ SI-Grundeinheiten (wichtig für Elektrotechnik)

| Größe | Grundeinheit | Symbol | Beschreibung |
|-------|--------------|---------|--------------|
| **Zeit** | Sekunde | s | Dauer eines Vorgangs |
| **Länge** | Meter | m | Entfernung |
| **Masse** | Kilogramm | kg | Stoffmenge |
| **Stromstärke** | Ampere | A | **Einzige elektrische Grundeinheit** |

### ⚡ Abgeleitete elektrische Einheiten

Alle anderen elektrischen Einheiten werden aus den Grundeinheiten **berechnet**:

| Größe | Einheit | Symbol | Ableitung aus Grundeinheiten |
|-------|---------|--------|------------------------------|
| **Spannung** | Volt | V | kg⋅m²/(A⋅s³) |
| **Widerstand** | Ohm | Ω | kg⋅m²/(A²⋅s³) |
| **Leistung** | Watt | W | kg⋅m²/s³ |
| **Energie** | Joule | J | kg⋅m²/s² |
| **Ladung** | Coulomb | C | A⋅s |
| **Leitwert** | Siemens | S | A²⋅s³/(kg⋅m²) |

## 🔧 Wichtige elektrische Einheiten im Detail

### Stromstärke (Ampere) - die Grundeinheit
```
Definition: 1 Ampere
= 1 Coulomb Ladung pro Sekunde
= 6,24 × 10¹⁸ Elektronen pro Sekunde

Symbol: A
Benannt nach: André-Marie Ampère (französischer Physiker)
```

### Spannung (Volt)
```
Definition: 1 Volt
= 1 Joule Energie pro 1 Coulomb Ladung
= 1 Watt Leistung bei 1 Ampere Strom

Symbol: V
Benannt nach: Alessandro Volta (italienischer Physiker)
Formel: U = W/Q = P/I
```

### Widerstand (Ohm)
```
Definition: 1 Ohm
= 1 Volt Spannung bei 1 Ampere Strom

Symbol: Ω (griechischer Buchstabe Omega)
Benannt nach: Georg Simon Ohm (deutscher Physiker)
Formel: R = U/I
```

### Leistung (Watt)
```
Definition: 1 Watt
= 1 Joule Energie pro 1 Sekunde
= 1 Volt × 1 Ampere

Symbol: W
Benannt nach: James Watt (schottischer Erfinder)
Formel: P = U × I = W/t
```

## 🧮 Einheiten umrechnen

### Grundregeln der Umrechnung
1. **Formel korrekt anwenden**
2. **Einheiten mitrechnen**  
3. **Ergebnis auf Plausibilität prüfen**

### Beispiel: Ohmsches Gesetz
```
Gegeben: U = 12V, R = 4Ω
Gesucht: I = ?

Formel: I = U/R
Einsetzen: I = 12V/4Ω = 3 V/Ω

Einheit prüfen: V/Ω = (kg⋅m²/(A⋅s³))/(kg⋅m²/(A²⋅s³))
                    = kg⋅m²/(A⋅s³) × A²⋅s³/(kg⋅m²)  
                    = A ✓

Ergebnis: I = 3A
```

## 🔍 Praktische IT-Beispiele

### USB-Spezifikationen
```
USB 2.0: 5V, 0,5A → P = U × I = 5V × 0,5A = 2,5W
USB 3.0: 5V, 0,9A → P = U × I = 5V × 0,9A = 4,5W  
USB-C:   5V, 3A   → P = U × I = 5V × 3A = 15W

Alle Einheiten stimmen: V × A = W ✓
```

### Netzteil-Effizienz
```
Eingagsleistung: 230V × 2A = 460W
Ausgangsleistung: 12V × 35A = 420W

Wirkungsgrad: η = P_aus/P_ein = 420W/460W = 0,91 = 91%

Einheitenprüfung: W/W = dimensionslos ✓
```

### Akku-Energie
```
Laptop-Akku: 14,8V, 4,4Ah

Energie: W = U × Q = U × I × t
        W = 14,8V × 4,4Ah = 65,12Wh

Umrechnung in Joule:
W = 65,12Wh = 65,12 × 3600s = 234.432 Ws = 234.432 J
```

## 🧮 Übungsaufgaben mit Einheiten

### Aufgabe 1: Einheiten prüfen
Prüfe, ob diese Berechnungen dimensionsrichtig sind:

1. **P = U²/R**
   - U in V, R in Ω
   - V²/Ω = ? → **_____ (richtig/falsch)**

2. **W = I²×R×t**  
   - I in A, R in Ω, t in s
   - A²×Ω×s = ? → **_____ (richtig/falsch)**

3. **Q = C×U**
   - C in F (Farad), U in V
   - F×V = ? → **_____ (richtig/falsch)**

### Aufgabe 2: Umrechnung mit Einheiten
```
Gegeben: Widerstand R = 470Ω, Strom I = 25mA
Gesucht: Spannung U, Leistung P

Berechnung:
U = R × I = 470Ω × 0,025A = _____ V
P = U × I = _____ V × 0,025A = _____ W
```

### Aufgabe 3: Energie berechnen
```
Server-Verbrauch: 800W für 24h
Strompreis: 0,30€/kWh

Energie: W = P × t = 800W × 24h = _____ Wh = _____ kWh
Kosten = _____ kWh × 0,30€/kWh = _____ €
```

## 📊 Einheiten-Tabelle für IT-Systeme

### Spannungen in IT-Systemen
| System | Spannung | Einheit | Anwendung |
|--------|----------|---------|-----------|
| **CMOS** | 3 | V | BIOS-Batterie |
| **USB 2.0** | 5 | V | Peripherie |
| **Laptop** | 19 | V | Netzteil |
| **Server** | 12 | V | Hauptversorgung |
| **Rechenzentrum** | 400 | V | Hauptverteilung |

### Ströme in IT-Systemen  
| Gerät | Strom | Einheit | Leistung |
|-------|-------|---------|----------|
| **LED** | 20 | mA | 0,04 W |
| **Smartphone** | 2 | A | 10 W |
| **Laptop** | 3,5 | A | 65 W |
| **Desktop-PC** | 8 | A | 200 W |
| **Server** | 50 | A | 600 W |

### Energieverbräuche
| Gerät | Energie/Tag | Einheit | Kosten/Jahr |
|-------|-------------|---------|-------------|
| **Smartphone** | 0,05 | kWh | 5€ |
| **Laptop** | 1,5 | kWh | 160€ |
| **Desktop-PC** | 4,8 | kWh | 525€ |
| **Server** | 14,4 | kWh | 1.575€ |

## 🔬 Präzision und Messgenauigkeit

### Signifikante Stellen
```
Messwert: 12,34V
→ 4 signifikante Stellen
→ Genauigkeit: ±0,01V

Berechnung: P = U²/R = (12,34V)²/100Ω
P = 152,3756W/100Ω = 1,523756W

Rundung auf 4 Stellen: P = 1,524W
```

### Messgenauigkeit berücksichtigen
```
Multimeter-Angabe: "±0,5% + 3 Digits"
Messwert: 12,34V

Fehler = 0,5% × 12,34V + 0,003V = 0,062V + 0,003V = 0,065V
Ergebnis: U = 12,34V ± 0,065V = (12,275...12,405)V
```

## ⚠️ Häufige Einheitenfehler

### Fehler 1: Vorsätze vergessen
```
❌ Falsch: I = 25mA → I = 25A in Formel einsetzen
✅ Richtig: I = 25mA = 0,025A in Formel einsetzen
```

### Fehler 2: Einheiten nicht prüfen
```
❌ Falsch: P = I×R = 2A × 10Ω = 20W (Formel falsch!)
✅ Richtig: P = I²×R = (2A)² × 10Ω = 40W
```

### Fehler 3: Zeit-Einheiten verwechseln
```
❌ Falsch: W = P×t = 100W × 2h = 200J (Einheit falsch!)
✅ Richtig: W = P×t = 100W × 2h = 200Wh = 720.000J
```

## ✅ Selbsttest

**Kreuze die richtigen Antworten an:**

1. **Die Grundeinheit der Stromstärke ist:**
   - ☐ Volt (V)
   - ☐ Ampere (A) ✓
   - ☐ Watt (W)
   - ☐ Ohm (Ω)

2. **1 Watt entspricht:**
   - ☐ 1 V × 1 Ω
   - ☐ 1 V × 1 A ✓
   - ☐ 1 A × 1 Ω
   - ☐ 1 V ÷ 1 A

3. **Die Einheit Siemens (S) steht für:**
   - ☐ Spannung
   - ☐ Strom
   - ☐ Widerstand
   - ☐ Leitwert ✓

4. **Bei P = U²/R sind die Einheiten:**
   - ☐ V²/Ω = W ✓
   - ☐ V²/Ω = A
   - ☐ V²/Ω = V
   - ☐ V²/Ω = Ω

## 🎯 Lösungen

### Aufgabe 1:
1. **V²/Ω = (kg⋅m²/(A⋅s³))²/(kg⋅m²/(A²⋅s³)) = kg⋅m²/s³ = W → richtig**
2. **A²×Ω×s = A²×(kg⋅m²/(A²⋅s³))×s = kg⋅m²/s² = J → richtig**
3. **F×V = (A²⋅s⁴/(kg⋅m²))×(kg⋅m²/(A⋅s³)) = A⋅s = C → richtig**

### Aufgabe 2:
**U = 470Ω × 0,025A = 11,75V**
**P = 11,75V × 0,025A = 0,294W**

### Aufgabe 3:
**W = 800W × 24h = 19.200Wh = 19,2kWh**
**Kosten = 19,2kWh × 0,30€/kWh = 5,76€**

## 📝 Merkregeln

```
SI-Grundlagen:
□ Ampere (A) = einzige elektrische Grundeinheit
□ Alle anderen sind abgeleitet: V, Ω, W, J, C, S
□ Formeln immer mit Einheiten rechnen
□ Einheitenprüfung verhindert Fehler

Wichtige Einheiten:
□ U in Volt (V) = kg⋅m²/(A⋅s³)
□ I in Ampere (A) = Grundeinheit
□ R in Ohm (Ω) = kg⋅m²/(A²⋅s³)  
□ P in Watt (W) = kg⋅m²/s³
□ W in Joule (J) = kg⋅m²/s²

Umrechnung:
□ Vorsätze beachten (mA → A)
□ Einheiten mitrechnen
□ Ergebnis prüfen (sinnvoll?)
□ Signifikante Stellen beachten

Häufige IT-Einheiten:
□ Spannung: 3V (CMOS) bis 400V (Rechenzentrum)
□ Strom: mA (LED) bis A (Server)
□ Leistung: mW (LED) bis kW (Server)
□ Energie: Wh (Akku) bis kWh (Verbrauch)
```

---

**▶️ Nächste Vertiefung:** [Einheitenvorsätze](./11_Einheitenvorsaetze.md)