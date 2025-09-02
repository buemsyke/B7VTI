# Lernschritt 7: Spannungsteiler
## 🎯 Handlungssituation: Sensorauswertung und Signalaufbereitung

Das Rechenzentrum soll mit einem Überwachungssystem ausgestattet werden. Temperatursensoren, Feuchtigkeitssensoren und Spannungsüberwachung müssen an ein Monitoring-System angeschlossen werden. Viele Sensoren liefern jedoch andere Spannungen als das System verarbeiten kann. Du musst lernen, wie Spannungsteiler funktionieren, um Sensorsignale richtig anzupassen.

**Deine heutige Mission:**
- Spannungsteiler verstehen und berechnen
- Belastungseffekte bei Spannungsteilern analysieren  
- Sensorschaltungen mit Spannungsteilern aufbauen
- Potentiometer als variable Spannungsteiler einsetzen

## 📖 Fachwissen: Spannungsteiler

### Was ist ein Spannungsteiler?

Ein **Spannungsteiler** teilt eine größere Spannung in kleinere Teilspannungen auf. Er besteht aus mindestens **zwei Widerständen in Reihe**.

**Grundschaltung:**
```
U_ein ──┬── R₁ ──┐
        │        │
        ├── R₂ ──┤ U_aus
        │        │
        └────────┘
```

### Spannungsteiler-Formel

Die Ausgangsspannung berechnet sich nach der **Spannungsteiler-Regel**:

```
U_aus = U_ein × (R₂ / (R₁ + R₂))
```

**Merkspruch:** *"Die Ausgangsspannung ist der Eingangsspannung mal dem Verhältnis vom unteren Widerstand zur Summe beider Widerstände"*

### Wichtige Eigenschaften

#### 1. Spannungsverhältnis
```
U_aus / U_ein = R₂ / (R₁ + R₂)
```
Das Verhältnis hängt nur von den Widerständen ab, nicht von der absoluten Spannung!

#### 2. Strom durch beide Widerstände
```
I = U_ein / (R₁ + R₂)
```
Der gleiche Strom fließt durch beide Widerstände (Reihenschaltung).

#### 3. Leistungsverbrauch
```
P_gesamt = U_ein × I = U_ein² / (R₁ + R₂)
```
Der Spannungsteiler verbraucht permanent Strom!

## 🔧 Tinkercad-Übung 1: Einfacher Spannungsteiler

### Schaltung aufbauen

```
12V ──┬── R₁(1kΩ) ──┐
      │             │
      ├── R₂(2kΩ) ──┤ U_aus
      │             │  
      └─────────────┘
```

### Berechnung VOR dem Aufbau:

1. **Erwartete Ausgangsspannung:**
   - U_aus = 12V × (2kΩ / (1kΩ + 2kΩ))
   - U_aus = 12V × (2kΩ / 3kΩ) = _____ V

2. **Strom durch die Widerstände:**
   - I = 12V / (1kΩ + 2kΩ) = 12V / 3kΩ = _____ mA

3. **Leistungsverbrauch:**
   - P = 12V × 4mA = _____ mW

### Messungen:
4. **Tatsächliche Ausgangsspannung:** _____ V
5. **Strom durch R₁:** _____ mA
6. **Strom durch R₂:** _____ mA
7. **Spannung über R₁:** _____ V
8. **Spannung über R₂:** _____ V

**Kontrollrechnung:** U_R1 + U_R2 = _____ V + _____ V = 12V ✓

## 🔧 Tinkercad-Übung 2: Verschiedene Teilerverhältnisse

Baue verschiedene Spannungsteiler auf und miss die Ausgangsspannung:

| R₁ | R₂ | Berechnet U_aus | Gemessen U_aus |
|----|----|-----------------|-----------------| 
| 1kΩ | 1kΩ | 12V × (1/2) = _____ V | _____ V |
| 1kΩ | 3kΩ | 12V × (3/4) = _____ V | _____ V |
| 3kΩ | 1kΩ | 12V × (1/4) = _____ V | _____ V |
| 2kΩ | 1kΩ | 12V × (1/3) = _____ V | _____ V |

**Beobachtung:** Welcher Widerstand bestimmt hauptsächlich die Ausgangsspannung?

## 🔧 Tinkercad-Übung 3: Belastungseffekt

**Was passiert, wenn der Spannungsteiler belastet wird?**

