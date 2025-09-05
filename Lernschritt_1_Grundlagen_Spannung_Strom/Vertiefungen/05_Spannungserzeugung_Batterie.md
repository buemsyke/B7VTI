# Vertiefung: Technische Spannungserzeugung am Beispiel einer Batterie

## 🎯 Lernziel
Du verstehst, wie eine Batterie Spannung erzeugt und welche Rolle sie in IT-Systemen spielt.

## 📖 Wie erzeugt eine Batterie Spannung?

Eine **Batterie** wandelt **chemische Energie** in **elektrische Energie** um. Sie besteht aus zwei verschiedenen **Materialien** (Elektroden), die in einer **chemischen Lösung** (Elektrolyt) stehen.

### ⚡ Grundprinzip der Spannungserzeugung

```
Batterie-Aufbau (vereinfacht):

 (-) Zink-Elektrode    (+) Kupfer-Elektrode
       │                      │
       │    Elektrolyt        │
       │   (Salzlösung)       │
       └──────────────────────┘
              
Elektronenfluss: (-) ──→ (+) durch äußeren Stromkreis
```

### 🔬 Was passiert chemisch?
1. **Zink-Elektrode:** Gibt Elektronen ab (wird positiv geladen)
2. **Kupfer-Elektrode:** Nimmt Elektronen auf (wird negativ geladen)  
3. **Elektrolyt:** Ermöglicht Ionenaustausch zwischen Elektroden
4. **Äußerer Stromkreis:** Elektronen fließen von (-) nach (+)

## 🔋 Batterietypen in der IT

### Primärbatterien (nicht wiederaufladbar)

| Batterietyp | Spannung | Anwendung IT |
|-------------|----------|--------------|
| **Alkali-Mangan** | 1,5V | Fernbedienungen, Tastaturen |
| **Lithium** | 3V | CMOS-Batterie (Mainboard) |
| **Zink-Kohle** | 1,5V | Billige Geräte |

### Sekundärbatterien (wiederaufladbar)

| Batterietyp | Spannung | Anwendung IT |
|-------------|----------|--------------|
| **Li-Ion** | 3,7V | Smartphones, Laptops |
| **Li-Po** | 3,7V | Tablets, dünne Geräte |
| **NiMH** | 1,2V | Ältere Laptops |
| **Blei-Gel** | 12V | USV (Unterbrechungsfreie Stromversorgung) |

## 🔍 Praktisches Beispiel: CMOS-Batterie

### Funktion im Computer
```
Mainboard:
┌─────────────────────────────────────┐
│  ┌─────┐  ┌─────────┐  ┌─────────┐  │
│  │ CPU │  │   RAM   │  │  CMOS   │  │
│  └─────┘  └─────────┘  │ Batterie│  │
│                        │   3V    │  │
│  ┌──────────────────┐  └─────────┘  │
│  │  CMOS-Speicher   │               │
│  │ (BIOS-Settings)  │←──── 3V       │
│  └──────────────────┘               │
└─────────────────────────────────────┘
```

### Warum braucht der Computer eine Batterie?
- **BIOS-Einstellungen** speichern (auch bei ausgeschaltetem PC)
- **Systemzeit** weiterlaufen lassen
- **Hardware-Konfiguration** behalten
- **Boot-Reihenfolge** merken

### Typische Lebensdauer: 3-5 Jahre

## 🏢 USV-Batterien im Rechenzentrum

### Aufgabe der USV (Unterbrechungsfreie Stromversorgung)
```
Stromausfall-Szenario:

Netzstrom 230V ───┐
                  │
                ┌─▼─┐    ┌─────────┐    ┌─────────┐
                │USV│────│ Server  │────│ Daten   │
                └─┬─┘    └─────────┘    └─────────┘
                  │
           12V Blei-Batterien
```

**Funktion:**
1. **Normal:** Netz versorgt Server, Batterien werden geladen
2. **Stromausfall:** Batterien übernehmen sofort die Versorgung
3. **Zeit für:** Sicheres Herunterfahren oder Generator-Start

### Typische USV-Batteriedaten
- **Spannung:** 12V (oft mehrere in Reihe = 24V, 48V)
- **Kapazität:** 7Ah - 200Ah
- **Überbrückungszeit:** 5-30 Minuten
- **Lebensdauer:** 3-5 Jahre

## 🧮 Batterieberechnung

### Grundformeln

**Kapazität:** C = I × t
- **C:** Kapazität in Ah (Amperestunden)
- **I:** Strom in A (Ampere)
- **t:** Zeit in h (Stunden)

**Entladezeit:** t = C ÷ I

