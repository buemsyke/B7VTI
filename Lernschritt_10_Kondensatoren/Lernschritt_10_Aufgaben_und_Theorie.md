# Lernschritt 10: Kondensatoren in Gleichstromkreisen
## 🎯 Handlungssituation: Störungsfreie Stromversorgung im Rechenzentrum

Das Rechenzentrum läuft im Dauerbetrieb, doch die empfindliche Messtechnik und die Mikrocontroller-Steuerungen zeigen gelegentlich Störungen. Kurze Spannungseinbrüche beim Einschalten großer Verbraucher (z. B. Klimaanlage, Server-Netzteile) und hochfrequentes Rauschen auf den Versorgungsleitungen führen zu Fehlfunktionen. Dein Projektleiter bittet dich, die Grundlagen von Kondensatoren zu verstehen, um Puffer-, Glättungs- und Filterschaltungen richtig dimensionieren zu können.

**Deine Aufgabe:**
- Aufbau und Funktionsweise von Kondensatoren verstehen
- Lade- und Entladevorgänge in RC-Schaltungen analysieren
- Zeitkonstanten berechnen und in Tinkercad messen
- Praktische Anwendungen von Kondensatoren in der IT kennenlernen

## 📖 Fachwissen: Der Kondensator

### Was ist ein Kondensator?

Ein **Kondensator** (Capacitor) speichert elektrische Energie in einem elektrischen Feld zwischen zwei leitenden Platten, die durch ein Isoliermaterial (Dielektrikum) getrennt sind.

**Aufbau:**
```
    Platte 1          Platte 2
    ┌──────┐          ┌──────┐
    │//////│  Dielek- │//////│
    │//////│  trikum  │//////│
    │//////│          │//////│
    └──┬───┘          └──┬───┘
       │                 │
  Anschluss 1       Anschluss 2
```

**Schaltzeichen:**
```
       ──┤├──       Kondensator (allgemein)
       ──┤┣──       Elektrolytkondensator (polarisiert, + Seite markiert)
```

### Die Kapazität C

Die **Kapazität** beschreibt, wie viel Ladung ein Kondensator bei einer bestimmten Spannung speichern kann.

**Formel:**
```
C = Q / U
```

| Größe | Symbol | Einheit |
|-------|--------|---------|
| Kapazität | C | Farad (F) |
| Ladung | Q | Coulomb (C) |
| Spannung | U | Volt (V) |

**Typische Werte:**
| Kapazität | Abkürzung | Anwendung |
|-----------|-----------|-----------|
| 1 pF – 100 pF | Picofarad | Hochfrequenztechnik |
| 100 pF – 1 μF | Nanofarad | Entstörung, Filter |
| 1 μF – 1000 μF | Mikrofarad | Glättung, Pufferung |
| 1000 μF – 1 F | Millifarad | Energiespeicher |

### Kondensatortypen

| Typ | Kapazitätsbereich | Polarität | Anwendung |
|-----|-------------------|-----------|-----------|
| Keramikkondensator | 1 pF – 10 μF | Nein | HF-Entstörung, Filterung |
| Folienkondensator | 1 nF – 10 μF | Nein | Audio, Signalverarbeitung |
| Elektrolytkondensator (Elko) | 1 μF – 10.000 μF | **Ja** | Glättung, Pufferung |
| Tantalkondensator | 0,1 μF – 1000 μF | **Ja** | Platzsparende Pufferung |

⚠️ **Achtung:** Elektrolytkondensatoren sind **polarisiert** – falscher Anschluss kann zur Zerstörung führen!

### Kondensatoren in Reihen- und Parallelschaltung

**Parallelschaltung** (Kapazitäten addieren sich):
```
C_gesamt = C₁ + C₂ + C₃ + ...
```

**Reihenschaltung** (ähnlich wie Widerstände parallel):
```
1/C_gesamt = 1/C₁ + 1/C₂ + 1/C₃ + ...
```

**Für zwei Kondensatoren in Reihe:**
```
C_gesamt = (C₁ × C₂) / (C₁ + C₂)
```

