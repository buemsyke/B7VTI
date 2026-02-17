# Lernschritt 9: Spannungsversorgung - Linear- und Schaltregler
## 🎯 Handlungssituation: Stromversorgung für das Rechenzentrum

Das Rechenzentrum ist in Betrieb! Doch der Projektleiter hat ein neues Anliegen: Die verschiedenen Komponenten benötigen unterschiedliche Spannungen (5V, 3.3V, 12V, 24V), und die Stromversorgung soll effizient und zuverlässig sein. Du sollst die Grundlagen von Spannungsreglern verstehen - sowohl Linearregler als auch Schaltregler - um die richtige Wahl für verschiedene Anwendungen treffen zu können.

**Deine finale Aufgabe:**
- Unterschiede zwischen Linear- und Schaltreglern verstehen
- Wirkungsgrade vergleichen und berechnen
- Wärmeentwicklung und Kühlung dimensionieren
- Die richtige Spannungsversorgung für IT-Komponenten auswählen

## 📖 Fachwissen: Spannungsversorgung

### Was ist ein Spannungsregler?

Ein **Spannungsregler** (Voltage Regulator) wandelt eine unstabilisierte Eingangsspannung in eine stabile, konstante Ausgangsspannung um - unabhängig von:
- Schwankungen der Eingangsspannung
- Änderungen der Last (Stromaufnahme)
- Temperaturänderungen

**Haupttypen:**
1. **Linearregler** (Linear Regulator)
2. **Schaltregler** (Switching Regulator)

### 1. Linearregler (Linear Regulator)

#### Funktionsprinzip

Ein Linearregler arbeitet wie ein **elektronisch regelbarer Widerstand**, der die überschüssige Spannung in Wärme umwandelt.

**Vereinfachtes Prinzip:**
```
U_ein ──┬─── [Steuerung ]─────┬─── U_aus
        │    (mit Transistor) │
        │          │          │
   C1  ===         │     C2  ===
        │          │          │
        │          │          │
    ────┴──────────┴──────────┴─── GND
            
```

Der Transistor der Steuerung passt seinen Widerstand so an, dass die Ausgangsspannung konstant bleibt.
Die Kondensatoren dienen der Stabilisierung und Glättung der Spannung.

#### Beliebte Linearregler

**7805 (5V-Regler):**
- Eingangsspannung: 7-35V
- Ausgangsspannung: 5V (fest)
- Maximaler Strom: 1,5A
- Dropout-Spannung: ca. 2V

**LM317 (einstellbarer Regler):**
- Eingangsspannung: 3-40V
- Ausgangsspannung: 1,25-37V (einstellbar)
- Maximaler Strom: 1,5A
- Dropout-Spannung: ca. 3V

**Dropout-Spannung:** Minimale Differenz zwischen Ein- und Ausgang, damit der Regler funktioniert

#### Vorteile von Linearreglern

✅ **Einfacher Aufbau** - wenige externe Bauteile
✅ **Geringe Störungen** - kein hochfrequentes Schalten
✅ **Günstiger Preis**
✅ **Kleine Bauform möglich**
✅ **Kein EMV-Problem** - keine elektromagnetischen Störungen

#### Nachteile von Linearreglern

❌ **Niedriger Wirkungsgrad** bei großer Spannungsdifferenz
❌ **Hohe Wärmeentwicklung** - Kühlung erforderlich
❌ **Nur Spannungsreduktion** möglich (keine Erhöhung)
❌ **Verlustleistung** = (U_ein - U_aus) × I

#### Wirkungsgrad Linearregler

```
η = (U_aus / U_ein) × 100%
```

**Beispiel:**
- Eingangsspannung: 12V
- Ausgangsspannung: 5V
- Wirkungsgrad: η = (5V / 12V) × 100% = **41,7%**
- **58,3% werden als Wärme abgeführt!**

### 2. Schaltregler (Switching Regulator)

#### Funktionsprinzip

