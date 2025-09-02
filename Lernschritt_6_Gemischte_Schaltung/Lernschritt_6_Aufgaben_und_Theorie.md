# Lernschritt 6: Gemischte Schaltung
## 🎯 Handlungssituation: Komplexe Serverraumverkabelung

Das Rechenzentrum wird komplexer! Der Projektleiter zeigt dir eine Schaltungszeichnung für die Serverraumbeleuchtung. Die Schaltung kombiniert Reihen- und Parallelschaltungen - eine sogenannte "gemischte Schaltung". Du musst lernen, solche komplexen Schaltungen zu analysieren, um Ströme und Spannungen korrekt zu berechnen und Fehler zu lokalisieren.

**Deine heutige Aufgabe:**
- Gemischte Schaltungen erkennen und analysieren
- Systematische Berechnung von komplexen Schaltungen
- Ersatzschaltbilder erstellen
- Fehlerdiagnose in komplexen Schaltungen

## 📖 Fachwissen: Gemischte Schaltungen

### Was sind gemischte Schaltungen?

**Gemischte Schaltungen** enthalten sowohl **Reihen-** als auch **Parallelverbindungen**. Sie sind die häufigste Art von Schaltungen in der Praxis.

**Beispiel:**
```
        ┌──── R₂ ────┐
Batt. ──┤            ├── R₄ ──
        └──── R₃ ────┘
```
Hier sind R₂ und R₃ parallel zueinander, aber beide zusammen in Reihe zu R₄.

### Analysemethode: Schrittweise Vereinfachung

**Schritt 1:** Erkenne die Struktur
- Welche Widerstände sind in Reihe?
- Welche sind parallel?

**Schritt 2:** Berechne Teilwiderstände
- Beginne mit den "innersten" Verbindungen
- Ersetze durch Ersatzwiderstände

**Schritt 3:** Vereinfache schrittweise
- Bis nur noch ein Gesamtwiderstand übrig ist

**Schritt 4:** Rückwärts rechnen
- Berechne Ströme und Spannungen für alle Teile

### Wichtige Strategien

#### 1. "Von innen nach außen" vereinfachen
#### 2. "Von außen nach innen" Ströme/Spannungen berechnen
#### 3. Immer prüfen: I_rein = I_raus (Knotenregel)
#### 4. Immer prüfen: U_hin + U_rück = U_gesamt (Maschenregel)

## 🔧 Tinkercad-Übung 1: Einfache gemischte Schaltung

### Schaltung aufbauen

```
        ┌── R₂(470Ω) ──┐
9V Batt. ── R₁(220Ω) ──┤                ├── R₄(330Ω) ──
        └── R₃(1kΩ) ───┘
```

### Komponenten:
- 1× 9V Batterie
- 4× Widerstände: 220Ω, 470Ω, 1kΩ, 330Ω
- Multimeter
- Verbindungsdrähte

### Analyse VOR dem Aufbau:

**Schritt 1 - Struktur erkennen:**
- R₁ ist in Reihe zur Parallelkombination R₂||R₃
- Diese Kombination ist in Reihe zu R₄

**Schritt 2 - Parallelwiderstand R₂||R₃:**
- R₂₃ = (R₂ × R₃) / (R₂ + R₃)
- R₂₃ = (470Ω × 1000Ω) / (470Ω + 1000Ω) = _____ Ω

**Schritt 3 - Gesamtwiderstand:**
- R_ges = R₁ + R₂₃ + R₄
- R_ges = 220Ω + _____ Ω + 330Ω = _____ Ω

**Schritt 4 - Gesamtstrom:**
- I_ges = U / R_ges = 9V / _____ Ω = _____ A

### Messungen zur Kontrolle:
1. **Tatsächlicher Gesamtstrom:** _____ A
2. **Spannung über R₁:** _____ V
3. **Spannung über R₂ (= R₃):** _____ V  
4. **Spannung über R₄:** _____ V

**Kontrollrechnung:** U_R1 + U_R23 + U_R4 = _____ V (soll 9V sein)

## 🔧 Tinkercad-Übung 2: LED-Mischschaltung

### Schaltung aufbauen