**Merke:** Bei Kondensatoren ist es genau **umgekehrt** wie bei Widerständen!
- Parallel → addieren sich (wie R in Reihe)
- Reihe → Kehrwert-Formel (wie R parallel)

### Gespeicherte Energie

Die im Kondensator gespeicherte Energie beträgt:

```
W = ½ × C × U²
```

| Größe | Symbol | Einheit |
|-------|--------|---------|
| Energie | W | Joule (J) |
| Kapazität | C | Farad (F) |
| Spannung | U | Volt (V) |

## 📖 Fachwissen: Die RC-Schaltung

### Lade- und Entladevorgang

Wird ein Kondensator über einen Widerstand geladen oder entladen, geschieht dies **nicht sofort**, sondern folgt einer **Exponentialfunktion**.

**Ladeschaltung:**
```
              R
    U_ein ──┤███├──┬── U_C
                   │
              C  ──┤├──
                   │
    GND ───────────┴── GND
```

### Die Zeitkonstante τ (tau)

Die **Zeitkonstante** τ bestimmt, wie schnell der Lade-/Entladevorgang abläuft:

```
τ = R × C
```

| Größe | Symbol | Einheit |
|-------|--------|---------|
| Zeitkonstante | τ | Sekunden (s) |
| Widerstand | R | Ohm (Ω) |
| Kapazität | C | Farad (F) |

### Ladekurve

| Zeit | Spannung am Kondensator | Prozent von U_ein |
|------|------------------------|-------------------|
| 0 × τ | 0 V | 0 % |
| 1 × τ | 0,632 × U_ein | 63,2 % |
| 2 × τ | 0,865 × U_ein | 86,5 % |
| 3 × τ | 0,950 × U_ein | 95,0 % |
| 4 × τ | 0,982 × U_ein | 98,2 % |
| 5 × τ | 0,993 × U_ein | 99,3 % |

**Faustregel:** Nach **5 × τ** gilt der Kondensator als **vollständig geladen** (99,3 %).

### Entladekurve

| Zeit | Spannung am Kondensator | Prozent von U_start |
|------|------------------------|---------------------|
| 0 × τ | U_start | 100 % |
| 1 × τ | 0,368 × U_start | 36,8 % |
| 2 × τ | 0,135 × U_start | 13,5 % |
| 3 × τ | 0,050 × U_start | 5,0 % |
| 4 × τ | 0,018 × U_start | 1,8 % |
| 5 × τ | 0,007 × U_start | 0,7 % |

**Faustregel:** Nach **5 × τ** gilt der Kondensator als **vollständig entladen**.

### Formeln für Lade- und Entladevorgang

**Laden:**
```
U_C(t) = U_ein × (1 - e^(-t/τ))
I_C(t) = (U_ein / R) × e^(-t/τ)
```

**Entladen:**
```
U_C(t) = U_start × e^(-t/τ)
I_C(t) = -(U_start / R) × e^(-t/τ)
```

## 🔧 Tinkercad-Übung 1: Kondensator laden und entladen

### Schaltung: RC-Ladevorgang beobachten

```
              R = 1 kΩ
    9V ──┬──┤███├──┬───── Messpunkt U_C
         │         │
    Schalter    C = 470 μF
         │         │
    GND ──┴────────┴───── GND
```

### Komponenten:
- 1× 9V Batterie
- 1× Widerstand 1 kΩ
- 1× Elektrolytkondensator 470 μF
- 1× Schalter (Schiebeschalter)
- 1× Multimeter (Spannungsmessung)
- Verbindungsdrähte

### Aufbau:

1. **9V Batterie** als Spannungsquelle
2. **Schalter** in Reihe zur Batterie
3. **1 kΩ Widerstand** in Reihe nach dem Schalter
4. **470 μF Elko** zwischen Widerstand und GND (Polarität beachten: + an Widerstand)
5. **Multimeter** parallel zum Kondensator (Spannungsmessung)

### Berechnung der Zeitkonstante:

```
τ = R × C = 1000 Ω × 0,000470 F = _____ s
```

### 🔍 Messungen – Ladevorgang:

1. **Schalter einschalten** und Stoppuhr starten
2. **Spannungsverlauf notieren:**

| Zeit (s) | U_C gemessen (V) | U_C berechnet (V) |
|----------|-------------------|--------------------|
| 0 | 0 V | 0 V |
| 0,5 | _____ V | _____ V |
| 1,0 | _____ V | _____ V |
| 1,5 | _____ V | _____ V |
| 2,0 | _____ V | _____ V |
| 2,5 | _____ V | _____ V |

3. **Nach welcher Zeit ist U_C ≈ 5,7 V (63,2 % von 9 V)?**
   - t ≈ _____ s (sollte ≈ τ sein)

### Variation: Widerstand ändern

**Ersetze den 1 kΩ durch 2,2 kΩ:**
- Neue Zeitkonstante: τ = _____ s
- Der Kondensator lädt jetzt _____ (schneller/langsamer)

**Ersetze den 1 kΩ durch 470 Ω:**
- Neue Zeitkonstante: τ = _____ s
- Der Kondensator lädt jetzt _____ (schneller/langsamer)

## 🔧 Tinkercad-Übung 2: LED-Nachleuchtschaltung

### Schaltung: LED leuchtet nach dem Ausschalten nach

```
                R1 = 220 Ω
    9V ──┬──┤███├──┬──┤███├── LED ──┐
         │         │   R2 = 470 Ω   │
    Schalter    C = 1000 μF         │
         │         │                │
    GND ──┴────────┴────────────────┘
```

### Komponenten:
- 1× 9V Batterie
- 1× Widerstand 220 Ω (R1 – Ladewiderstand)
- 1× Widerstand 470 Ω (R2 – Vorwiderstand LED)
- 1× Elektrolytkondensator 1000 μF
- 1× LED (rot)
- 1× Schalter
- 1× Multimeter
- Verbindungsdrähte

### Aufbau:

1. **9V Batterie** über Schalter und **R1 (220 Ω)** zum Knotenpunkt
2. **1000 μF Elko** zwischen Knotenpunkt und GND (Polarität beachten!)
3. **R2 (470 Ω)** und **LED** in Reihe vom Knotenpunkt nach GND

### Beobachtungen:

1. **Schalter einschalten:**
   - LED leuchtet _____ (sofort / langsam heller werdend)
   - U_C steigt auf ca. _____ V

2. **Schalter ausschalten:**
   - LED leuchtet noch für ca. _____ Sekunden nach
   - Zeitkonstante der Entladung: τ = R2 × C = 470 Ω × 0,001 F = _____ s
   - Nach 5 × τ = _____ s ist die LED aus

3. **Warum leuchtet die LED nach?**
   - Antwort: _____

## 🔧 Tinkercad-Übung 3: Kondensatoren parallel und in Reihe

### Teil A: Zwei Kondensatoren parallel

```
              R = 1 kΩ
    9V ──┬──┤███├──┬──────┬── Messpunkt
         │         │      │
    Schalter    C1=470μF C2=470μF
         │         │      │
    GND ──┴────────┴──────┴── GND
```

### Berechnung:
- C_gesamt = C₁ + C₂ = 470 μF + 470 μF = _____ μF
- τ = R × C_gesamt = 1000 Ω × _____ F = _____ s

### Messung:
- Ladezeit bis 63,2 % (5,7 V): t ≈ _____ s
- Vergleich mit einzelnem 470 μF: Ladezeit ist _____ (doppelt so lang / halb so lang)

### Teil B: Zwei Kondensatoren in Reihe

```
              R = 1 kΩ
    9V ──┬──┤███├──┬──┤├──┬──┤├──┬── GND
         │         │  C1  │  C2  │
    Schalter   Mess-│      │      │
         │    punkt │      │      │
    GND ──┴────────┘      └──────┘
                   470μF   470μF
```

### Berechnung:
- C_gesamt = (C₁ × C₂) / (C₁ + C₂) = _____ μF
- τ = R × C_gesamt = _____ s

### Messung:
- Ladezeit bis 63,2 %: t ≈ _____ s
- Vergleich: Reihenschaltung lädt _____ (schneller / langsamer) als Einzelkondensator