Ein Schaltregler arbeitet mit **schnellem Ein- und Ausschalten** (Frequenz: 100kHz - mehrere MHz) und Energiespeicherung in Spulen und Kondensatoren.

**Vereinfachtes Prinzip:**

![Wikipedia](https://de.wikipedia.org/wiki/Abwärtswandler#/media/Datei:Buck_converter.svg)            


Durch das Verhältnis von Ein- zu Ausschaltzeit (Duty Cycle) wird die Ausgangsspannung geregelt.

#### Typen von Schaltreglern

**1. Buck-Converter (Step-Down):**
- Ausgang < Eingang
- Beispiel: 12V → 5V

**2. Boost-Converter (Step-Up):**
- Ausgang > Eingang
- Beispiel: 5V → 12V

**3. Buck-Boost-Converter:**
- Ausgang kann < oder > Eingang sein
- Flexible Spannungswandlung

**4. Invertierende Regler:**
- Negative Ausgangsspannung
- Beispiel: +12V → -12V

#### Vorteile von Schaltreglern

✅ **Hoher Wirkungsgrad** - typisch 80-95%
✅ **Geringe Wärmeentwicklung**
✅ **Spannungserhöhung möglich** (Boost)
✅ **Effizient bei großen Spannungsdifferenzen**
✅ **Kleinere Kühler** erforderlich

#### Nachteile von Schaltreglern

❌ **Komplexer Aufbau** - mehr externe Bauteile
❌ **Höhere Kosten**
❌ **EMV-Probleme** - hochfrequente Störungen
❌ **Ausgangsspannung mit Restwelligkeit** (Ripple)
❌ **Größere Bauform** durch Spule

#### Wirkungsgrad Schaltregler

Typische Wirkungsgrade:
- **Buck-Converter:** 85-95%
- **Boost-Converter:** 80-90%
- **Buck-Boost:** 75-90%

**Der Wirkungsgrad ist relativ konstant** über verschiedene Spannungsdifferenzen!

## 🔧 Tinkercad-Übung 1: Linearregler 7805

### Schaltung: 9V auf 5V mit 7805

```
  12V ──┬─────── [7805]───────┬─── 5V
        │          │          │
        │          │          │
   C1  ===         │     C2  ===
        │          │          │
        │          │          │
    ────┴──────────┴──────────┴─── GND
            
```

### Komponenten:
- 1× 12V Batterie
- 1× Spannungsregler 7805
- 2× Kondensator 100nF (0,1μF)
- 1× LED (rot)
- 1× Widerstand 220Ω
- 1× Multimeter
- Verbindungsdrähte

### Aufbau:

1. **12V Batterie** als Eingangsspannung
2. **100nF Kondensator** zwischen Eingang und GND
3. **7805** mit:
   - Pin 1 (IN) an 12V
   - Pin 2 (GND) an GND
   - Pin 3 (OUT) an 5V-Ausgang
4. **100nF Kondensator** zwischen Ausgang und GND
5. **LED + Widerstand** zur Visualisierung

### 🔍 Messungen:

1. **Eingangsspannung messen:**
   - U_ein = _____ V

2. **Ausgangsspannung messen:**
   - U_aus = _____ V (sollte ~5V sein)

3. **Laststrom messen** (durch LED):
   - I_Last = _____ mA

4. **Verlustleistung berechnen:**
   - P_Verlust = (U_ein - U_aus) × I_Last
   - P_Verlust = (12V - 5V) × _____ A = _____ W

5. **Wirkungsgrad berechnen:**
   - η = (U_aus / U_ein) × 100%
   - η = (5V / 12V) × 100% = _____ %

### Variation: Last erhöhen

**Füge einen 100Ω Widerstand parallel zur LED hinzu:**

1. **Neuer Laststrom:**
   - I_Last = _____ mA (deutlich höher!)

2. **Neue Verlustleistung:**
   - P_Verlust = (12V - 5V) × _____ A = _____ W

3. **Temperatur des 7805:** Der Regler wird _____ (warm/heiß)

## 🔧 Übung 2: Einstellbarer Regler LM317 (nur berechnen)

### Schaltung: Variable Spannung mit LM317

```
        R1 (240Ω)
12V ──[LM317]──┬──── U_aus
       │ ADJ   │
       │       R2
       └───────┴──── GND
         (Potentiometer
          1kΩ)
```

### Formel für U_aus:

```
U_aus = 1,25V × (1 + R2/R1)
```

### Komponenten:
- 1× 12V Batterie
- 1× LM317 (einstellbarer Regler)
- 1× Widerstand 240Ω (R1)
- 1× Potentiometer 1kΩ (R2)
- 2× Kondensator 100nF
- 1× Multimeter

### Berechnungen:

**Bei R2 = 240Ω:**
- U_aus = 1,25V × (1 + 240Ω/240Ω) = 1,25V × 2 = _____ V

**Bei R2 = 1000Ω:**
- U_aus = 1,25V × (1 + 1000Ω/240Ω) = 1,25V × 5,17 = _____ V

### Aufgabe:
**Berechne R2 für U_aus = 9V:**
- 9V = 1,25V × (1 + R2/240Ω)
- R2 = _____ Ω

## 🔧 Übung 3: Vergleich Linear vs. Schaltregler (nur berechnen)

### Szenario: 12V → 3,3V bei 500mA Last

**Linearregler-Lösung:**
- Eingangsspannung: 12V
- Ausgangsspannung: 3,3V
- Laststrom: 500mA

**Berechnungen:**
1. **Ausgangsleistung:**
   - P_aus = U_aus × I_Last = 3,3V × 0,5A = _____ W

2. **Eingangsleistung:**
   - P_ein = U_ein × I_Last = 12V × 0,5A = _____ W

3. **Verlustleistung:**
   - P_Verlust = P_ein - P_aus = _____ W - _____ W = _____ W

4. **Wirkungsgrad:**
   - η = (P_aus / P_ein) × 100% = _____ %

**Schaltregler-Lösung (angenommen η = 90%):**

1. **Ausgangsleistung:**
   - P_aus = 3,3V × 0,5A = _____ W

2. **Eingangsleistung:**
   - P_ein = P_aus / η = _____ W / 0,90 = _____ W

3. **Verlustleistung:**
   - P_Verlust = P_ein - P_aus = _____ W

4. **Eingangsstrom:**
   - I_ein = P_ein / U_ein = _____ W / 12V = _____ A

### Vergleich:

| Parameter | Linearregler | Schaltregler |
|-----------|--------------|--------------|
| Wirkungsgrad | _____ % | 90% |
| Verlustleistung | _____ W | _____ W |
| Eingangsstrom | 500mA | _____ mA |
| Wärmeabfuhr | Groß | Klein |

## 🧮 Rechenübungen

### Aufgabe 1: Kühler für 7805 dimensionieren

Ein 7805 versorgt eine Last mit 1A bei 5V. Die Eingangsspannung beträgt 15V.

**Gegeben:**
- U_ein = 15V
- U_aus = 5V
- I_aus = 1A
- T_Umgebung = 25°C
- T_max (7805) = 125°C
- Thermischer Widerstand Junction-to-Case: R_thJC = 5°C/W
- Thermischer Widerstand Case-to-Heatsink: R_thCH = 1°C/W

**Gesucht:** 
a) Verlustleistung
b) Maximal zulässiger thermischer Widerstand des Kühlkörpers