### Aufbau 1: Unbelasteter Teiler
```
12V ── R₁(1kΩ) ── R₂(1kΩ) ── U_aus (erwartet 6V)
```

### Aufbau 2: Belasteter Teiler  
```
12V ── R₁(1kΩ) ── R₂(1kΩ) ──┬── U_aus
                              │
                              R_Last(1kΩ)
                              │
                              └──
```

### Messungen:
1. **Unbelastet:** U_aus = _____ V
2. **Belastet:** U_aus = _____ V

### Erklärung des Effekts:
Bei Belastung entsteht eine **Parallelschaltung** von R₂ und R_Last:
- R₂_ersatz = (R₂ × R_Last) / (R₂ + R_Last) = (1kΩ × 1kΩ) / (1kΩ + 1kΩ) = _____ Ω
- U_aus_neu = 12V × (500Ω / (1kΩ + 500Ω)) = _____ V

**Faustregel:** R_Last sollte mindestens **10× größer** als R₂ sein!

## 🧮 Rechenübungen

### Aufgabe 1: 3,3V aus 5V erzeugen
Ein Mikrocontroller benötigt 3,3V, aber verfügbar sind nur 5V.

**Gesucht:** Spannungsteiler mit R₁ = 1kΩ

**Lösung:**
- Verhältnis: U_aus / U_ein = 3,3V / 5V = 0,66
- 0,66 = R₂ / (1kΩ + R₂)
- 0,66 × (1kΩ + R₂) = R₂
- 660Ω + 0,66 × R₂ = R₂
- 660Ω = R₂ - 0,66 × R₂ = 0,34 × R₂
- R₂ = 660Ω / 0,34 = _____ Ω

**Nächster Standardwert:** _____ Ω

### Aufgabe 2: Temperatursensor auswerten
Ein Temperatursensor ändert seinen Widerstand von 100Ω (0°C) bis 200Ω (100°C). Er ist Teil eines Spannungsteilers mit 5V und R₁ = 1kΩ.

**Gesucht:** 
a) Spannung bei 0°C
b) Spannung bei 100°C  
c) Spannungsänderung pro °C

**Lösung:**
a) **Bei 0°C (R_sensor = 100Ω):**
   - U_aus = 5V × (100Ω / (1000Ω + 100Ω)) = _____ V

b) **Bei 100°C (R_sensor = 200Ω):**
   - U_aus = 5V × (200Ω / (1000Ω + 200Ω)) = _____ V

c) **Änderung:**
   - ΔU = _____ V - _____ V = _____ V für 100°C
   - Pro °C: _____ V / 100°C = _____ mV/°C

### Aufgabe 3: Potentiometer als Spannungsteiler
Ein 10kΩ Potentiometer wird als Spannungsteiler an 12V betrieben. Die Mittelanzapfung steht auf 30% der Gesamtstrecke.

**Gesucht:** Ausgangsspannung

**Lösung:**
- R₁ = 30% von 10kΩ = _____ kΩ
- R₂ = 70% von 10kΩ = _____ kΩ  
- U_aus = 12V × (7kΩ / (3kΩ + 7kΩ)) = _____ V

## 🎯 Praktisches Anwendungsbeispiel: Serverraum-Monitoring

**Situation:** Das Monitoring-System kann nur Spannungen von 0-3V verarbeiten. Verschiedene Sensoren liefern aber unterschiedliche Spannungsbereiche.

### Sensor 1: Temperatursensor (0-5V)
**Anpassung nötig:** 5V → 3V

**Spannungsteiler berechnen:**
- Verhältnis: 3V / 5V = 0,6
- Mit R₁ = 2kΩ: 0,6 = R₂ / (2kΩ + R₂)
- Auflösen: R₂ = _____ kΩ

### Sensor 2: Drucksensor (0-10V)  
**Anpassung nötig:** 10V → 3V

**Spannungsteiler berechnen:**
- Verhältnis: 3V / 10V = 0,3
- Mit R₁ = 7kΩ: 0,3 = R₂ / (7kΩ + R₂)
- Auflösen: R₂ = _____ kΩ

### Sensor 3: Feuchtigkeitssensor (0-12V)
**Anpassung nötig:** 12V → 3V

**Spannungsteiler berechnen:**  
- Verhältnis: _____ 
- R₂ bei R₁ = 9kΩ: R₂ = _____ kΩ