## 🧮 Rechenübungen

### Aufgabe 1: Zeitkonstante berechnen

Berechne die Zeitkonstante τ und die Zeit bis zur vollständigen Ladung (5 × τ) für folgende RC-Kombinationen:

| R | C | τ | 5 × τ |
|---|---|---|-------|
| 1 kΩ | 100 μF | _____ s | _____ s |
| 10 kΩ | 47 μF | _____ s | _____ s |
| 470 Ω | 1000 μF | _____ s | _____ s |
| 2,2 kΩ | 220 μF | _____ s | _____ s |

### Aufgabe 2: Kondensator für Pufferung dimensionieren

Ein Mikrocontroller (3,3 V) hat kurze Stromspitzen von 200 mA, die 10 ms dauern. Während dieser Zeit darf die Spannung maximal um 0,5 V einbrechen.

**Wie groß muss der Pufferkondensator sein?**

**Gegeben:**
- ΔU = 0,5 V (maximaler Spannungseinbruch)
- I = 200 mA = 0,2 A
- Δt = 10 ms = 0,01 s

**Formel:**
```
C = (I × Δt) / ΔU
```

**Berechnung:**
- C = (0,2 A × 0,01 s) / 0,5 V = _____ F = _____ μF

### Aufgabe 3: Gespeicherte Energie

Berechne die im Kondensator gespeicherte Energie:

**a)** C = 1000 μF, U = 5 V
- W = ½ × C × U² = ½ × 0,001 F × (5 V)² = _____ J = _____ mJ

**b)** C = 4700 μF, U = 12 V
- W = ½ × C × U² = ½ × 0,0047 F × (12 V)² = _____ J = _____ mJ

**c)** Wie lange könnte Kondensator b) eine LED mit 20 mA bei 2 V versorgen?
- P_LED = U × I = 2 V × 0,02 A = _____ W
- t = W / P = _____ J / _____ W = _____ s

### Aufgabe 4: Spannung zu einem bestimmten Zeitpunkt

Ein RC-Glied mit R = 2,2 kΩ und C = 100 μF wird mit 9 V geladen.

**a)** Berechne die Zeitkonstante:
- τ = R × C = 2200 Ω × 0,0001 F = _____ s

**b)** Welche Spannung hat der Kondensator nach 0,5 s?
- U_C(0,5 s) = 9 V × (1 - e^(-0,5/τ)) = _____ V

**c)** Nach welcher Zeit erreicht der Kondensator 7 V?
- 7 = 9 × (1 - e^(-t/τ))
- e^(-t/τ) = 1 - 7/9 = _____
- t = -τ × ln(_____) = _____ s

## 🎯 Praktische Anwendungen in der IT

### Anwendung 1: Stützkondensatoren auf Mainboards

Jeder Prozessor auf einem Mainboard hat zahlreiche **Stützkondensatoren** (Decoupling Capacitors) in unmittelbarer Nähe.

**Zweck:**
- Kurzzeitige Stromspitzen lokal bereitstellen
- Hochfrequentes Rauschen filtern
- Stabile Versorgungsspannung sicherstellen

**Typische Werte:**
- 100 nF Keramik (Hochfrequenz-Entkopplung)
- 10 μF Tantal (Mittelfrequenz-Pufferung)
- 100 μF – 470 μF Elko (Niederfrequenz-Glättung)

### Anwendung 2: Eingangskondensatoren bei Netzteilen

Die Kondensatoren C1 und C2, die du in Lernschritt 9 beim 7805-Linearregler eingesetzt hast, sind ein gutes Beispiel:

- **C1 (Eingang, 100 nF):** Filtert hochfrequente Störungen der Eingangsleitung
- **C2 (Ausgang, 100 nF):** Glättet die Ausgangsspannung und verhindert Schwingungen

### Anwendung 3: USV-Überbrückung (unterbrechungsfreie Stromversorgung)

Große Kondensatorbänke (Superkondensatoren) können kurzzeitige Stromausfälle überbrücken, bis der Dieselgenerator des Rechenzentrums anspringt.