**Lösung:**

a) **Verlustleistung:**
- P_Verlust = (U_ein - U_aus) × I_aus
- P_Verlust = (15V - 5V) × 1A = _____ W

b) **Thermischer Widerstand:**
- T_Junction = T_Umgebung + P_Verlust × (R_thJC + R_thCH + R_thHA)
- 125°C = 25°C + 10W × (5°C/W + 1°C/W + R_thHA)
- R_thHA = (100°C / 10W) - 6°C/W = _____ °C/W

**Ein Kühlkörper mit ≤ 4°C/W ist erforderlich!**

### Aufgabe 2: Vergleich Energieverbrauch

Ein Gerät benötigt 3,3V bei 2A. Verfügbar ist eine 12V Quelle.

**Option A: Linearregler**

1. **Ausgangsleistung:**
   - P_aus = 3,3V × 2A = _____ W

2. **Verlustleistung:**
   - P_Verlust = (12V - 3,3V) × 2A = _____ W

3. **Gesamtleistung:**
   - P_gesamt = _____ W

4. **Energiekosten pro Jahr** (bei 0,30€/kWh, 24/7 Betrieb):
   - E = P_gesamt × 8760h = _____ kWh
   - Kosten = _____ kWh × 0,30€ = _____ €

**Option B: Schaltregler (η = 90%)**

