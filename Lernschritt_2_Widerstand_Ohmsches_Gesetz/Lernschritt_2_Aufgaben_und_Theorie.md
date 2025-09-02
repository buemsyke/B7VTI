# Lernschritt 2: Widerstand und Ohm'sches Gesetz
## 🎯 Handlungssituation: Verkabelung und Leitungswiderstände

Der Elektriker des Rechenzentrums hat dich zu sich gerufen. Er erklärt dir, dass die Länge und der Durchmesser der Stromkabel einen entscheidenden Einfluss auf die Spannungsversorgung haben. Für die korrekte Dimensionierung der Verkabelung zu den Serverschränken musst du verstehen, wie sich Widerstand auf Spannung und Strom auswirkt.

**Deine heutige Mission:**
- Das Ohm'sche Gesetz verstehen und anwenden
- Verschiedene Widerstände messen und berechnen
- Den Einfluss von Leitungswiderständen auf die Stromversorgung untersuchen

## 📖 Fachwissen: Widerstand und Ohm'sches Gesetz

### Was ist elektrischer Widerstand?

**Widerstand (R)** ist der "Widerstand", den ein Material dem Stromfluss entgegensetzt. Er wird in **Ohm (Ω)** gemessen.

**Analogie**: Stell dir Widerstand wie eine Engstelle in einem Wasserrohr vor:
- Enge Stelle → wenig Wasser fließt durch → hoher Widerstand
- Weite Stelle → viel Wasser fließt durch → niedriger Widerstand

**Widerstand in der IT:**
- **Kupferkabel:** sehr niedrig (0,001-1Ω)
- **LED-Schutzwiderstand:** 220-1000Ω  
- **Pull-up Widerstand:** 1.000-10.000Ω (1-10kΩ)
- **Isolation:** sehr hoch (>1.000.000Ω = 1MΩ)

### Das Ohm'sche Gesetz - Das wichtigste Gesetz der Elektrotechnik!

Das Ohm'sche Gesetz beschreibt den Zusammenhang zwischen Spannung (U), Strom (I) und Widerstand (R):

```
U = R × I
```

**Drei Varianten der Formel:**
- **U = R × I** (Spannung berechnen)
- **I = U / R** (Strom berechnen)  
- **R = U / I** (Widerstand berechnen)

**Merkhilfe - das "URI-Dreieck":**
```
    U
   ---
  R | I
```
*Halte das gesuchte ab, multipliziere die anderen beiden oder teile oberes durch unteres*

### Wichtige Symbole und Einheiten

| Größe | Symbol | Einheit | Einheitenzeichen |
|-------|---------|---------|------------------|
| Spannung | U | Volt | V |
| Strom | I | Ampere | A |
| Widerstand | R | Ohm | Ω |

### Präfixe für Widerstände

| Präfix | Symbol | Faktor | Beispiel |
|--------|---------|--------|----------|
| Kilo | k | 1.000 | 4,7kΩ = 4.700Ω |
| Mega | M | 1.000.000 | 2,2MΩ = 2.200.000Ω |

## 🔧 Tinkercad-Übung 1: Ohm'sches Gesetz experimentell überprüfen

### Schaltung aufbauen

```
9V Batterie (+) → Widerstand (470Ω) → LED → 9V Batterie (-)
```

### Komponenten:
- 1x 9V Batterie
- 1x LED (rot)
- 1x Widerstand 470Ω
- 2x Multimeter
- Verbindungsdrähte

### Messungen durchführen:

1. **Spannungsmessung am Widerstand:**
   - Voltmeter parallel zum Widerstand
   - Gemessene Spannung: _____ V

2. **Strommessung:**
   - Amperemeter in Reihe zur Schaltung
   - Gemessener Strom: _____ A

3. **Berechne den Widerstand mit dem Ohm'schen Gesetz:**
   - R = U / I = _____ V / _____ A = _____ Ω
   - Vergleiche mit dem theoretischen Wert (470Ω)

## 🔧 Tinkercad-Übung 2: Verschiedene Widerstände testen

Baue nacheinander Schaltungen mit verschiedenen Widerständen auf und miss jeweils Spannung und Strom:

| Widerstand | Spannung am R | Strom | Berechneter R |
|------------|---------------|-------|---------------|
| 220Ω       | _____ V       | _____ A | _____ Ω     |
| 470Ω       | _____ V       | _____ A | _____ Ω     |
| 1kΩ        | _____ V       | _____ A | _____ Ω     |
| 2,2kΩ      | _____ V       | _____ A | _____ Ω     |