### Praxisbeispiel: Laptop-Akku
```
Laptop-Daten:
- Akku: Li-Ion, 14,8V, 4400mAh (4,4Ah)
- Stromaufnahme: 2,2A

Laufzeit berechnen:
t = C ÷ I = 4,4Ah ÷ 2,2A = 2 Stunden
```

## 🧮 Übung: Batterieberechnungen

**Aufgabe 1:** CMOS-Batterie-Lebensdauer

Eine CMOS-Batterie (3V, 225mAh) versorgt den CMOS-Speicher mit 10μA.

Wie lange hält die Batterie?
t = C ÷ I = 225mAh ÷ 0,01mA = _____ Stunden = _____ Jahre

**Aufgabe 2:** USV-Auslegung

Ein Server verbraucht 300W bei 12V. Die USV soll 15 Minuten überbrücken.

1. Stromaufnahme: I = P ÷ U = 300W ÷ 12V = _____ A
2. Benötigte Kapazität: C = I × t = _____ A × 0,25h = _____ Ah

**Aufgabe 3:** Smartphone-Ladezeit

Smartphone-Akku: 3000mAh, Ladestrom: 2A

Ladezeit: t = C ÷ I = 3Ah ÷ 2A = _____ h = _____ min

## 🔬 Batterie-Kennlinie verstehen

### Entladekurve einer Batterie
```
Spannung
   ↑
3,0V ┃─────────────────────┐
     ┃                     │
2,8V ┃                     │
     ┃                     └─────────┐
2,6V ┃                               │
     ┃                               └─────────
2,4V ┃
     └─────────────────────────────────────────→ Zeit
     0%        50%        80%        100%
           Entladung
```

**Erkenntnis:** Batteriespannung fällt beim Entladen ab!

### Praktische Auswirkung
- **Neu:** 3,0V - Gerät funktioniert perfekt
- **50% entladen:** 2,8V - Gerät funktioniert noch  
- **80% entladen:** 2,6V - "Low Battery" Warnung
- **100% entladen:** 2,4V - Gerät schaltet ab

## ⚠️ Batteriesicherheit

### Gefahren vermeiden
- **Kurzschluss:** Kann Brand verursachen!
- **Überhitzung:** Batterie kann explodieren
- **Falsche Polarität:** Gerät kaputt
- **Tiefentladung:** Batterie unbrauchbar

### Sicherheitsregeln
1. **Kurzschluss vermeiden:** Plus und Minus nie verbinden
2. **Richtige Polarität:** + und - beachten
3. **Nicht erhitzen:** Temperaturen über 60°C meiden
4. **Fachgerecht entsorgen:** Batterien gehören in Sondermüll

## ✅ Selbsttest

**Kreuze die richtigen Antworten an:**

1. **Eine Batterie wandelt um:**
   - ☐ Elektrische in chemische Energie
   - ☐ Chemische in elektrische Energie ✓
   - ☐ Mechanische in elektrische Energie
   - ☐ Thermische in elektrische Energie

2. **CMOS-Batterien haben typisch:**
   - ☐ 1,5V
   - ☐ 3V ✓
   - ☐ 12V
   - ☐ 230V

3. **Eine 1000mAh Batterie bei 100mA Strom hält:**
   - ☐ 1 Stunde
   - ☐ 10 Stunden ✓
   - ☐ 100 Stunden
   - ☐ 1000 Stunden

## 🎯 Lösungen

### Übung Aufgabe 1:
t = 225mAh ÷ 0,01mA = **22.500 Stunden ≈ 2,6 Jahre**

### Übung Aufgabe 2:
1. I = 300W ÷ 12V = **25A**
2. C = 25A × 0,25h = **6,25Ah**

### Übung Aufgabe 3:
t = 3Ah ÷ 2A = **1,5h = 90 min**

## 📝 Merkregeln

```
Batterie-Grundlagen:
□ Chemische → Elektrische Energie
□ Zwei verschiedene Elektroden
□ Elektrolyt ermöglicht Ionenfluss
□ Elektronen fließen von (-) nach (+)

IT-Anwendungen:
□ CMOS: 3V, Jahre Lebensdauer
□ Laptop: Li-Ion, 3,7V/Zelle
□ USV: Blei-Gel, 12V
□ Smartphone: Li-Po, 3,7V

Berechnung:
□ Kapazität: C = I × t (Ah = A × h)
□ Laufzeit: t = C ÷ I
□ Spannung fällt beim Entladen!
```

---

**▶️ Nächste Vertiefung:** [Messung von Strom und Spannung](./06_Messung_Strom_Spannung.md)