1. **Ausgangsleistung:**
   - P_aus = _____ W

2. **Eingangsleistung:**
   - P_ein = P_aus / 0,90 = _____ W

3. **Verlustleistung:**
   - P_Verlust = _____ W - _____ W = _____ W

4. **Energiekosten pro Jahr:**
   - E = _____ W × 8760h / 1000 = _____ kWh
   - Kosten = _____ €

**Ersparnis pro Jahr:** _____ € - _____ € = _____ €

### Aufgabe 3: USB-Ladeadapter

Ein USB-Ladeadapter soll 5V bei 2,1A (10,5W) liefern. Eingangsspannung: 230V AC → 12V DC.

**Mit Linearregler:**
1. **Verlustleistung:**
   - P_Verlust = (12V - 5V) × 2,1A = _____ W

2. **Gesamtleistung:**
   - P_gesamt = _____ W + _____ W = _____ W

3. **Wirkungsgrad:**
   - η = _____ %

**Mit Schaltregler (η = 92%):**
1. **Eingangsleistung:**
   - P_ein = 10,5W / 0,92 = _____ W

2. **Verlustleistung:**
   - P_Verlust = _____ W

**Warum verwenden moderne USB-Adapter Schaltregler?**
- Antwort: _____

## 🎯 Praktisches Anwendungsbeispiel: Rechenzentrum

### Anwendung 1: Servernetzteil (ATX)

Moderne ATX-Netzteile sind **Schaltregler-basiert** und liefern mehrere Spannungen:

**Ausgangsspannungen:**
- +12V (Hauptversorgung CPU, GPU)
- +5V (Peripherie, USB)
- +3,3V (RAM, Mainboard)
- -12V (alte Schnittstellen)
- +5V Standby (immer aktiv)

**Typische Wirkungsgrade:**
- 80 PLUS Standard: ≥ 80%
- 80 PLUS Bronze: ≥ 85%
- 80 PLUS Gold: ≥ 90%
- 80 PLUS Platinum: ≥ 92%
- 80 PLUS Titanium: ≥ 94%

**Beispielrechnung** (500W Netzteil, 80% Last, Gold):

Bei 400W Ausgangsleistung:
- η = 90%
- P_ein = 400W / 0,90 = _____ W
- P_Verlust = _____ W
- Wärmeabfuhr erforderlich: _____ W

### Anwendung 2: Raspberry Pi Stromversorgung

**Anforderung:** 5V bei 3A (15W)

**Option A: 9V + Linearregler 7805**
- Verlustleistung: (9V - 5V) × 3A = _____ W
- ❌ **Zu hohe Wärme!** Nicht praktikabel

**Option B: USB-Netzteil (Schaltregler)**
- Eingangsspannung: 230V AC
- Ausgangsspannung: 5V DC
- Wirkungsgrad: ~85%
- P_ein = 15W / 0,85 = _____ W
- P_Verlust = _____ W
- ✅ **Geringe Wärme**, kompakt, effizient

### Anwendung 3: LED-Beleuchtung im Serverraum

