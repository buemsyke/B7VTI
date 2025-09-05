# Vertiefung: Stromstärke und Ladung (I = Q/t)

## 🎯 Lernziel
Du verstehst die physikalische Definition des Stroms und kannst mit der Formel I = Q/t rechnen.

## 📖 Die Grundformel des Stroms

**Stromstärke** ist definiert als **Ladung pro Zeit**:

### ⚡ Formel: I = Q/t

- **I** = Stromstärke in Ampere [A]
- **Q** = Ladung in Coulomb [C]
- **t** = Zeit in Sekunden [s]

### 🧠 Physikalische Bedeutung
**Strom** gibt an, wie viel **Ladung** pro **Sekunde** durch einen Leiterquerschnitt fließt.

## 🌊 Analogie: Wasserfluss

```
Wasserstrom in einem Rohr:

   ┌─────────────────────────────────┐
   │ ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← │ Wasser fließt
   └─────────────────────────────────┘
            │
            ▼
   "Pro Sekunde fließen 5 Liter Wasser"
   
Elektrischer Strom:
   
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Leiter
   ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← Elektronen fließen
            │
            ▼
   "Pro Sekunde fließt 1 Coulomb Ladung" = 1 Ampere
```

## 🔬 Was ist 1 Ampere?

### Definition
**1 Ampere = 1 Coulomb pro Sekunde**

### Größenordnung verstehen
```
1 Coulomb = 6.241.000.000.000.000.000 Elektronen!
           (≈ 6,24 × 10¹⁸ Elektronen)

1 Ampere = 6,24 × 10¹⁸ Elektronen pro Sekunde
```

**Das ist eine unvorstellbar große Anzahl!** Selbst bei kleinen Strömen bewegen sich Milliarden von Elektronen.

## 🧮 Formel umstellen und rechnen

### Alle drei Formelformen
1. **I = Q ÷ t** (Strom berechnen)
2. **Q = I × t** (Ladung berechnen)
3. **t = Q ÷ I** (Zeit berechnen)

### Wichtige Einheiten
- **Ladung Q:**
  - 1 C = 1 As (Amperesekunde)
  - 1 Ah = 3600 As = 3600 C
- **Zeit t:**
  - 1 min = 60 s
  - 1 h = 3600 s

## 🔍 Praktisches Beispiel: Smartphone laden

### Gegeben
- **Ladestrom:** 2A
- **Ladezeit:** 1,5 Stunden
- **Gesucht:** Übertragene Ladung

### Rechnung
**Q = I × t = 2A × (1,5 × 3600s) = 2A × 5400s = 10.800 C**

**In Ah umrechnen:**
**Q = 10.800 C ÷ 3600 = 3 Ah**

### Interpretation
Beim Laden wurden **3 Ah** (= 10.800 Coulomb) Ladung in den Akku "hineingeschoben".

## 🏢 IT-Anwendung: Serverraum-Stromanalyse

### Szenario
Ein Server zieht konstant 5A aus der 12V-Leitung.

### Aufgaben

**Aufgabe 1: Ladung pro Tag**
- **t = 24h = 86.400s**
- **Q = I × t = 5A × 86.400s = 432.000 C = 120 Ah**

**Aufgabe 2: Anzahl Elektronen pro Tag**
- **Anzahl = Q × 6,24 × 10¹⁸**
- **Anzahl = 432.000 × 6,24 × 10¹⁸ = 2,7 × 10²⁴ Elektronen**

**Das ist eine 27 mit 23 Nullen!**

## 🔋 Batterieentladung verstehen

### Akku-Kapazität und Entladestrom

```
Smartphone-Akku: 3000mAh = 3Ah

Verschiedene Entladeströme:
┌─────────────────────────────────────────┐
│ Anwendung    │ Strom │ Laufzeit          │
├─────────────────────────────────────────┤
│ Standby      │ 0,01A │ 3Ah÷0,01A = 300h │
│ Surfen       │ 0,5A  │ 3Ah÷0,5A = 6h    │
│ Gaming       │ 1,5A  │ 3Ah÷1,5A = 2h    │
│ Video+GPS    │ 3A    │ 3Ah÷3A = 1h      │
└─────────────────────────────────────────┘
```

### Entlade-Kurve
```
Akkukapazität
     ↑
100% ┃────┐
     ┃    │ Standby (wenig Strom)
 50% ┃    └─────────────────────┐
     ┃                         └────┐
  0% ┃─────────────────────────────────→ Zeit
     0     10h    20h    30h    40h
     
     ┃────┐ Gaming (viel Strom)  
 50% ┃    └────┐
     ┃         └────┐
  0% ┃─────────────────→ Zeit
     0    1h   2h   3h
```

## 🧮 Übungsaufgaben

### Aufgabe 1: LED-Strom berechnen
Durch eine LED fließen in 10 Minuten 12 Coulomb Ladung.

**Gesucht:** Stromstärke I = ?
- **I = Q ÷ t = 12C ÷ 600s = _____ A = _____ mA**

### Aufgabe 2: USB-Ladevorgang
Ein USB-Port liefert 2,5A für 2 Stunden.