```
        ┌── R₂(220Ω) ── LED₂ ──┐
12V Batt. ── R₁(100Ω) ──┤                    ├──
        └── R₃(330Ω) ── LED₃ ──┘
```

### Berechnungen:

**1. Ersatzwiderstand der LED-Zweige:**
Annahme: Jede LED hat 2V Spannung und wirkt wie ein 100Ω Widerstand
- R₂_ges = 220Ω + 100Ω = 320Ω (R₂ + LED₂)
- R₃_ges = 330Ω + 100Ω = 430Ω (R₃ + LED₃)
- R₂₃ = (320Ω × 430Ω) / (320Ω + 430Ω) = _____ Ω

**2. Gesamtwiderstand:**
- R_ges = R₁ + R₂₃ = 100Ω + _____ Ω = _____ Ω

**3. Hauptstrom:**
- I_haupt = 12V / _____ Ω = _____ A

**4. Spannung am Parallelblock:**
- U₂₃ = I_haupt × R₂₃ = _____ A × _____ Ω = _____ V

**5. Ströme durch die LED-Zweige:**
- I₂ = U₂₃ / R₂_ges = _____ V / 320Ω = _____ A
- I₃ = U₂₃ / R₃_ges = _____ V / 430Ω = _____ A

### Messungen zur Überprüfung:
6. **Hauptstrom:** _____ A
7. **Strom durch LED₂:** _____ A
8. **Strom durch LED₃:** _____ A

## 🧮 Rechenübungen

### Aufgabe 1: Server-Rack Stromverteilung
Ein Server-Rack hat folgende Struktur:
```
        ┌── Server₁ (800W) ──┐
230V ── Hauptverteiler ──┤                  ├── Hauptschalter
        └── Server₂ (600W) ──┘
```
Zusätzlich ist vor dem Hauptverteiler eine USV (100Ω Innenwiderstand) geschaltet.

**Gesucht:** 
a) Gesamtstrom
b) Spannung an den Servern
c) Verlustleistung der USV

**Lösung:**
a) **Gesamtleistung:** 800W + 600W = _____ W
   **Gesamtstrom:** I = P / U = _____ W / 230V = _____ A

b) **Spannungsfall USV:** U_USV = I × R = _____ A × 100Ω = _____ V
   **Serverspannung:** U_Server = 230V - _____ V = _____ V

c) **USV-Verluste:** P_USV = I² × R = (_____ A)² × 100Ω = _____ W

### Aufgabe 2: Komplexe LED-Schaltung
```
        ┌── LED₁ (2V, 20mA) ── R₁ ──┐
24V ─── ┤                          ├───
        └── LED₂ (2V, 20mA) ── R₂ ──┘
```
Die LEDs sollen mit je 20mA betrieben werden.

**Gesucht:** R₁ und R₂

**Lösung:**
**Spannung je Zweig:** 24V (parallel)
**Spannung am Widerstand:** 24V - 2V = _____ V
**R₁ = R₂:** R = U / I = _____ V / 0,02A = _____ Ω

### Aufgabe 3: Fehlerdiagnose
Eine Schaltung soll 5A Gesamtstrom haben, misst aber nur 3A.
```
        ┌── R₂(100Ω) ──┐
12V ── R₁(50Ω) ──┤            ├── R₄(200Ω) ──
        └── R₃(200Ω) ──┘
```

**Normale Berechnung:**
- R₂₃ = (100Ω × 200Ω) / (100Ω + 200Ω) = _____ Ω  
- R_ges = 50Ω + _____ Ω + 200Ω = _____ Ω
- I_soll = 12V / _____ Ω = _____ A ≠ 5A

**Mögliche Fehler:** _____

## 🎯 Praktisches Anwendungsbeispiel: Redundante Stromversorgung

**Situation:** Ein kritischer Server soll redundant mit Strom versorgt werden. Zwei Netzteile arbeiten parallel, aber jedes hat eine eigene Zuleitung.

```
230V Netz A ── Netzteil A (600W) ──┐
                                  ├── Server (1000W)
230V Netz B ── Netzteil B (600W) ──┘
```