**Anforderung:** 24V LED-Streifen, 2A (48W)

**Verfügbar:** 230V AC Netzspannung

**Lösung:**
1. **AC/DC Schaltnetzteil:** 230V AC → 24V DC
2. **Wirkungsgrad:** ~88%
3. **Eingangsleistung:** 48W / 0,88 = _____ W
4. **Wärmeentwicklung:** _____ W

**Warum nicht Linearregler?**
- Linearregler brauchen DC-Eingang
- Bei hoher Leistung (48W) wäre die Verlustleistung zu hoch
- Schaltnetzteil ist die einzige praktikable Lösung

## 📊 Entscheidungshilfe: Linear vs. Schaltregler

### Wann Linearregler verwenden?

✅ **Geringe Spannungsdifferenz** (z.B. 6V → 5V)
✅ **Niedriger Strom** (< 500mA)
✅ **Sehr saubere Spannung** erforderlich (Audio, Sensoren)
✅ **Einfachheit und Kosten** sind wichtig
✅ **Geringes EMV-Problem** erforderlich
✅ **Kleine Bauform** ohne Spule gewünscht

**Beispiele:**
- Batterieversorgung für Sensoren (9V → 5V, 50mA)
- Audio-Vorverstärker (Low-Noise)
- Referenzspannungen für ADC

### Wann Schaltregler verwenden?

✅ **Große Spannungsdifferenz** (z.B. 24V → 5V)
✅ **Hoher Strom** (> 500mA)
✅ **Hoher Wirkungsgrad** erforderlich
✅ **Spannungserhöhung** benötigt (Boost)
✅ **Geringe Wärmeentwicklung** gewünscht
✅ **Batterielaufzeit** optimieren

**Beispiele:**
- USB-Netzteile (230V → 5V, 2A)
- Laptop-Netzteile (230V → 19V, 3A)
- LED-Treiber (12V → 24V)
- Batteriegespeiste Geräte

### Kombinierte Lösungen

**Häufig verwendet:**
1. **Schaltregler** für grobe Spannungswandlung (Hauptversorgung)
2. **Linearregler** für empfindliche Komponenten (Endstufe)

**Beispiel:**
```
230V AC → [Schaltnetzteil] → 12V DC → [LDO Linearregler] → 3,3V (Mikrocontroller)
                                    ↓
                             [Schaltregler] → 5V (Peripherie)
```

**Vorteile:**
- ✅ Hohe Effizienz durch Schaltregler
- ✅ Saubere Spannung durch Linearregler
- ✅ Optimale Lösung für Mixed-Signal Systeme

## ⚡ Besondere Regler-Typen

### Low-Dropout (LDO) Regler

**Spezielle Linearregler** mit sehr geringer Dropout-Spannung (0,1-0,4V statt 2-3V).

**Vorteil:** Kann z.B. aus 3,6V (Akku) noch 3,3V erzeugen

**Beispiele:**
- LM1117-3.3 (3,3V, Dropout: 1,2V)
- AMS1117 (einstellbar, Dropout: 1,3V)
- MCP1700 (3,3V, Dropout: 0,178V) ← Low-Dropout!

**Anwendung:** 
- Batteriebetriebene Geräte
- Wenn Eingangsspannung nur knapp über Ausgang

### Buck-Boost Converter

**Kann Spannung erhöhen ODER senken:**

```
Eingangsspannung: 5-12V
Ausgangsspannung: 9V (konstant)
```

**Anwendung:**
- Akkubetrieb (Spannung sinkt von 12V auf 9V)
- Flexibles Eingangsspannungsbereich
- Automotive (8-16V → 12V)

### Invertierende Regler

**Erzeugen negative Spannung:**

```
+12V → -12V
```

**Anwendung:**
- Operationsverstärker (benötigen ±12V)
- Analoge Schaltungen
- LCD-Displays

## 🔍 Typische Probleme und Lösungen

### Problem 1: Linearregler überhitzt

