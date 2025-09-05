# Vertiefung: Referenzkennzeichen nach EN IEC 81356

## 🎯 Lernziel
Du lernst die standardisierten Referenzkennzeichen kennen, die in der Elektrotechnik zur eindeutigen Bauteilidentifikation verwendet werden.

## 📖 Was sind Referenzkennzeichen?

**Referenzkennzeichen** sind eindeutige Bezeichnungen für Bauteile in Schaltplänen nach der Norm **EN IEC 81356**. Sie bestehen aus einem **Buchstaben** und einer **Nummer**.

### 🏷️ Aufbau eines Referenzkennzeichens
```
R47 = Widerstand Nr. 47
│ │
│ └── Nummer (eindeutig)
└── Buchstabe (Bauteiltyp)
```

## 🔧 Wichtige Referenzkennzeichen für IT-Systeme

### Grundlegende Bauteile

| Kennzeichen | Bauteil | Beispiele aus IT-Bereich |
|-------------|---------|---------------------------|
| **R** | Widerstand (Resistor) | R1, R15, R220 |
| **C** | Kondensator (Capacitor) | C1, C47, C100 |
| **L** | Spule (Inductor) | L1, L12 |
| **D** | Diode | D1, D5 (LED), D12 |

### Aktive Bauteile

| Kennzeichen | Bauteil | Beispiele aus IT-Bereich |
|-------------|---------|---------------------------|
| **IC** | Integrierter Schaltkreis | IC1 (Prozessor), IC15 (RAM-Controller) |
| **Q** | Transistor | Q1, Q25 |
| **U** | Verstärker/IC (USA-Standard) | U1, U12 |

### Verbindungen und Schnittstellen

| Kennzeichen | Bauteil | Beispiele aus IT-Bereich |
|-------------|---------|---------------------------|
| **X** | Steckverbinder/Buchse | X1 (USB), X12 (RJ45) |
| **S** | Schalter (Switch) | S1 (Power), S5 (Reset) |
| **F** | Sicherung (Fuse) | F1, F3 |

### Spannungsversorgung

| Kennzeichen | Bauteil | Beispiele aus IT-Bereich |
|-------------|---------|---------------------------|
| **T** | Transformator | T1 (Netzteil) |
| **BT** | Batterie | BT1 (CMOS), BT2 (USV) |
| **PS** | Netzteil (Power Supply) | PS1, PS2 |

## 🔍 Praxisbeispiel: Mainboard-Analyse

**Situation:** Du analysierst ein defektes Mainboard und findest folgende Bezeichnungen:

### Prozessor-Bereich
- **IC1** = Hauptprozessor (CPU)
- **C15, C16, C17** = Pufferkondensatoren für CPU
- **R22, R23** = Abschlusswiderstände

### RAM-Bereich  
- **IC10, IC11, IC12, IC13** = RAM-Module
- **R45** = Terminierungswiderstand
- **C25-C32** = Entkopplungskondensatoren

### Stromversorgung
- **IC20** = Spannungsregler
- **L5, L6** = Filterspulen
- **C50-C55** = Siebkondensatoren

### Schnittstellen
- **X1** = USB-Anschluss
- **X5** = Ethernet-Buchse (RJ45)
- **X10** = Stromversorgungsbuchse

## 🧮 Übung: Referenzkennzeichen zuordnen

**Aufgabe 1:** Erkläre, was diese Bauteile sind:

1. **R15** = ___________
2. **IC3** = ___________
3. **C22** = ___________
4. **D8** = ___________
5. **X12** = ___________

**Aufgabe 2:** Welche Referenzkennzeichen würdest du vergeben?

1. Der fünfte Widerstand: **___5**
2. Der zweite USB-Anschluss: **___2**
3. Der erste Kondensator: **___1**
4. Die dritte LED: **___3**

## 🔬 Praktische Anwendung: Fehlerbehebung

**Problemfall:** Ein Server startet nicht mehr. Im Schaltplan findest du:

```
Fehlermeldung: "Power LED (D5) leuchtet nicht"
Verdächtiger Schaltungsteil:
+5V ──── R12 ──── D5 ──── GND
         470Ω    LED
```

**Analyseschritt:**
1. **D5** = LED (Referenzkennzeichen verrät Bauteiltyp)
2. **R12** = Widerstand (Vorwiderstand für LED)
3. **Prüfung:** Spannung an R12 messen
4. **Austausch:** Bei Defekt R12 oder D5 tauschen

## 🎯 Nummerierungsregeln

### Logische Nummerierung
- **Funktionsgruppen zusammen:** R10-R19 (CPU-Bereich)
- **Signalwege folgen:** IC1 → R1 → C1 → IC2
- **Bereiche trennen:** 1-99 (Hauptplatine), 100-199 (Netzteil)

### Typische Nummerierungsbereiche

| Bereich | Bauteilnummern | Anwendung |
|---------|----------------|-----------|
| 1-99 | Grundschaltung | Prozessor, RAM, Grundfunktionen |
| 100-199 | Stromversorgung | Netzteile, Spannungsregler |
| 200-299 | Schnittstellen | USB, Ethernet, Video |
| 300-399 | Zusatzfunktionen | Audio, WLAN, Bluetooth |

## ✅ Selbsttest

**Kreuze die richtigen Antworten an:**

1. **Was bedeutet R47?**
   - ☐ 47. Kondensator
   - ☐ 47. Widerstand ✓
   - ☐ 47 Ohm Widerstand
   - ☐ 47V Spannung

2. **Welches Kennzeichen hat ein USB-Anschluss?**
   - ☐ U1
   - ☐ S1
   - ☐ X1 ✓
   - ☐ C1

3. **IC12 steht für:**
   - ☐ 12. Widerstand
   - ☐ 12. Integrierter Schaltkreis ✓
   - ☐ 12A Strom
   - ☐ 12V Spannung

## 🎯 Lösungen

### Übung Aufgabe 1:
1. **R15** = **Widerstand Nr. 15**
2. **IC3** = **Integrierter Schaltkreis Nr. 3**
3. **C22** = **Kondensator Nr. 22**
4. **D8** = **Diode Nr. 8**
5. **X12** = **Steckverbinder Nr. 12**

### Übung Aufgabe 2:
1. Der fünfte Widerstand: **R5**
2. Der zweite USB-Anschluss: **X2**
3. Der erste Kondensator: **C1**
4. Die dritte LED: **D3**

## 📝 Merkregeln

```
Referenzkennzeichen-ABC:
□ R = Widerstand (Resistor)
□ C = Kondensator (Capacitor)  
□ L = Spule (inductor/coiL)
□ D = Diode (auch LED)
□ IC = Integrierter Schaltkreis
□ X = steckerverbinder (eXternal)
□ S = Schalter (Switch)
□ F = Sicherung (Fuse)

Praxistipp: Nummer zeigt Position im Plan,
nicht den Wert des Bauteils!
```

**Wichtig:** R47 = 47. Widerstand ≠ 47Ω Widerstand!

---

**▶️ Nächste Vertiefung:** [Zählpfeile, Skalar und Vektor](./03_Zaehlpfeile_Skalar_Vektor.md)