**Normale Bedingung (beide Netzteile funktionieren):**
- **Leistung je Netzteil:** 1000W / 2 = _____ W
- **Strom je Netzteil:** 500W / 230V = _____ A

**Fehlerfall (Netzteil A fällt aus):**
- **Leistung Netzteil B:** _____ W  
- **Bewertung:** ☐ OK ☐ Überlast

**Planung:** Welche Netzteilleistung ist mindestens nötig?
- Jedes Netzteil muss allein _____ W liefern können
- **Empfehlung:** _____ W Netzteile verwenden

## 📊 Systematisches Vorgehen bei gemischten Schaltungen

### Analyse-Checkliste:

1. **☐ Schaltbild vereinfachen**
   - Parallelwiderstände zusammenfassen
   - Reihenschaltungen addieren

2. **☐ Gesamtwiderstand berechnen**
   - Von innen nach außen arbeiten
   - Ersatzschaltbild erstellen

3. **☐ Hauptstrom bestimmen**
   - I_gesamt = U_gesamt / R_gesamt

4. **☐ Spannungen berechnen**
   - Beginnend mit Hauptstrom
   - Von außen nach innen

5. **☐ Teilströme ermitteln**
   - I = U / R für jeden Zweig
   - Knotenregel prüfen

6. **☐ Ergebnis kontrollieren**
   - Leistungen addieren: P_ges = P₁ + P₂ + ...
   - Mit P_ges = U_ges × I_ges vergleichen

## ✅ Selbstüberprüfung

1. **Bei der Analyse gemischter Schaltungen geht man vor:**
   ☐ von außen nach innen
   ☐ von innen nach außen
   ☐ beliebig

2. **Der Gesamtwiderstand einer gemischten Schaltung ist:**
   ☐ immer größer als alle Einzelwiderstände
   ☐ immer kleiner als alle Einzelwiderstände  
   ☐ kann größer oder kleiner sein

3. **Parallelwiderstände in einer gemischten Schaltung:**
   ☐ haben immer gleichen Strom
   ☐ haben immer gleiche Spannung
   ☐ haben immer gleiche Leistung

4. **Bei Ausfall eines Zweiges in einer gemischten Schaltung:**
   ☐ ändert sich der Gesamtwiderstand
   ☐ bleibt der Gesamtwiderstand gleich
   ☐ hängt von der Position ab

## 🎯 Lösungen

### Tinkercad-Übung 1:
- **R₂₃:** 320Ω
- **R_ges:** 870Ω  
- **I_ges:** 10,3mA

### Tinkercad-Übung 2:
- **R₂₃:** 183Ω
- **R_ges:** 283Ω
- **I_haupt:** 42,4mA
- **U₂₃:** 7,76V
- **I₂:** 24,3mA, **I₃:** 18,1mA

### Rechenübungen:
1. **Server-Rack:** a) I = 6,09A, b) U = 621V, c) P = 3,7kW
2. **LED-Schaltung:** R = 1100Ω
3. **Fehlerdiagnose:** R₂₃ = 66,7Ω, R_ges = 316,7Ω, I_soll = 37,9mA (Aufgabe fehlerhaft)

### Redundante Stromversorgung:
- **Normal:** 500W je Netzteil, 2,17A
- **Fehlerfall:** 1000W auf ein Netzteil → **Überlast**
- **Empfehlung:** Mindestens 1200W Netzteile

### Selbstüberprüfung:
1. ✅ von innen nach außen
2. ✅ kann größer oder kleiner sein
3. ✅ haben immer gleiche Spannung  
4. ✅ ändert sich der Gesamtwiderstand

---

## 📝 Notizen

```
Meine Strategie für gemischte Schaltungen:
1. Struktur analysieren (was ist parallel, was in Reihe?)
2. Von innen nach außen vereinfachen
3. Gesamtwiderstand berechnen
4. Von außen nach innen Ströme/Spannungen berechnen  
5. Kontrollrechnung durchführen

Häufige Fehlerquellen:
- Parallele Widerstände addiert statt Kehrwertformel
- Reihenfolge der Berechnung vertauscht
- Kontrollrechnung vergessen
```

**▶️ Gemischte Schaltungen verstanden? Weiter zu Spannungsteilern in Lernschritt 7!**