**Symptome:**
- Regler wird sehr heiß (>100°C)
- Thermische Abschaltung
- Reduzierte Ausgangsspannung

**Ursachen:**
- Zu hoher Laststrom
- Zu große Eingangsspannung
- Unzureichende Kühlung

**Lösungen:**
1. **Kühlkörper** anbringen
2. **Eingangsspannung** reduzieren
3. Auf **Schaltregler** umsteigen
4. **Last** reduzieren

### Problem 2: Schaltregler erzeugt Störungen

**Symptome:**
- Hochfrequentes Rauschen
- Störungen in Audio/Video
- EMV-Probleme

**Lösungen:**
1. **Bessere Abschirmung**
2. **Größere Ausgangskondensatoren**
3. **LC-Filter** am Ausgang
4. **Ferritkerne** auf Leitungen
5. **Linearregler** als Nachfilter

### Problem 3: Ausgangsspannung instabil

**Linearregler:**
- **Eingangs-Kondensator** fehlt (100nF)
- **Ausgangs-Kondensator** fehlt (10μF)
- **Dropout** unterschritten

**Schaltregler:**
- **Falsche Spule** gewählt
- **Kondensatoren zu klein**
- **Schaltfrequenz** falsch eingestellt

## ✅ Selbstüberprüfung

1. **Ein Linearregler wandelt überschüssige Spannung in:**
   ☐ Magnetfeld
   ☐ Wärme
   ☐ Licht

2. **Der Wirkungsgrad eines 7805 bei 12V Eingang beträgt ca.:**
   ☐ 90%
   ☐ 42%
   ☐ 75%

3. **Schaltregler können:**
   ☐ nur Spannung reduzieren
   ☐ nur Spannung erhöhen
   ☐ Spannung reduzieren und erhöhen

4. **Welcher Regler ist für 24V → 5V bei 3A am effizientesten?**
   ☐ Linearregler 7805
   ☐ Buck-Schaltregler
   ☐ Boost-Converter

5. **Die Dropout-Spannung ist:**
   ☐ die Ausgangsspannung
   ☐ die minimale Differenz U_ein - U_aus
   ☐ die maximale Verlustleistung

6. **Ein 80 PLUS Gold Netzteil hat mindestens:**
   ☐ 80% Wirkungsgrad
   ☐ 90% Wirkungsgrad
   ☐ 95% Wirkungsgrad

7. **Für rauscharme Anwendungen (Audio) eignet sich:**
   ☐ Schaltregler
   ☐ Linearregler
   ☐ Buck-Boost Converter

8. **Die Verlustleistung eines Linearreglers berechnet sich:**
   ☐ P = U_aus × I_aus
   ☐ P = (U_ein - U_aus) × I_aus
   ☐ P = U_ein / I_aus

## 🎯 Lösungen

### Tinkercad-Übungen:

**Übung 1: 7805**
- U_aus = 5V
- Wirkungsgrad = 41,7%
- Mit 100Ω Last: P_Verlust = 7W × 0,05A = 0,35W
- Regler wird warm

**Übung 2: LM317**
- Bei R2 = 240Ω: U_aus = 2,5V
- Bei R2 = 1000Ω: U_aus = 6,46V
- Für U_aus = 9V: R2 = 1.488Ω (≈1,5kΩ)

**Übung 3: Vergleich**
- Linearregler: η = 27,5%, P_Verlust = 4,35W
- Schaltregler: P_Verlust = 0,18W
- Schaltregler ist **24× effizienter!**

### Rechenübungen:

**Aufgabe 1:**
- a) P_Verlust = 10W
- b) R_thHA = 4°C/W

**Aufgabe 2:**
- Linearregler: 210,7 kWh/Jahr = 63,21€
- Schaltregler: 63,9 kWh/Jahr = 19,17€
- **Ersparnis: 44,04€ pro Jahr!**

