# Vertiefung: Elektrische Spannung (U = W/Q)

## 🎯 Lernziel
Du verstehst die physikalische Definition der Spannung und kannst mit der Formel U = W/Q rechnen.

## 📖 Die Grundformel der Spannung

**Spannung** ist definiert als **Arbeit pro Ladung**:

### ⚡ Formel: U = W/Q

- **U** = Spannung in Volt [V]
- **W** = Arbeit (Energie) in Joule [J]  
- **Q** = Ladung in Coulomb [C]

### 🧠 Physikalische Bedeutung
**Spannung** gibt an, wie viel **Arbeit** verrichtet werden muss, um **1 Coulomb Ladung** von einem Punkt zum anderen zu bewegen.

## 🔬 Was bedeutet das praktisch?

### Analogie: Wasserbehälter
```
Hoher Wasserbehälter (hohe Spannung):
┌─────────┐ ← 10m hoch
│  Wasser │   = viel potentielle Energie
│         │   = viel "Arbeit" beim Herunterfallen
└─────────┘

Niedriger Wasserbehälter (niedrige Spannung):
┌─────────┐ ← 1m hoch  
│  Wasser │   = wenig potentielle Energie
└─────────┘   = wenig "Arbeit" beim Herunterfallen
```

### Elektrische Entsprechung
- **Hohe Spannung (12V):** Viel Energie pro Ladung → Starke "Kraft" auf Elektronen
- **Niedrige Spannung (1,2V):** Wenig Energie pro Ladung → Schwache "Kraft" auf Elektronen

## 🧮 Formel umstellen und rechnen

### Alle drei Formelformen
1. **U = W ÷ Q** (Spannung berechnen)
2. **W = U × Q** (Arbeit berechnen)  
3. **Q = W ÷ U** (Ladung berechnen)

### Einheiten umrechnen
- **1 Volt = 1 Joule/Coulomb**
- **1 J = 1 Ws** (Wattsekunde)
- **1 C = 1 As** (Amperesekunde)

## 🔍 Praktisches Beispiel: Smartphone-Akku

### Gegeben
- **Smartphone-Akku:** 3,7V, 3000mAh
- **Gesucht:** Gespeicherte Energie

### Rechnung Schritt für Schritt

**Schritt 1: Ladung berechnen**
- Q = 3000mAh = 3Ah = 3 × 3600s × A = 10.800 As = 10.800 C

**Schritt 2: Energie berechnen**
- W = U × Q = 3,7V × 10.800C = 39.960 J ≈ 40 kJ

**Schritt 3: In Wattstunden umrechnen**  
- W = 39.960 J = 39.960 Ws = 39.960 ÷ 3600 Wh = 11,1 Wh

### Interpretation
Der Smartphone-Akku speichert **11,1 Wh** Energie - genug für mehrere Stunden Betrieb!

## 🏢 IT-Anwendung: Serverschrank-Energieberechnung

### Szenario
Ein Serverschrank wird bei Stromausfall von einer USV versorgt:
- **USV-Batterie:** 48V, 100Ah  
- **Server-Verbrauch:** 2000W

### Aufgabe: Wie lange hält die USV?

**Schritt 1: Gespeicherte Energie berechnen**
- Q = 100Ah = 100 × 3600 C = 360.000 C
- W = U × Q = 48V × 360.000C = 17.280.000 J = 4.800 Wh

**Schritt 2: Laufzeit berechnen**
- t = W ÷ P = 4.800 Wh ÷ 2000W = 2,4h = **144 Minuten**

**Ergebnis:** Die USV kann den Serverschrank **2,4 Stunden** versorgen.

## 🧮 Übungsaufgaben

### Aufgabe 1: Laptop-Netzteil
Ein Laptop-Netzteil liefert 19V bei 3,42A für 2 Stunden.

**Gesucht:**
1. Transportierte Ladung: Q = I × t = _____ C
2. Verrichtete Arbeit: W = U × Q = _____ J
3. Energie in kWh: W = _____ kWh

### Aufgabe 2: LED-Energie
Eine LED (2V, 20mA) leuchtet 8 Stunden.

**Gesucht:**
1. Ladung durch LED: Q = _____ C
2. Energie-Verbrauch: W = _____ J  
3. Kosten bei 0,30€/kWh: _____ €

### Aufgabe 3: CMOS-Batterie  
Eine CMOS-Batterie (3V, 225mAh) versorgt den CMOS-Speicher.

**Gesucht:**
1. Gespeicherte Energie: W = _____ J
2. Bei 10μA Verbrauch, Laufzeit: t = _____ Jahre

## 🔬 Erweiterte Betrachtung: Energiedichte

### Verschiedene Speichertechnologien vergleichen

