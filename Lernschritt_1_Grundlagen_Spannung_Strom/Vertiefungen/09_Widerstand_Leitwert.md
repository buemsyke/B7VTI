# Vertiefung: Widerstand und Leitwert (R = 1/G)

## 🎯 Lernziel
Du verstehst die physikalische Bedeutung von Widerstand und Leitwert und kannst mit der Beziehung R = 1/G rechnen.

## 📖 Die Grundbeziehung zwischen Widerstand und Leitwert

**Widerstand** und **Leitwert** sind zueinander **umgekehrt proportional**:

### ⚡ Formeln
- **R = 1/G** (Widerstand = 1 / Leitwert)
- **G = 1/R** (Leitwert = 1 / Widerstand)

**Einheiten:**
- **R** = Widerstand in Ohm [Ω]
- **G** = Leitwert in Siemens [S]

### 🧠 Physikalische Bedeutung
- **Widerstand:** Wie stark ein Material dem Stromfluss **widersteht**
- **Leitwert:** Wie gut ein Material den Strom **leitet**

## 🚰 Analogie: Wasserrohr

```
Enges Rohr (hoher Widerstand):
┌────┐ ← Wenig Wasser fließt durch
│    │   = hoher Widerstand
│    │   = niedriger Leitwert
└────┘

Weites Rohr (niedriger Widerstand):
┌──────────┐ ← Viel Wasser fließt durch
│          │   = niedriger Widerstand  
│          │   = hoher Leitwert
└──────────┘
```

### Elektrische Entsprechung
- **Dünner Draht:** Hoher Widerstand → Niedriger Leitwert
- **Dicker Draht:** Niedriger Widerstand → Hoher Leitwert

## 🧮 Umrechnung zwischen R und G

### Beispiele

| Widerstand R | Berechnung | Leitwert G |
|--------------|------------|------------|
| 1 Ω | G = 1/1 = 1 S | 1 S |
| 10 Ω | G = 1/10 = 0,1 S | 0,1 S |
| 100 Ω | G = 1/100 = 0,01 S | 0,01 S |
| 1000 Ω | G = 1/1000 = 0,001 S | 1 mS |

### Erkenntnis
- **Hoher Widerstand** → **Niedriger Leitwert**
- **Niedriger Widerstand** → **Hoher Leitwert**

## 🔍 Praktisches Beispiel: Kabelwiderstand

### Situation
Du planst die Verkabelung im Rechenzentrum und musst verschiedene Kabel beurteilen:

**Kabel A:** 50m Kupferkabel, 2,5mm² Querschnitt
- **Widerstand:** R = 0,4 Ω
- **Leitwert:** G = 1/0,4 = 2,5 S

**Kabel B:** 50m Kupferkabel, 1,5mm² Querschnitt  
- **Widerstand:** R = 0,7 Ω
- **Leitwert:** G = 1/0,7 = 1,43 S

### Interpretation
- **Kabel A** hat **niedrigeren Widerstand** → **bessere Leitung**
- **Kabel A** hat **höheren Leitwert** → **weniger Verluste**

## 🏢 IT-Anwendung: Parallelschaltung von Widerständen

### Warum ist der Leitwert praktisch?

Bei **Parallelschaltung** addieren sich die **Leitwerte**:
```
     R1 = 10Ω
  ┌─────▭─────┐
  │           │
──┤           ├── 
  │           │
  └─────▭─────┘
     R2 = 15Ω

Gesamtleitwert: G_ges = G1 + G2
G1 = 1/10Ω = 0,1 S
G2 = 1/15Ω = 0,067 S
G_ges = 0,1 + 0,067 = 0,167 S

Gesamtwiderstand: R_ges = 1/G_ges = 1/0,167 = 6Ω
```

### Server-Stromversorgung
```
Server mit mehreren parallelen Stromwegen:

12V ┬─── CPU-Modul (R1 = 2Ω)
    ├─── RAM-Module (R2 = 6Ω)  
    ├─── Festplatten (R3 = 4Ω)
    └─── Lüfter (R4 = 12Ω)

Gesamtleitwert:
G_ges = 1/2 + 1/6 + 1/4 + 1/12
G_ges = 0,5 + 0,167 + 0,25 + 0,083 = 1 S

Gesamtwiderstand: R_ges = 1/1 = 1Ω
```

## 🧮 Übungsaufgaben

### Aufgabe 1: Widerstand → Leitwert
Berechne die Leitwerte folgender Widerstände:

1. **R = 5Ω:** G = 1/5 = _____ S
2. **R = 20Ω:** G = 1/20 = _____ S = _____ mS
3. **R = 1kΩ:** G = 1/1000 = _____ S = _____ mS

### Aufgabe 2: Leitwert → Widerstand  
Berechne die Widerstände folgender Leitwerte:

1. **G = 0,2S:** R = 1/0,2 = _____ Ω
2. **G = 50mS:** R = 1/0,05 = _____ Ω
3. **G = 2mS:** R = 1/0,002 = _____ Ω

### Aufgabe 3: Parallelschaltung
Drei Widerstände sind parallel geschaltet:
- R1 = 6Ω
- R2 = 12Ω  
- R3 = 4Ω

**Berechne:**
1. **G1 = _____ S, G2 = _____ S, G3 = _____ S**
2. **G_ges = G1 + G2 + G3 = _____ S**
3. **R_ges = 1/G_ges = _____ Ω**

## 🔬 Materialien und ihre Eigenschaften

### Leiter (niederer Widerstand, hoher Leitwert)

