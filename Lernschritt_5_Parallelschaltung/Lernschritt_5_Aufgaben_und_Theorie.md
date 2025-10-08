# Lernschritt 5: Parallelschaltung
## 🎯 Handlungssituation: Stromversorgung für mehrere Geräte

Der Serverraum nimmt Gestalt an! Jetzt müssen verschiedene Geräte parallel an die Stromversorgung angeschlossen werden: Server, Switches, Monitore und Lüfter. Jedes Gerät soll unabhängig ein- und ausgeschaltet werden können, ohne die anderen zu beeinflussen. Du musst verstehen, wie sich Parallelschaltungen verhalten und wie viel Strom die Hauptzuleitung führen muss.

**Deine Mission heute:**
- Parallelschaltungen verstehen und aufbauen
- Stromaufteilung in parallelen Zweigen berechnen
- Gesamtwiderstand von Parallelschaltungen ermitteln
- Ausfallsicherheit gegenüber Reihenschaltung bewerten

## 📖 Fachwissen: Parallelschaltung

### Was ist eine Parallelschaltung?

In einer **[Parallelschaltung](https://falstad.com/circuit/circuitjs.html?ctz=CQAgLCAMB0l3BWEBGGAmOaDsWDMkAONANgE5SsQFIqqaEBTAWmWQCgA3EDAkfCHijS8aNMDVRQpMBGwDu3QkN64MyqGwBOfNcjARVE0minVIWnTTTjL3AiLrmFh9S70Qnt-opWQPbAAdwOG4bcSt7PmkUeFj5YKsbF2tRePC7FTVhETSQ5GNbfJNPdPdC-Q0g0orSgtxo1Fi4eOTIl29zIORhFALu3hSo0Rimz37ek3HxsZ7B8Y74+b8fPmWZ3nHBabZcLBo3Oqyk6TYgA)** sind alle Bauteile **nebeneinander** geschaltet. Jedes Bauteil hat einen **eigenen Weg** zur Stromquelle.

```
                  ┌── R₁ ──┐
9V Batterie (+) ──├── R₂ ──┤── Batterie (-)
                  └── R₃ ──┘
```

### Gesetze der Parallelschaltung

Verändere die Widerstandswerte in der **[Parallelschaltung](https://falstad.com/circuit/circuitjs.html?ctz=CQAgLCAMB0l3BWEBGGAmOaDsWDMkAONANgE5SsQFIqqaEBTAWmWQCgA3EDAkfCHijS8aNMDVRQpMBGwDu3QkN64MyqGwBOfNcjARVE0minVIWnTTTjL3AiLrmFh9S70Qnt-opWQPbAAdwOG4bcSt7PmkUeFj5YKsbF2tRePC7FTVhETSQ5GNbfJNPdPdC-Q0g0orSgtxo1Fi4eOTIl29zIORhFALu3hSo0Rimz37ek3HxsZ7B8Y74+b8fPmWZ3nHBabZcLBo3Oqyk6TYgA)** und überprüfe die folgenden Aussagen:

#### 1. Spannung ist überall gleich
```
U_gesamt = U₁ = U₂ = U₃ = ...
```
**Warum?** Alle Bauteile sind direkt mit der Stromquelle verbunden.

#### 2. Ströme addieren sich
```
I_gesamt = I₁ + I₂ + I₃ + ...
```
**Warum?** Der Gesamtstrom teilt sich auf die einzelnen Zweige auf.

#### 3. Gesamtwiderstand wird kleiner
```
1/R_gesamt = 1/R₁ + 1/R₂ + 1/R₃ + ...
```
**Warum?** Jeder parallele Zweig bietet einen zusätzlichen Weg für den Strom.

### Vereinfachte Formel für zwei Widerstände:
```
R_gesamt = (R₁ × R₂) / (R₁ + R₂)
```
**Merkspruch:** "Produkt durch Summe"

### Vor- und Nachteile der Parallelschaltung

**Vorteile:**
✅ Jedes Gerät kann einzeln geschaltet werden
✅ Fällt ein Gerät aus → andere arbeiten weiter
✅ Alle Geräte haben gleiche Spannung
✅ Niedrigerer Gesamtwiderstand

**Nachteile:**
❌ Mehr Kabel nötig  
❌ Höherer Gesamtstrom
❌ Höhere Leistungsaufnahme
❌ Dickere Hauptzuleitung erforderlich

## 🔧 Tinkercad-Übung 1: Drei LEDs parallel

### Schaltung aufbauen

```
                  ┌── R₁(470Ω) ── LED₁ ──┐
9V Batterie (+) ──├── R₂(470Ω) ── LED₂ ──┤── Batterie (-) 
                  └── R₃(470Ω) ── LED₃ ──┘
```

### Komponenten:
- 1× 9V Batterie
- 3× LEDs (rot)  
- 3× Widerstände 470Ω
- Multimeter
- Verbindungsdrähte

### Spannungsmessungen:

1. **Spannung über LED₁:** _____ V
2. **Spannung über LED₂:** _____ V
3. **Spannung über LED₃:** _____ V
4. **Batteriespannung:** _____ V

**Beobachtung:** Sind alle Spannungen gleich? ☐ Ja ☐ Nein

### Strommessungen:

5. **Strom durch LED₁:** _____ A
6. **Strom durch LED₂:** _____ A
7. **Strom durch LED₃:** _____ A  
8. **Gesamtstrom (von der Batterie):** _____ A

**Rechnung:** I₁ + I₂ + I₃ = _____ A (sollte dem Gesamtstrom entsprechen)

### Experiment: LED entfernen
9. **Entferne LED₂ und miss erneut:**
   - Strom durch LED₁: _____ A
   - Strom durch LED₃: _____ A
   - **Beobachtung:** Ändern sich die anderen LEDs? ☐ Ja ☐ Nein

## 🔧 Tinkercad-Übung 2: Widerstandsberechnung

Baue eine Parallelschaltung mit drei verschiedenen Widerständen:

```
                  ┌── R₁(220Ω) ──┐
9V Batterie (+) ──├── R₂(470Ω) ──┤── Batterie (-) 
                  └── R₃(1kΩ) ───┘
```

### Berechnungen VOR der Messung:

1. **Gesamtwiderstand berechnen:**
   - 1/R_ges = 1/220Ω + 1/470Ω + 1/1000Ω
   - 1/R_ges = 0,00455 + 0,00213 + 0,001 = _____ (1/Ω)
   - R_ges = 1 / _____ = _____ Ω

2. **Erwarteter Gesamtstrom:**
   - I_ges = U / R_ges = 9V / _____ Ω = _____ A

3. **Einzelströme berechnen:**
   - I₁ = 9V / 220Ω = _____ A
   - I₂ = 9V / 470Ω = _____ A  
   - I₃ = 9V / 1000Ω = _____ A
   - Summe: I₁ + I₂ + I₃ = _____ A

### Messungen zur Kontrolle:
4. **Tatsächlicher Gesamtstrom:** _____ A
5. **Tatsächlicher Strom I₁:** _____ A
6. **Tatsächlicher Strom I₂:** _____ A
7. **Tatsächlicher Strom I₃:** _____ A

## 🧮 Rechenübungen

### Aufgabe 1: Server-Rack Stromversorgung
An einen 230V Stromkreis werden parallel angeschlossen:
- Server 1: 800W
- Server 2: 1200W  
- Monitor: 150W
- Switch: 50W

**Gesucht:** Gesamtstrom der Zuleitung

**Lösung:**
1. **Einzelströme berechnen:**
   - I_Server1 = P / U = 800W / 230V = _____ A
   - I_Server2 = 1200W / 230V = _____ A
   - I_Monitor = 150W / 230V = _____ A  
   - I_Switch = 50W / 230V = _____ A

2. **Gesamtstrom:**
   - I_gesamt = _____ A + _____ A + _____ A + _____ A = _____ A

3. **Benötigte Sicherung (mit 25% Reserve):**
   - I_Sicherung = _____ A × 1,25 = _____ A

### Aufgabe 2: LED-Parallelschaltung
4 LEDs sollen parallel an 12V betrieben werden. Jede LED benötigt 2V bei 20mA.

**Gegeben:**
- 4 LEDs parallel
- Versorgung: 12V
- LED-Daten: 2V, 20mA
- Gesucht: Vorwiderstand pro LED, Gesamtstrom

**Lösung:**
1. **Spannung am Vorwiderstand:**
   - U_R = 12V - 2V = _____ V

2. **Vorwiderstand pro LED:**
   - R = U / I = _____ V / 0,02A = _____ Ω

3. **Gesamtstrom:**
   - I_gesamt = 4 × 0,02A = _____ A

### Aufgabe 3: Gesamtwiderstand berechnen
Zwei Widerstände R₁ = 120Ω und R₂ = 180Ω werden parallel geschaltet.

**Gesucht:** Gesamtwiderstand

**Lösung (Methode 1 - Formel):**
- R_ges = (R₁ × R₂) / (R₁ + R₂)
- R_ges = (120Ω × 180Ω) / (120Ω + 180Ω) = _____ Ω

**Lösung (Methode 2 - Kehrwerte):**
- 1/R_ges = 1/120Ω + 1/180Ω = _____ + _____ = _____
- R_ges = 1 / _____ = _____ Ω

## 🎯 Praktisches Anwendungsbeispiel: Rechenzentrum Stromverteilung

**Situation:** Ein Serverraum hat 3 getrennte Stromkreise mit je 16A Absicherung (230V). Die Geräte sollen optimal auf die Stromkreise verteilt werden.

**Geräte:**
- 8× Server à 600W
- 4× Switches à 100W  
- 2× Klimageräte à 2000W
- 1× Beleuchtung 300W

### Berechnung pro Stromkreis:

**Stromkreis 1 - Server:**
- 3× Server = 3 × 600W = 1800W
- Strom: I = 1800W / 230V = _____ A
- Reserve: 16A - _____ A = _____ A (für weitere Server)

**Stromkreis 2 - Infrastruktur:**
- 5× Server = 5 × 600W = 3000W  
- 4× Switches = 4 × 100W = 400W
- Beleuchtung = 300W
- Gesamt: _____ W
- Strom: I = _____ W / 230V = _____ A
- Bewertung: ☐ OK ☐ Überlast

**Stromkreis 3 - Kühlung:**
- 2× Klimageräte = 2 × 2000W = 4000W
- Strom: I = 4000W / 230V = _____ A  
- Bewertung: ☐ OK ☐ Überlast

**Optimierung:** Wie würdest du die Geräte besser verteilen?

## 🔌 Spezialfall: Gleiche Widerstände parallel

**Bei n gleichen Widerständen parallel:**
```
R_gesamt = R / n
```

**Beispiel:** 4× 1000Ω parallel:
- R_gesamt = 1000Ω / 4 = 250Ω
- Der Gesamtwiderstand ist ¼ des Einzelwiderstands!

## ✅ Selbstüberprüfung

1. **In einer Parallelschaltung ist die Spannung:**
   ☐ überall gleich
   ☐ überall unterschiedlich  
   ☐ am Ende am kleinsten

2. **In einer Parallelschaltung addieren sich:**
   ☐ die Spannungen
   ☐ die Ströme
   ☐ die Widerstände

3. **Der Gesamtwiderstand einer Parallelschaltung ist:**
   ☐ größer als der größte Einzelwiderstand
   ☐ kleiner als der kleinste Einzelwiderstand
   ☐ der Mittelwert aller Widerstände

4. **Fällt in einer Parallelschaltung ein Gerät aus:**
   ☐ fällt die ganze Schaltung aus
   ☐ arbeiten die anderen Geräte weiter
   ☐ werden die anderen Geräte heller

## 🎯 Lösungen

### Rechenübungen:
1. **Server-Rack:** I = 3,48A + 5,22A + 0,65A + 0,22A = **9,57A**, Sicherung: **12A**
2. **LED-Parallel:** U_R = 10V, R = 500Ω, I_gesamt = 0,08A  
3. **Gesamtwiderstand:** R_ges = **72Ω** (beide Methoden)

### Rechenzentrum-Beispiel:
- **Stromkreis 1:** I = 7,83A, Reserve = 8,17A ✓
- **Stromkreis 2:** 3700W, I = 16,09A ❌ **Überlast!**
- **Stromkreis 3:** I = 17,39A ❌ **Überlast!**

**Optimierung:** Switches und Beleuchtung zu Stromkreis 1 verschieben!

### Selbstüberprüfung:
1. ✅ überall gleich
2. ✅ die Ströme  
3. ✅ kleiner als der kleinste Einzelwiderstand
4. ✅ arbeiten die anderen Geräte weiter

## 📊 Vergleich: Reihen- vs. Parallelschaltung

| Eigenschaft | Reihenschaltung | Parallelschaltung |
|-------------|----------------|-------------------|
| Spannung | teilt sich auf | überall gleich |
| Strom | überall gleich | teilt sich auf |
| Widerstand | R₁ + R₂ + R₃ | kleiner als kleinster |
| Ausfall | alles aus | andere arbeiten weiter |
| Anwendung | Spannungsteiler | Hausinstallation |

---

## 📝 Notizen

```
Meine Erkenntnisse zu Parallelschaltungen:
- Spannung überall gleich: U₁ = U₂ = U₃ = U_ges
- Ströme addieren sich: I_ges = I₁ + I₂ + I₃
- Gesamtwiderstand: 1/R_ges = 1/R₁ + 1/R₂ + 1/R₃  
- Vorteil: Ausfallsicher, einzeln schaltbar

Anwendungen in der IT:
- Hausinstallation (Steckdosen)
- Server-Racks (einzeln schaltbar)  
- Redundante Systeme
- LED-Arrays mit einzelner Helligkeitsregelung
```

**▶️ Parallelschaltung verstanden? Weiter zu gemischten Schaltungen in Lernschritt 6!**
