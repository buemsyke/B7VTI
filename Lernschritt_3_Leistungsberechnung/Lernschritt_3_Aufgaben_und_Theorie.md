# Lernschritt 3: Leistungsberechnung
## 🎯 Handlungssituation: Energieverbrauch der Server berechnen

Der Facility-Manager des Rechenzentrums ist besorgt über die Stromkosten. Er hat dich beauftragt, den Energieverbrauch der verschiedenen Server und Netzwerkgeräte zu berechnen. Außerdem musst du prüfen, ob die vorhandenen Sicherungen ausreichend dimensioniert sind und wie viel Wärme die Geräte produzieren (wichtig für die Klimaanlage!).

**Deine Mission heute:**
- Elektrische Leistung verstehen und berechnen
- Energiekosten für IT-Geräte ermitteln  
- Wärmeerzeugung in Schaltungen untersuchen
- Sicherungsauslegung überprüfen

## 📖 Fachwissen: Elektrische Leistung

### Was ist elektrische Leistung?

**Leistung (P)** ist die Energie, die pro Zeiteinheit umgesetzt wird. Sie wird in **Watt (W)** gemessen.

**Analogie**: Stell dir Leistung wie die "Arbeitskraft" vor:
- Ein starker Motor → hohe Leistung → viel Arbeit in kurzer Zeit
- Ein starkes Netzteil → hohe Leistung → kann viele Geräte versorgen

**Leistung in der IT:**
- **LED:** 0,1-3W
- **Smartphone-Ladegerät:** 5-20W
- **Laptop:** 45-90W
- **Desktop-PC:** 300-800W  
- **Server:** 500-2000W
- **Rechenzentrum:** 1-50 MW (Megawatt!)

### Leistungsformeln

**Grundformel:**
```
P = U × I
```

**Mit Ohm'schem Gesetz erweitert:**
```
P = U × I
P = U² / R  (wenn R bekannt)
P = I² × R  (wenn R bekannt)
```

### Wichtige Symbole und Einheiten

| Größe | Symbol | Einheit | Einheitenzeichen |
|-------|---------|---------|------------------|
| Leistung | P | Watt | W |
| Spannung | U | Volt | V |
| Strom | I | Ampere | A |
| Widerstand | R | Ohm | Ω |

### Präfixe für Leistung

| Präfix | Symbol | Faktor | Beispiel |
|--------|---------|--------|----------|
| Milli | m | 0,001 | 500mW = 0,5W |
| Kilo | k | 1.000 | 2kW = 2.000W |
| Mega | M | 1.000.000 | 5MW = 5.000.000W |

### Energie und Kosten

**Energie** ist Leistung × Zeit:
```
Energie = Leistung × Zeit
E = P × t
```

**Einheit:** Kilowattstunden (kWh)

**Stromkosten berechnen:**
```
Kosten = Energie × Strompreis
Kosten = P × t × Preis pro kWh
```

## 🔧 Tinkercad-Übung 1: Leistung einer LED-Schaltung

### Schaltung aufbauen

```
9V Batterie (+) → Widerstand (470Ω) → LED → 9V Batterie (-)
```

### Messungen:
1. **Spannung über der LED:** _____ V
2. **Strom durch die LED:** _____ A
3. **Leistung der LED berechnen:** P = U × I = _____ W

### Zusatzmessungen:
4. **Spannung über dem Widerstand:** _____ V  
5. **Strom durch den Widerstand:** _____ A (gleich wie LED)
6. **Leistung des Widerstands:** P = U × I = _____ W

**Gesamtleistung:** P_gesamt = P_LED + P_Widerstand = _____ W

## 🔧 Tinkercad-Übung 2: Leistungsvergleich verschiedener Widerstände

Baue nacheinander Schaltungen mit verschiedenen Widerständen und miss die Leistung:

| Widerstand | Spannung | Strom | Leistung |
|------------|----------|-------|----------|
| 220Ω       | _____ V  | _____ A | _____ W |
| 470Ω       | _____ V  | _____ A | _____ W |
| 1kΩ        | _____ V  | _____ A | _____ W |
| 2,2kΩ      | _____ V  | _____ A | _____ W |

**Beobachtung:** Bei welchem Widerstand ist die Leistung am höchsten?

## 🧮 Rechenübungen

### Aufgabe 1: Server-Netzteil
Ein Server hat folgende Daten auf dem Typenschild:
- Spannung: 230V
- Strom: 4,2A

**Gesucht:** 
a) Leistungsaufnahme des Servers
b) Energiekosten pro Tag bei 0,30€/kWh

**Lösung:**
a) P = U × I = 230V × 4,2A = _____ W = _____ kW
b) Energie pro Tag = P × 24h = _____ kWh
   Kosten = _____ kWh × 0,30€/kWh = _____ € pro Tag

