# Vertiefung: Einheitenvorsätze

## 🎯 Lernziel
Du lernst die wichtigsten Einheitenvorsätze (Präfixe) kennen und kannst sicher zwischen verschiedenen Größenordnungen umrechnen.

## 📖 Was sind Einheitenvorsätze?

**Einheitenvorsätze** (auch **Präfixe** genannt) sind Abkürzungen für **Zehnerpotenzen**. Sie machen große und kleine Zahlen einfacher lesbar und handlicher.

### 💡 Warum brauchen wir Vorsätze?

**Ohne Vorsätze:**
- Smartphone-Akku: 11.100.000.000 mWh
- WLAN-Frequenz: 2.400.000.000 Hz
- LED-Strom: 0,000.020 A

**Mit Vorsätzen:**
- Smartphone-Akku: 11,1 Wh  
- WLAN-Frequenz: 2,4 GHz
- LED-Strom: 20 mA

## 📏 Die wichtigsten Vorsätze für IT-Systeme

### Kleine Werte (Bruchteile)

| Vorsatz | Symbol | Faktor | Zehnerpotenz | Beispiel IT |
|---------|--------|--------|---------------|-------------|
| **Milli** | m | 0,001 | 10⁻³ | 20 mA (LED-Strom) |
| **Mikro** | μ | 0,000001 | 10⁻⁶ | 10 μA (CMOS-Strom) |
| **Nano** | n | 0,000000001 | 10⁻⁹ | 45 nm (CPU-Strukturen) |
| **Piko** | p | 0,000000000001 | 10⁻¹² | 100 pF (Kondensator) |

### Große Werte (Vielfache)

| Vorsatz | Symbol | Faktor | Zehnerpotenz | Beispiel IT |
|---------|--------|--------|---------------|-------------|
| **Kilo** | k | 1.000 | 10³ | 5 kV (Hochspannung) |
| **Mega** | M | 1.000.000 | 10⁶ | 2,4 GHz (WLAN) |
| **Giga** | G | 1.000.000.000 | 10⁹ | 16 GB (RAM) |
| **Tera** | T | 1.000.000.000.000 | 10¹² | 2 TB (Festplatte) |

## 🧮 Umrechnung zwischen Vorsätzen

### Grundregeln
1. **Von größerem zu kleinerem Vorsatz:** × 1000
2. **Von kleinerem zu größerem Vorsatz:** ÷ 1000
3. **Kommastelle verschieben:** 3 Stellen pro Vorsatz-Sprung

### Umrechnungsbeispiele

#### Von mA zu A (kleiner → größer)
```
25 mA = ? A
mA → A: ÷ 1000
25 mA = 25 ÷ 1000 = 0,025 A
```

#### Von V zu kV (groß → größer)  
```
2300 V = ? kV
V → kV: ÷ 1000  
2300 V = 2300 ÷ 1000 = 2,3 kV
```

#### Von μA zu mA (klein → größer)
```
500 μA = ? mA
μA → mA: ÷ 1000
500 μA = 500 ÷ 1000 = 0,5 mA
```

## 🔍 Praktische IT-Beispiele

### Smartphone-Spezifikationen
```
Original-Datenblatt:
- Prozessor: 2800000000 Hz
- RAM: 8192 MB  
- Akku: 4000 mAh
- Display: 0,000440 m

Mit Vorsätzen:
- Prozessor: 2,8 GHz
- RAM: 8 GB (= 8192 MB)
- Akku: 4 Ah (= 4000 mAh)  
- Display: 6,7" (= 0,17 m)
```

### Server-Stromversorgung
```
Netzteil-Angaben:
- Eingangsspannung: 230000 mV = 230 V
- Ausgangsstrom: 41700 mA = 41,7 A  
- Leistung: 1200000 mW = 1200 W = 1,2 kW
- Effizienz: 0,92 = 92%
```

### Netzwerk-Geschwindigkeiten
```
Internet-Anschlüsse:
- DSL: 50.000.000 bit/s = 50 Mbit/s
- Glasfaser: 1.000.000.000 bit/s = 1 Gbit/s
- 5G: 10.000.000.000 bit/s = 10 Gbit/s
```