**Gesucht:**
1. **Übertragene Ladung:** Q = _____ C = _____ Ah
2. **Anzahl Elektronen:** N = _____ × 10¹⁸

### Aufgabe 3: Festplatte analysieren
Eine Festplatte zieht 1,2A beim Start für 5 Sekunden, dann 0,6A im Dauerbetrieb.

**Gesucht für 1 Stunde Betrieb:**
1. **Ladung beim Start:** Q₁ = _____ C
2. **Ladung im Dauerbetrieb (3595s):** Q₂ = _____ C  
3. **Gesamtladung:** Q_ges = _____ C

### Aufgabe 4: Kondensator entladen
Ein Kondensator entlädt sich in 0,1s mit 50mA.

**Gesucht:** Gespeicherte Ladung Q = _____ C

## 🔬 Stromdichte verstehen

### Was passiert im Leiter?
```
Dicker Leiter (großer Querschnitt):
┌──────────────────────────────────────┐
│ ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← │ 
│ ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← │ Mehr Platz
│ ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← │ für Elektronen
└──────────────────────────────────────┘
→ Wenig Widerstand, wenig Wärme

Dünner Leiter (kleiner Querschnitt):  
┌────────────┐
│ ← ← ← ← ← ← │ Wenig Platz für Elektronen
└────────────┘
→ Mehr Widerstand, mehr Wärme
```

### Stromdichte J = I/A
- **J** = Stromdichte in A/mm²
- **I** = Strom in A
- **A** = Leiterquerschnitt in mm²

**Faustregel:** Kupferleitungen sollten max. 2-3 A/mm² belastet werden.

## ⚡ Stromarten unterscheiden

### Gleichstrom (DC)
```
Strom ↑
      │ ────────────────────── konstant
      │
    0 └─────────────────────────────→ Zeit
```
**Beispiele:** Batterie, USB, Netzteil-Ausgang

### Wechselstrom (AC)
```
Strom ↑
      │   ∩       ∩       ∩
      │  ∩ ∩     ∩ ∩     ∩ ∩
    0 ├─────────────────────────────→ Zeit
      │ ∪   ∪   ∪   ∪   ∪   ∪
      │  ∪ ∪     ∪ ∪     ∪ ∪
```
**Beispiele:** Netzstrom 230V, Transformator-Eingang

### Impulsstrom
```
Strom ↑
      │ ┌┐    ┌┐    ┌┐    ┌┐
      │ ││    ││    ││    ││
    0 └─┘└────┘└────┘└────┘└────→ Zeit
```
**Beispiele:** Schaltnetzteile, Prozessortakt

## ✅ Selbsttest

**Kreuze die richtigen Antworten an:**

1. **Die Formel I = Q/t bedeutet:**
   - ☐ Strom ist Spannung pro Zeit
   - ☐ Strom ist Ladung pro Zeit ✓
   - ☐ Strom ist Widerstand pro Zeit
   - ☐ Strom ist Energie pro Zeit

2. **1 Ampere entspricht:**
   - ☐ 1 Volt pro Sekunde
   - ☐ 1 Coulomb pro Sekunde ✓
   - ☐ 1 Joule pro Sekunde
   - ☐ 1 Ohm pro Sekunde

3. **Ein Strom von 2A für 1 Stunde transportiert:**
   - ☐ 2 Coulomb
   - ☐ 7200 Coulomb ✓
   - ☐ 3600 Coulomb
   - ☐ 2 Ah

## 🎯 Lösungen

### Aufgabe 1: LED-Strom
**I = Q ÷ t = 12C ÷ 600s = 0,02A = 20mA**

### Aufgabe 2: USB-Ladevorgang
1. **Q = I × t = 2,5A × 7200s = 18.000C = 5Ah**
2. **N = 18.000 × 6,24 × 10¹⁸ = 1,12 × 10²³ Elektronen**

### Aufgabe 3: Festplatte
1. **Q₁ = 1,2A × 5s = 6C**
2. **Q₂ = 0,6A × 3595s = 2.157C**
3. **Q_ges = 6C + 2.157C = 2.163C**

### Aufgabe 4: Kondensator
**Q = I × t = 0,05A × 0,1s = 0,005C = 5mC**

## 📝 Merkregeln

```
Formel I = Q/t:
□ I = Strom (Ampere)
□ Q = Ladung (Coulomb)
□ t = Zeit (Sekunden)
□ Strom = Ladung pro Zeit

Umstellungen:
□ Q = I × t (Ladung berechnen)
□ t = Q ÷ I (Zeit berechnen)
□ 1A = 1C/s = 1As/s

Größenordnungen:
□ 1C = 6,24 × 10¹⁸ Elektronen
□ 1Ah = 3600C
□ Selbst kleine Ströme = Milliarden Elektronen

Praxis:
□ Akku-Laufzeit: t = Kapazität ÷ Strom
□ Hoher Strom = schnelle Entladung
□ Stromdichte beachten (Wärme!)
□ Gleichstrom vs. Wechselstrom
```

---

**▶️ Nächste Vertiefung:** [Widerstand und Leitwert R=1/G](./09_Widerstand_Leitwert.md)