### Aufgabe 2: Widerstand in einer Schaltung
Ein Widerstand von 100Ω wird an 12V angeschlossen.

**Gesucht:**
a) Strom durch den Widerstand
b) Leistung am Widerstand

**Lösung:**
a) I = U / R = 12V / 100Ω = _____ A
b) P = U × I = 12V × _____ A = _____ W
   oder: P = U² / R = (12V)² / 100Ω = _____ W

### Aufgabe 3: LED-Array
Ein Netzwerkswitch hat 24 Status-LEDs. Jede LED benötigt 2V und 15mA.

**Gesucht:**
a) Leistung einer LED
b) Gesamtleistung aller LEDs

**Lösung:**
a) P_LED = U × I = 2V × 0,015A = _____ W = _____ mW
b) P_gesamt = 24 × _____ W = _____ W

## 🎯 Praktisches Anwendungsbeispiel: Rechenzentrum-Planung

**Situation:** Du planst die Stromversorgung für einen Serverraum mit:
- 10× Server à 800W
- 5× Network-Switch à 150W  
- 2× Klimageräte à 3000W
- Beleuchtung: 500W

**Berechnungen:**

### 1. Gesamtleistung berechnen:
- Server: 10 × 800W = _____ W
- Switches: 5 × 150W = _____ W  
- Klima: 2 × 3000W = _____ W
- Beleuchtung: _____ W
- **Gesamtleistung:** _____ W = _____ kW

### 2. Benötigter Strom bei 230V:
I = P / U = _____ W / 230V = _____ A

### 3. Sicherungsauslegung (mit 25% Reserve):
I_Sicherung = _____ A × 1,25 = _____ A
→ Nächstgrößere Sicherung: _____ A

### 4. Stromkosten pro Monat (30 Tage, 0,25€/kWh):
- Energie pro Monat: _____ kW × 24h × 30d = _____ kWh
- Kosten: _____ kWh × 0,25€/kWh = _____ €

### 5. Wärmeabgabe:
Die gesamte elektrische Leistung wird als Wärme freigesetzt!
**Wärmeabgabe:** _____ W = _____ kW Heizleistung

## ⚡ Effizienz und Verluste

### Was ist Effizienz?

**Effizienz (η)** = Nutzleistung / aufgenommene Leistung × 100%

**Beispiel - Server-Netzteil:**
- Aufgenommene Leistung: 500W
- Abgegebene Leistung: 450W  
- Effizienz: η = 450W / 500W × 100% = 90%
- Verlustleistung: 500W - 450W = 50W (als Wärme)

## ✅ Selbstüberprüfung

1. **Die Formel für elektrische Leistung lautet:**
   ☐ P = U + I
   ☐ P = U × I
   ☐ P = U / I

2. **Ein Gerät mit 100W läuft 10 Stunden. Energieverbrauch:**
   ☐ 10 kWh
   ☐ 1 kWh
   ☐ 0,1 kWh

3. **Bei höherer Spannung wird die Leistung:**
   ☐ größer (bei gleichem Strom)
   ☐ kleiner
   ☐ bleibt gleich

4. **1000W entspricht:**
   ☐ 1kW
   ☐ 0,1kW
   ☐ 10kW

## 🎯 Lösungen

### Rechenübungen:
1. **Server:** a) P = 966W = 0,966kW, b) 23,18kWh, 6,95€/Tag
2. **Widerstand:** a) I = 0,12A, b) P = 1,44W
3. **LED-Array:** a) P = 0,03W = 30mW, b) P = 0,72W

### Rechenzentrum-Beispiel:
1. **Gesamtleistung:** 8000W + 750W + 6000W + 500W = **15.250W = 15,25kW**
2. **Strom:** I = 66,3A
3. **Sicherung:** 82,9A → **90A Sicherung**
4. **Kosten:** 10.980kWh × 0,25€ = **2.745€/Monat**
5. **Wärme:** **15,25kW Heizleistung**

### Selbstüberprüfung:
1. ✅ P = U × I
2. ✅ 1 kWh
3. ✅ größer (bei gleichem Strom)
4. ✅ 1kW

## 💡 Energiespar-Tipps für IT

**Wie kann man Strom sparen?**
- Server virtualisieren (weniger physische Geräte)
- Effiziente Netzteile verwenden (>90% Effizienz)
- Geräte bei Nichtgebrauch ausschalten
- LED statt Glühlampen verwenden
- Moderne, stromsparende Hardware einsetzen

---

## 📝 Notizen

```
Wichtige Erkenntnisse zur Leistung:
- Alle elektrische Leistung wird zu Wärme
- Hohe Leistung = hohe Stromkosten
- Effizienz ist wichtig für Kosteneinsparung

Berechnungen üben:
- P = U × I
- E = P × t  
- Kosten = E × Preis
```

**▶️ Leistung verstanden? Dann zu den Schaltungsarten in Lernschritt 4!**