**Aufgabe 3:**
- Linearregler: P_Verlust = 14,7W, η = 41,7%
- Schaltregler: P_Verlust = 0,91W, η = 92%
- **Schaltregler = weniger Wärme, höhere Effizienz, kompaktere Bauform**

### Praktische Beispiele:

**500W Netzteil (Gold):**
- P_ein = 444W
- P_Verlust = 44W

**Raspberry Pi:**
- 9V + 7805: P_Verlust = 12W ❌
- USB-Netzteil: P_ein = 17,6W, P_Verlust = 2,6W ✅

**LED-Beleuchtung:**
- P_ein = 54,5W
- P_Verlust = 6,5W

### Selbstüberprüfung:

1. ✅ Wärme
2. ✅ 42%
3. ✅ Spannung reduzieren und erhöhen (je nach Typ)
4. ✅ Buck-Schaltregler
5. ✅ die minimale Differenz U_ein - U_aus
6. ✅ 90% Wirkungsgrad
7. ✅ Linearregler
8. ✅ P = (U_ein - U_aus) × I_aus

---

## 📝 Notizen

Platz für deine eigenen Aufzeichnungen und Erkenntnisse:

```
Vergleich Linear- vs. Schaltregler:

Linearregler:
- Prinzip: Variabler Widerstand
- Wirkungsgrad: η = U_aus / U_ein
- Verlustleistung: P = (U_ein - U_aus) × I
- Vorteil: Einfach, rauscharm
- Nachteil: Wärme, niedriger Wirkungsgrad

Schaltregler:
- Prinzip: Schnelles Schalten + Energiespeicherung
- Wirkungsgrad: 80-95%
- Typen: Buck (Down), Boost (Up), Buck-Boost
- Vorteil: Effizient, geringe Wärme
- Nachteil: Komplex, EMV-Probleme

Entscheidungskriterien:
- Spannungsdifferenz groß → Schaltregler
- Hoher Strom → Schaltregler
- Rauscharme Anwendung → Linearregler
- Batteriebetrieb → Schaltregler (Effizienz!)
```

## 🏆 Abschluss des gesamten Lernmoduls

**Herzlichen Glückwunsch!** Du hast alle 9 Lernschritte erfolgreich absolviert!

**Du hast gelernt:**
- ✅ **Grundgrößen:** Spannung, Strom, Widerstand, Leistung
- ✅ **Gesetze:** Ohm'sches Gesetz, Kirchhoff'sche Regeln
- ✅ **Schaltungen:** Reihe, Parallel, Gemischt, Spannungsteiler, Brücke
- ✅ **Spannungsversorgung:** Linear- und Schaltregler

**Du kannst jetzt:**
- 🔧 Elektrische Schaltungen analysieren und dimensionieren
- 📊 Berechnungen für IT-Systeme durchführen
- ⚡ Die richtige Spannungsversorgung auswählen
- 🎯 Effiziente und zuverlässige Stromversorgungen planen

**🎉 Du bist jetzt bestens vorbereitet für die elektrischen Herausforderungen als Informationstechnischer Assistent!**

---

## 📈 Dein Lernfortschritt

### ✅ Grundlagen-Checkliste Lernschritt 9
- [ ] Linear- und Schaltregler verstehen
- [ ] Wirkungsgrade berechnen können
- [ ] Verlustleistung und Kühlung dimensionieren
- [ ] 7805 Linearregler-Schaltung aufbauen
- [ ] LM317 einstellbaren Regler berechnen
- [ ] Vergleich Linear vs. Schaltregler durchführen
- [ ] Anwendungsbeispiele verstehen
- [ ] Selbsttest bestanden

### 🎯 Gesamtmodul abgeschlossen
- [ ] Alle 9 Lernschritte durchgearbeitet
- [ ] Tinkercad-Übungen erfolgreich absolviert
- [ ] Rechenübungen verstanden
- [ ] Praktische IT-Anwendungen erkannt

**🚀 Bereit für die Praxis im IT-Bereich!**