**Beobachtung:** Was passiert mit dem Strom, wenn der Widerstand größer wird?

## 🧮 Rechenübungen

### Aufgabe 1: Server-Netzteil
Ein Server-Netzteil liefert 12V. Ein angeschlossener Lüfter nimmt 0,5A auf.

**Gesucht:** Wie groß ist der Widerstand des Lüfters?

**Lösung:**
- Gegeben: U = 12V, I = 0,5A
- Gesucht: R = ?
- Formel: R = U / I
- Rechnung: R = 12V / 0,5A = _____ Ω

### Aufgabe 2: LED-Schaltung
Eine LED soll an 5V betrieben werden. Der LED-Strom soll 20mA betragen. Die LED selbst hat eine Spannung von 2V.

**Gesucht:** Welcher Vorwiderstand ist nötig?

**Lösung:**
- Am Widerstand liegt an: U = 5V - 2V = 3V
- Strom: I = 20mA = 0,02A
- R = U / I = 3V / 0,02A = _____ Ω

### Aufgabe 3: Kabelwiderstand
Ein 50m langes Netzwerkkabel hat einen Widerstand von 0,5Ω. Welche Spannung fällt bei einem Strom von 2A am Kabel ab?

**Lösung:**
- R = 0,5Ω, I = 2A
- U = R × I = _____ V

## 🎯 Praktisches Anwendungsbeispiel: Power over Ethernet (PoE)

**Situation:** Du sollst eine IP-Kamera per PoE mit Strom versorgen. Die Kamera benötigt 12W bei 12V.

**Daten:**
- Spannung am Switch: 48V
- Spannung an der Kamera: 12V  
- Kabellänge: 80m
- Kabelwiderstand: 0,8Ω

**Berechnungen:**

1. **Strom der Kamera:**
   - P = U × I → I = P / U
   - I = 12W / 12V = _____ A

2. **Spannungsfall am Kabel:**
   - U_Kabel = R × I = 0,8Ω × _____ A = _____ V

3. **Benötigte Spannung am Switch:**
   - U_Switch = U_Kamera + U_Kabel = 12V + _____ V = _____ V

**Frage:** Reicht die PoE-Spannung von 48V aus? ☐ Ja ☐ Nein

## ✅ Selbstüberprüfung

1. **Das Ohm'sche Gesetz lautet:**
   ☐ P = U × I
   ☐ U = R × I
   ☐ I = U + R

2. **Bei größerem Widerstand wird der Strom:**
   ☐ größer
   ☐ kleiner  
   ☐ bleibt gleich

3. **Der Widerstand wird gemessen in:**
   ☐ Volt (V)
   ☐ Ampere (A)
   ☐ Ohm (Ω)

4. **4,7kΩ entspricht:**
   ☐ 47Ω
   ☐ 470Ω
   ☐ 4.700Ω

## 🎯 Lösungen

### Rechenübungen:
1. **Server-Lüfter:** R = 12V / 0,5A = **24Ω**
2. **LED-Vorwiderstand:** R = 3V / 0,02A = **150Ω**
3. **Kabelspannung:** U = 0,5Ω × 2A = **1V**

### PoE-Beispiel:
1. **Kamera-Strom:** I = 12W / 12V = **1A**
2. **Kabel-Spannungsfall:** U = 0,8Ω × 1A = **0,8V**
3. **Benötigte Switch-Spannung:** U = 12V + 0,8V = **12,8V**
4. **48V reichen aus:** ✅ **Ja**

### Selbstüberprüfung:
1. ✅ U = R × I
2. ✅ kleiner
3. ✅ Ohm (Ω)
4. ✅ 4.700Ω

## 📊 Widerstandscode (Farbringe)

**Bonus-Wissen:** Widerstände haben oft Farbringe zur Wertbestimmung:

| Farbe | Wert |
|-------|------|
| Schwarz | 0 |
| Braun | 1 |
| Rot | 2 |
| Orange | 3 |
| Gelb | 4 |
| Grün | 5 |
| Blau | 6 |
| Violett | 7 |
| Grau | 8 |
| Weiß | 9 |

**Beispiel:** Rot-Rot-Braun = 2-2-×10 = 220Ω

---

## 📝 Notizen

```
Meine wichtigsten Erkenntnisse zum Ohm'schen Gesetz:
- 
- 
- 

Schwierige Berechnungen üben:
- 
- 
```

**▶️ Verstehst du das Ohm'sche Gesetz? Dann weiter zu Lernschritt 3!**