| Technologie | Spannung | Energiedichte | Anwendung |
|-------------|----------|---------------|-----------|
| **Li-Ion** | 3,7V | 150 Wh/kg | Smartphones, Laptops |
| **Blei-Gel** | 12V | 35 Wh/kg | USV, Autos |
| **Kondensator** | 2,7V | 5 Wh/kg | Kurzzeitpufferung |

### Warum nutzen Smartphones Li-Ion?
- **Hohe Energiedichte:** Viel Energie bei wenig Gewicht
- **Hohe Spannung:** Weniger Zellen nötig
- **Lange Lebensdauer:** 500-1000 Ladezyklen

## ⚡ Spannung und Gefahr

### Gefahrengrenzen verstehen
```
Berührungsspannung und Gefahr:

< 50V DC:    ┣━━━━━━━━━━━━━━┫ Ungefährlich
             USB, Laptop, 12V Auto

50-120V DC:  ┣━━━━┫ Vorsicht!
             48V USV, 110V USA

> 120V DC:   ┣━┫ GEFAHR!  
             230V Netz, Hochspannung
```

### Warum ist hohe Spannung gefährlich?
- **U = W/Q:** Hohe Spannung = viel Energie pro Ladung
- **Mehr Energie = mehr Schäden** am menschlichen Körper
- **Bereits 50V** können bei schlechten Bedingungen gefährlich werden

## 🔍 Messung: Spannung vs. Energie

### Was misst ein Voltmeter wirklich?
```
Voltmeter zeigt: 12V
Bedeutung: Pro Coulomb Ladung werden 12 Joule Energie freigesetzt

Batterie-Kapazität: 7Ah = 25.200 C
Gespeicherte Energie: W = 12V × 25.200C = 302.400 J = 84 Wh
```

### Energiemesser (kWh-Zähler)
```
Stromzähler zu Hause:
┌─────────────────┐
│ 1247,3 kWh      │ ← Verbrauchte Energie
│ 2,4 kW          │ ← Aktuelle Leistung  
└─────────────────┘

Berechnung: kWh = kW × h (Leistung × Zeit)
```

## ✅ Selbsttest

**Kreuze die richtigen Antworten an:**

1. **Die Formel U = W/Q bedeutet:**
   - ☐ Spannung ist Leistung pro Ladung
   - ☐ Spannung ist Arbeit pro Ladung ✓
   - ☐ Spannung ist Strom pro Ladung
   - ☐ Spannung ist Zeit pro Ladung

2. **1 Volt entspricht:**
   - ☐ 1 Watt pro Coulomb
   - ☐ 1 Joule pro Coulomb ✓
   - ☐ 1 Ampere pro Coulomb
   - ☐ 1 Ohm pro Coulomb

3. **Bei doppelter Spannung wird:**
   - ☐ Die gleiche Energie pro Ladung übertragen
   - ☐ Die doppelte Energie pro Ladung übertragen ✓
   - ☐ Die halbe Energie pro Ladung übertragen
   - ☐ Keine Energie übertragen

## 🎯 Lösungen

### Aufgabe 1: Laptop-Netzteil
1. **Q = I × t = 3,42A × 7200s = 24.624 C**
2. **W = U × Q = 19V × 24.624C = 467.856 J**
3. **W = 467.856 J = 0,13 kWh**

### Aufgabe 2: LED-Energie  
1. **Q = I × t = 0,02A × 28.800s = 576 C**
2. **W = U × Q = 2V × 576C = 1.152 J**
3. **Kosten = 1.152 J = 0,00032 kWh × 0,30€ = 0,000096€ ≈ 0,01 Cent**

### Aufgabe 3: CMOS-Batterie
1. **W = U × Q = 3V × 810C = 2.430 J**
2. **t = Q ÷ I = 0,225Ah ÷ 0,00001A = 22.500h ≈ 2,6 Jahre**

## 📝 Merkregeln

```
Formel U = W/Q:
□ U = Spannung (Volt)
□ W = Arbeit/Energie (Joule)  
□ Q = Ladung (Coulomb)
□ Spannung = Energie pro Ladung

Umstellungen:
□ W = U × Q (Energie berechnen)
□ Q = W ÷ U (Ladung berechnen)
□ 1V = 1J/C = 1Ws/As

Praxis:
□ Hohe Spannung = viel Energie pro Ladung
□ Akkus: W = U × I × t (Energie = Spannung × Strom × Zeit)
□ Energiedichte wichtig für mobile Geräte
□ > 50V: Vorsicht wegen hoher Energie!
```

---

**▶️ Nächste Vertiefung:** [Stromstärke und Ladung I=Q/t](./08_Stromstaerke_Ladung_Formel.md)