**Beispielrechnung:**
- Server-Leistung: 500 W
- Überbrückungszeit: 5 s
- Benötigte Energie: W = P × t = 500 W × 5 s = 2500 J
- Bei U = 48 V: C = 2 × W / U² = 2 × 2500 / 48² ≈ **2,17 F** (Superkondensator)

### Anwendung 4: Entprellung von Tastern (Debouncing)

Mechanische Taster prellen beim Drücken (kurze Ein-/Aus-Impulse). Ein RC-Glied glättet diese Prellimpulse.

```
    Taster
    ──/ ──┬── R = 10 kΩ ── Vcc (5V)
          │
       C = 100 nF
          │
         GND
```

**Zeitkonstante:** τ = 10 kΩ × 100 nF = 1 ms

Das Signal wird innerhalb von ca. 5 ms (5 × τ) stabil – schneller als ein Mensch einen Taster drückt, aber langsam genug, um das Prellen zu unterdrücken.

## ⚡ Sicherheitshinweise für Kondensatoren

1. **Elektrolytkondensatoren** haben eine Polarität – **niemals verpolen!**
2. **Geladene Kondensatoren** können gefährliche Spannungen halten – **vor Arbeiten entladen!**
3. **Kurzschluss** eines geladenen Kondensators kann zu Funken und Beschädigungen führen
4. **Alte Elkos** können austrocknen und ausfallen – häufige Ursache für defekte Netzteile
5. **In Tinkercad** sind Kondensatoren sicher simulierbar – in der Realität immer Vorsicht!

## ✅ Selbstüberprüfung

1. **Ein Kondensator speichert Energie in Form von:**
   ☐ einem Magnetfeld
   ☐ einem elektrischen Feld
   ☐ Wärme

2. **Die Zeitkonstante τ eines RC-Glieds berechnet sich:**
   ☐ τ = R / C
   ☐ τ = R × C
   ☐ τ = C / R

3. **Nach einer Zeitkonstante (1 × τ) ist der Kondensator geladen auf:**
   ☐ 50 %
   ☐ 63,2 %
   ☐ 100 %

4. **Als vollständig geladen gilt ein Kondensator nach:**
   ☐ 1 × τ
   ☐ 3 × τ
   ☐ 5 × τ

5. **Zwei gleiche Kondensatoren parallel ergeben:**
   ☐ die halbe Kapazität
   ☐ die doppelte Kapazität
   ☐ die gleiche Kapazität

6. **Zwei gleiche Kondensatoren in Reihe ergeben:**
   ☐ die halbe Kapazität
   ☐ die doppelte Kapazität
   ☐ die gleiche Kapazität

7. **Stützkondensatoren auf Mainboards dienen hauptsächlich:**
   ☐ der Energiespeicherung für Stunden
   ☐ der Entkopplung und Filterung von Stromspitzen
   ☐ der Spannungserhöhung

8. **Die gespeicherte Energie im Kondensator berechnet sich:**
   ☐ W = C × U
   ☐ W = ½ × C × U²
   ☐ W = C × U²

## 🎯 Lösungen

### Tinkercad-Übungen:

**Übung 1: Ladevorgang**
- τ = 1000 Ω × 0,000470 F = **0,47 s**
- Nach 0,47 s: U_C ≈ 5,7 V (63,2 %)
- Mit 2,2 kΩ: τ = 1,034 s → langsamer
- Mit 470 Ω: τ = 0,221 s → schneller

**Übung 2: LED-Nachleuchtschaltung**
- LED leuchtet langsam heller werdend
- Entlade-Zeitkonstante: τ = 470 Ω × 0,001 F = 0,47 s
- 5 × τ = 2,35 s → LED leuchtet ca. 2-3 Sekunden nach
- Der Kondensator gibt die gespeicherte Energie über die LED ab

**Übung 3: Parallel und Reihe**
- Parallel: C_gesamt = 940 μF, τ = 0,94 s (doppelt so lang)
- Reihe: C_gesamt = 235 μF, τ = 0,235 s (schneller als Einzelkondensator)

### Rechenübungen:

**Aufgabe 1: Zeitkonstanten**

| R | C | τ | 5 × τ |
|---|---|---|-------|
| 1 kΩ | 100 μF | 0,1 s | 0,5 s |
| 10 kΩ | 47 μF | 0,47 s | 2,35 s |
| 470 Ω | 1000 μF | 0,47 s | 2,35 s |
| 2,2 kΩ | 220 μF | 0,484 s | 2,42 s |

**Aufgabe 2: Pufferkondensator**
- C = (0,2 A × 0,01 s) / 0,5 V = 0,004 F = **4000 μF**
- Ein 4700 μF Elko wäre ein passender Standardwert

**Aufgabe 3: Gespeicherte Energie**

a) W = ½ × 0,001 F × 25 V² = **12,5 mJ**

b) W = ½ × 0,0047 F × 144 V² = **338,4 mJ**

c) P_LED = 2 V × 0,02 A = 0,04 W
   t = 0,3384 J / 0,04 W = **8,46 s**
   (Hinweis: In der Praxis kürzer, da die Spannung exponentiell sinkt)

**Aufgabe 4: Spannung zu bestimmtem Zeitpunkt**

a) τ = 2200 Ω × 0,0001 F = **0,22 s**

b) U_C(0,5 s) = 9 V × (1 - e^(-0,5/0,22)) = 9 V × (1 - e^(-2,27)) = 9 V × (1 - 0,103) = **8,07 V**

c) e^(-t/0,22) = 1 - 7/9 = 0,222
   t = -0,22 × ln(0,222) = -0,22 × (-1,505) = **0,331 s**

### Selbstüberprüfung:

1. ✅ einem elektrischen Feld
2. ✅ τ = R × C
3. ✅ 63,2 %
4. ✅ 5 × τ
5. ✅ die doppelte Kapazität
6. ✅ die halbe Kapazität
7. ✅ der Entkopplung und Filterung von Stromspitzen
8. ✅ W = ½ × C × U²

---

## 📝 Notizen

Platz für deine eigenen Aufzeichnungen und Erkenntnisse:

```
Kondensator-Grundlagen:

Kapazität:
- C = Q / U
- Einheit: Farad (F), typisch μF, nF, pF

RC-Schaltung:
- Zeitkonstante: τ = R × C
- Ladevorgang: U_C(t) = U_ein × (1 - e^(-t/τ))
- Entladevorgang: U_C(t) = U_start × e^(-t/τ)
- Nach 5 × τ: vollständig geladen/entladen

Schaltungen:
- Parallel: C_gesamt = C₁ + C₂ + ...
- Reihe: 1/C_gesamt = 1/C₁ + 1/C₂ + ...

Energie:
- W = ½ × C × U²

IT-Anwendungen:
- Stützkondensatoren (Decoupling)
- Glättung bei Netzteilen
- Entprellung von Tastern
- USV-Überbrückung
```

---

## 📈 Dein Lernfortschritt

### ✅ Grundlagen-Checkliste Lernschritt 10
- [ ] Aufbau und Funktion von Kondensatoren verstehen
- [ ] Kapazität und Einheiten kennen
- [ ] Lade- und Entladevorgang erklären können
- [ ] Zeitkonstante τ = R × C berechnen
- [ ] Kondensatoren in Reihe und Parallel berechnen
- [ ] Tinkercad-Übungen erfolgreich absolviert
- [ ] Rechenübungen gelöst
- [ ] Praktische IT-Anwendungen verstanden
- [ ] Selbsttest bestanden

### 🔗 Verbindung zu vorherigen Lernschritten
- **Lernschritt 2:** Ohm'sches Gesetz → Widerstand bestimmt Ladegeschwindigkeit
- **Lernschritt 3:** Leistung → Energieberechnung im Kondensator
- **Lernschritt 4/5:** Reihen-/Parallelschaltung → Kondensatoren kombinieren
- **Lernschritt 9:** Spannungsregler → Kondensatoren für Filterung und Stabilisierung

**🚀 Weiter geht's – du vertiefst dein Wissen Schritt für Schritt!**