### Schaltung für alle Sensoren:
```
Temp.  (5V) ── 2kΩ ── 3kΩ ──┬── ADC1 (0-3V)
                              │
Druck (10V) ── 7kΩ ── 3kΩ ──├── ADC2 (0-3V)  
                              │
Feucht(12V) ── 9kΩ ── 3kΩ ──└── ADC3 (0-3V)
```

## ⚡ Probleme mit Spannungsteilern

### 1. Belastungseffekt
- **Problem:** Angeschlossene Last verändert die Ausgangsspannung
- **Lösung:** Niederohmige Spannungsteiler oder Operationsverstärker

### 2. Leistungsverlust
- **Problem:** Permanenter Stromfluss → Wärmeverluste  
- **Lösung:** Hochohmige Widerstände verwenden (mA statt A)

### 3. Temperaturabhängigkeit
- **Problem:** Widerstände ändern sich mit der Temperatur
- **Lösung:** Präzisionswiderstände oder Temperaturkompensation

### 4. Rauschen
- **Problem:** Thermisches Rauschen der Widerstände
- **Lösung:** Niedrige Widerstandswerte oder Filterung

## 🔄 Alternative: Schaltregler

**Für höhere Leistungen:** Statt Spannungsteiler → Schaltregler verwenden
- **Vorteil:** Hoher Wirkungsgrad (>90%)
- **Nachteil:** Komplexer, kann elektromagnetische Störungen verursachen

## ✅ Selbstüberprüfung

1. **Die Spannungsteiler-Formel lautet:**
   ☐ U_aus = U_ein × (R₁ / R₂)
   ☐ U_aus = U_ein × (R₂ / (R₁ + R₂))
   ☐ U_aus = U_ein × (R₁ + R₂) / R₂

2. **Bei Belastung eines Spannungsteilers:**
   ☐ steigt die Ausgangsspannung
   ☐ sinkt die Ausgangsspannung  
   ☐ bleibt die Ausgangsspannung gleich

3. **Ein Spannungsteiler verbraucht:**
   ☐ nur Strom wenn belastet
   ☐ immer Strom
   ☐ nie Strom

4. **Für präzise Spannungsteiler sollte die Last sein:**
   ☐ viel kleiner als R₂  
   ☐ viel größer als R₂
   ☐ gleich R₂

## 🎯 Lösungen

### Tinkercad-Übungen:
1. **Einfacher Teiler:** U_aus = 8V, I = 4mA, P = 48mW
2. **Verschiedene Verhältnisse:** 6V, 9V, 3V, 4V
3. **Belastungseffekt:** Unbelastet: 6V, Belastet: 4V

### Rechenübungen:
1. **3,3V aus 5V:** R₂ = 1941Ω ≈ 2kΩ
2. **Temperatursensor:** a) 0,45V, b) 0,83V, c) 3,8mV/°C  
3. **Potentiometer:** U_aus = 8,4V

### Serverraum-Monitoring:
- **Sensor 1:** R₂ = 3kΩ  
- **Sensor 2:** R₂ = 3kΩ
- **Sensor 3:** Verhältnis = 0,25, R₂ = 3kΩ

### Selbstüberprüfung:
1. ✅ U_aus = U_ein × (R₂ / (R₁ + R₂))
2. ✅ sinkt die Ausgangsspannung
3. ✅ immer Strom
4. ✅ viel größer als R₂

## 💡 Anwendungen von Spannungsteilern

**In der IT-Praxis:**
- **Sensorauswertung:** Anpassung von Sensorsignalen
- **Referenzspannungen:** Erzeugen fester Spannungen
- **Pegelwandler:** 5V ↔ 3,3V Anpassung
- **Potentiometer:** Lautstärkeregelung, Helligkeitsregelung  
- **Spannungsüberwachung:** Überwachung hoher Spannungen

---

## 📝 Notizen

```
Spannungsteiler-Formel merken:
U_aus = U_ein × (R_unten / (R_oben + R_unten))

Wichtige Punkte:
- Immer Stromverbrauch vorhanden
- Belastungseffekt beachten (R_Last >> R₂)
- Für hohe Genauigkeit: Präzisionswiderstände
- Für hohe Leistung: Schaltregler statt Spannungsteiler

Anwendungen:
- Sensorauswertung im Servermonitoring
- Pegelwandler für verschiedene Logikspannungen
- Potentiometer für variable Einstellungen
```

**▶️ Spannungsteiler verstanden? Zum Abschluss die Brückenschaltung in Lernschritt 8!**