## 🧮 Übungsaufgaben

### Aufgabe 1: Umrechnung nach A (Ampere)
Rechne alle Werte in Ampere um:

1. **150 mA = _____ A**
2. **2,5 kA = _____ A**  
3. **750 μA = _____ A**
4. **0,05 A = _____ mA**

### Aufgabe 2: Umrechnung nach V (Volt)
Rechne alle Werte in Volt um:

1. **12 kV = _____ V**
2. **3300 mV = _____ V**
3. **0,5 MV = _____ V**
4. **230 V = _____ kV**

### Aufgabe 3: Gemischte Umrechnung
Führe die gewünschten Umrechnungen durch:

1. **2,4 GHz = _____ MHz**
2. **1000 pF = _____ nF**
3. **5 TB = _____ GB**  
4. **45 nm = _____ μm**

### Aufgabe 4: IT-Praxis
Berechne die fehlenden Werte:

```
USB-C Netzteil:
- Spannung: 20 V = _____ mV
- Strom: 4,5 A = _____ mA  
- Leistung: 90 W = _____ mW

WLAN-Router:
- Frequenz: 5800 MHz = _____ GHz
- Sendeleistung: 20000 mW = _____ W
- Reichweite: 0,05 km = _____ m
```

## 🔬 Vorsätze in verschiedenen IT-Bereichen

### Prozessortechnologie
```
CPU-Strukturbreiten:
- 1995: 350 nm = 0,35 μm
- 2005: 90 nm = 0,09 μm  
- 2015: 14 nm = 0,014 μm
- 2025: 2 nm = 0,002 μm

Trend: Immer kleinere Strukturen!
```

### Speicherkapazitäten
```
Entwicklung über die Jahre:
- 1980: 64 kB Diskette
- 1990: 1,44 MB Diskette  
- 2000: 700 MB CD
- 2010: 8 GB USB-Stick
- 2020: 2 TB SSD
- 2030: 128 TB (geplant)

Pro Dekade: Faktor 1000 mehr Speicher!
```

### Netzwerk-Bandbreiten
```
Internet-Evolution:
- 1990: 56 kbit/s (Modem)
- 2000: 1 Mbit/s (DSL)
- 2010: 100 Mbit/s (Kabel)  
- 2020: 1 Gbit/s (Glasfaser)
- 2030: 100 Gbit/s (geplant)

Jede Dekade: ~1000-fache Steigerung
```

## ⚡ Vorsätze bei Energieberechnungen

### Smartphone-Akku analysieren
```
Gegeben: 3,7V, 4000 mAh

Schritt 1: In Grundeinheiten umrechnen
Q = 4000 mAh = 4 Ah = 4 × 3600 s × A = 14.400 As = 14.400 C

Schritt 2: Energie berechnen  
W = U × Q = 3,7V × 14.400 C = 53.280 J

Schritt 3: In praktische Einheit umrechnen
W = 53.280 J = 53.280 Ws = 53.280/3600 Wh = 14,8 Wh
```

### Rechenzentrum-Verbrauch
```
Server-Rack: 42 Server à 800W = 33.600 W = 33,6 kW

Tagesverbrauch:
W = P × t = 33,6 kW × 24h = 806,4 kWh

Jahresverbrauch:  
W = 806,4 kWh × 365 = 294.336 kWh ≈ 294 MWh

Kosten (0,15€/kWh):
Kosten = 294.336 kWh × 0,15€ = 44.150€
```

## 🔍 Digitale vs. analoge Vorsätze

### Binäre Vorsätze (2er-Potenzen)
```
Speicher verwendet binäre Vorsätze:
- 1 Kibi (Ki) = 1024 = 2¹⁰
- 1 Mebi (Mi) = 1.048.576 = 2²⁰  
- 1 Gibi (Gi) = 1.073.741.824 = 2³⁰

Beispiel:
8 GB RAM = 8 × 10⁹ Byte = 7,45 GiB
(Unterschied: ~7% weniger!)
```