| Material | Spez. Widerstand | Anwendung IT |
|----------|------------------|--------------|
| **Silber** | 0,016 Ω⋅mm²/m | Hochfrequenz-Kabel |
| **Kupfer** | 0,017 Ω⋅mm²/m | Standard-Kabel, Platinen |
| **Aluminium** | 0,028 Ω⋅mm²/m | Billige Kabel |
| **Gold** | 0,022 Ω⋅mm²/m | Kontakte (korrosionsbeständig) |

### Halbleiter (mittlerer Widerstand)

| Material | Besonderheit | Anwendung IT |
|----------|--------------|--------------|
| **Silizium** | Widerstand steuerbar | Prozessoren, Speicher |
| **Germanium** | Temperaturabhängig | Dioden |

### Isolatoren (hoher Widerstand, niedriger Leitwert)

| Material | Spez. Widerstand | Anwendung IT |
|----------|------------------|--------------|
| **Glas** | 10¹²-10¹⁴ Ω⋅mm²/m | Isolation |
| **Kunststoff** | 10¹⁰-10¹⁶ Ω⋅mm²/m | Kabelisolation |
| **Keramik** | 10¹²-10¹⁵ Ω⋅mm²/m | IC-Substrate |

## ⚡ Temperaturabhängigkeit

### Kaltleiter (PTC - Positive Temperature Coefficient)
```
Widerstand ↑
           │    ┌────
           │   ╱
           │  ╱
           │ ╱
           └──────────→ Temperatur
```
**Beispiel:** Glühlampe
- **Kalt:** 20Ω (niedriger Widerstand)
- **Heiß:** 200Ω (hoher Widerstand)

### Heißleiter (NTC - Negative Temperature Coefficient)
```
Widerstand ↑
           │ ────╲
           │      ╲
           │       ╲
           │        ╲___
           └──────────────→ Temperatur
```
**Beispiel:** Temperatursensor
- **Kalt:** 10kΩ (hoher Widerstand)
- **Heiß:** 1kΩ (niedriger Widerstand)

## 🔍 Messungen: Widerstand vs. Leitwert

### Multimeter-Messung
```
Widerstandsmessung (Ω-Bereich):
Multimeter zeigt direkt: R = 47Ω

Leitwert berechnen:
G = 1/R = 1/47Ω = 0,021 S = 21mS
```

### Strom-Spannungs-Messung
```
Gegeben: U = 12V, I = 2A

Widerstand: R = U/I = 12V/2A = 6Ω
Leitwert: G = I/U = 2A/12V = 0,167 S
```

## 🧮 Erweiterte Anwendung: Spannungsteiler

### Spannungsteiler mit Leitwerten berechnen
```
Eingangsspannung: 12V
        │
      ┌─┴─┐ R1 = 4Ω → G1 = 0,25 S
      └─┬─┘
    UT  │  ← Teilspannung
      ┌─┴─┐ R2 = 8Ω → G2 = 0,125 S  
      └─┬─┘
        ⏚

Spannungsteiler-Formel mit Leitwerten:
UT = U_ein × (G2/(G1+G2))
UT = 12V × (0,125/(0,25+0,125))
UT = 12V × (0,125/0,375) = 12V × 1/3 = 4V
```

## ✅ Selbsttest

**Kreuze die richtigen Antworten an:**

1. **Ein Widerstand von 10Ω hat einen Leitwert von:**
   - ☐ 10 S
   - ☐ 0,1 S ✓
   - ☐ 1 S
   - ☐ 100 S

2. **Hoher Leitwert bedeutet:**
   - ☐ Hoher Widerstand
   - ☐ Niedriger Widerstand ✓
   - ☐ Hohe Spannung
   - ☐ Hoher Strom

3. **Die Einheit des Leitwerts ist:**
   - ☐ Ohm (Ω)
   - ☐ Siemens (S) ✓
   - ☐ Volt (V)
   - ☐ Ampere (A)

4. **Bei Parallelschaltung addieren sich:**
   - ☐ Die Widerstände
   - ☐ Die Leitwerte ✓
   - ☐ Die Spannungen
   - ☐ Die Kapazitäten

## 🎯 Lösungen

### Aufgabe 1:
1. **G = 1/5 = 0,2 S**
2. **G = 1/20 = 0,05 S = 50 mS**
3. **G = 1/1000 = 0,001 S = 1 mS**

### Aufgabe 2:
1. **R = 1/0,2 = 5 Ω**
2. **R = 1/0,05 = 20 Ω**
3. **R = 1/0,002 = 500 Ω**

### Aufgabe 3:
1. **G1 = 1/6 = 0,167 S, G2 = 1/12 = 0,083 S, G3 = 1/4 = 0,25 S**
2. **G_ges = 0,167 + 0,083 + 0,25 = 0,5 S**
3. **R_ges = 1/0,5 = 2 Ω**

## 📝 Merkregeln

```
Grundbeziehung:
□ R = 1/G (Widerstand = 1/Leitwert)
□ G = 1/R (Leitwert = 1/Widerstand)
□ Einheiten: R in Ω, G in S (Siemens)

Physikalische Bedeutung:
□ Hoher Widerstand = niederer Leitwert
□ Niederer Widerstand = hoher Leitwert
□ Widerstand = "Bremse" für Strom
□ Leitwert = "Durchlass" für Strom

Praktische Anwendung:
□ Parallelschaltung: G_ges = G1 + G2 + G3 + ...
□ Materialien: Leiter (niedriger R), Isolatoren (hoher R)
□ Temperatur beeinflusst Widerstand
□ Leitwert praktisch bei Parallelschaltungen

Merkhilfe:
□ 1 Ω ↔ 1 S
□ 10 Ω ↔ 0,1 S  
□ 100 Ω ↔ 0,01 S
□ 1000 Ω ↔ 1 mS
```

---

**▶️ Nächste Vertiefung:** [Einheiten](./10_Einheiten.md)