### Dezimale Vorsätze (10er-Potenzen)
```
Netzwerk und Frequenzen verwenden dezimale Vorsätze:
- 1 kbit/s = 1000 bit/s = 10³ bit/s
- 1 Mbit/s = 1.000.000 bit/s = 10⁶ bit/s
- 1 Gbit/s = 1.000.000.000 bit/s = 10⁹ bit/s
```

## ⚠️ Häufige Fehler vermeiden

### Fehler 1: Falsche Umrechnungsrichtung
```
❌ Falsch: 50 mA → A: 50 × 1000 = 50.000 A
✅ Richtig: 50 mA → A: 50 ÷ 1000 = 0,05 A
```

### Fehler 2: Symbol verwechseln
```
❌ Falsch: μ (Mikro) und m (Milli) verwechseln
✅ Richtig: 
   - μ = 10⁻⁶ (Mikro)
   - m = 10⁻³ (Milli)  
   - M = 10⁶ (Mega)
```

### Fehler 3: Binär/Dezimal verwechseln
```
❌ Falsch: 1 GB = 1024 MB (das wäre 1 GiB!)
✅ Richtig: 1 GB = 1000 MB (dezimal)
```

## ✅ Selbsttest

**Kreuze die richtigen Antworten an:**

1. **1000 mA entspricht:**
   - ☐ 0,001 A
   - ☐ 1 A ✓
   - ☐ 10 A
   - ☐ 1000 A

2. **Das Symbol μ steht für:**
   - ☐ Milli (10⁻³)
   - ☐ Mikro (10⁻⁶) ✓
   - ☐ Mega (10⁶)
   - ☐ Nano (10⁻⁹)

3. **2,5 kV entspricht:**
   - ☐ 250 V
   - ☐ 2500 V ✓
   - ☐ 25000 V
   - ☐ 0,25 V

4. **1 GHz entspricht:**
   - ☐ 1000 MHz ✓
   - ☐ 100 MHz  
   - ☐ 10 MHz
   - ☐ 1 MHz

## 🎯 Lösungen

### Aufgabe 1:
1. **150 mA = 0,15 A**
2. **2,5 kA = 2500 A**
3. **750 μA = 0,00075 A**
4. **0,05 A = 50 mA**

### Aufgabe 2:
1. **12 kV = 12.000 V**
2. **3300 mV = 3,3 V**
3. **0,5 MV = 500.000 V**  
4. **230 V = 0,23 kV**

### Aufgabe 3:
1. **2,4 GHz = 2400 MHz**
2. **1000 pF = 1 nF**
3. **5 TB = 5000 GB**
4. **45 nm = 0,045 μm**

### Aufgabe 4:
```
USB-C: 20 V = 20.000 mV, 4,5 A = 4500 mA, 90 W = 90.000 mW
WLAN: 5800 MHz = 5,8 GHz, 20000 mW = 20 W, 0,05 km = 50 m
```

## 📝 Merkregeln

```
Wichtige Vorsätze:
□ m = Milli = 10⁻³ = 0,001
□ μ = Mikro = 10⁻⁶ = 0,000001
□ k = Kilo = 10³ = 1.000
□ M = Mega = 10⁶ = 1.000.000
□ G = Giga = 10⁹ = 1.000.000.000

Umrechnung:
□ Klein → Groß: ÷ 1000 (pro Vorsatz-Sprung)
□ Groß → Klein: × 1000 (pro Vorsatz-Sprung)
□ Kommastelle: 3 Stellen pro Sprung verschieben

IT-Besonderheiten:
□ Speicher: oft binäre Vorsätze (1024)
□ Netzwerk: dezimale Vorsätze (1000)
□ Prozessor: nm-Strukturen (Nano)
□ Frequenz: GHz-Bereich (Giga)

Merkhilfe:
□ mA → A: durch 1000
□ kV → V: mal 1000  
□ GHz → MHz: mal 1000
□ μA → mA: durch 1000
```

---

**▶️ Nächste Vertiefung:** [Runden und Fehlerrechnung](./12_Runden_Fehlerrechnung.md)