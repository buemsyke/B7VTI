# Lernschritt 1: Grundlagen - Spannung und Strom
## 🎯 Handlungssituation: Erste Messungen im neuen Rechenzentrum

Du beginnst deinen ersten Tag im Projektteam für das neue Rechenzentrum. Der Projektleiter führt dich in die Räumlichkeiten und erklärt, dass vor dem Anschluss der teuren Serverausrüstung die bestehende Stromversorgung überprüft werden muss.

**Deine Aufgabe heute:**
- Die Grundlagen von Spannung und Strom verstehen
- Erste einfache Messungen mit einem Multimeter durchführen
- Eine einfache Schaltung in Tinkercad aufbauen und messen

## 📖 Fachwissen: Spannung und Strom

### Was ist elektrische Spannung?

**Spannung (U)** ist der "Druck", der Elektronen durch einen Leiter treibt. Sie wird in **Volt (V)** gemessen.

**Analogie**: Stell dir Spannung wie Wasserdruck in einem Rohr vor:
- Hoher Wasserdruck → Wasser fließt schnell
- Hohe Spannung → Elektronen bewegen sich schnell

**Wichtige Spannungen in der IT:**
- Steckdose: 230V (Deutschland)
- USB: 5V
- Motherboard: 12V, 5V, 3,3V
- Prozessor: 1,2-1,8V

### Was ist elektrischer Strom?

**Strom (I)** ist die Menge der Elektronen, die pro Sekunde durch einen Leiter fließt. Er wird in **Ampere (A)** gemessen.

**Analogie**: Strom ist wie die Wassermenge, die durch ein Rohr fließt:
- Großes Rohr → viel Wasser fließt durch
- Dicker Leiter → viel Strom fließt durch

**Typische Stromstärken in der IT:**
- LED: 0,02A (20mA)
- USB-Gerät: 0,5-2,1A
- Desktop-PC: 2-8A
- Server: 5-15A

### Wichtige Symbole und Einheiten

| Größe | Symbol | Einheit | Einheitenzeichen |
|-------|---------|---------|------------------|
| Spannung | U | Volt | V |
| Strom | I | Ampere | A |

### Präfixe (Vorsätze)

| Präfix | Symbol | Faktor | Beispiel |
|--------|---------|--------|----------|
| Milli | m | 0,001 | 20mA = 0,02A |
| Kilo | k | 1.000 | 5kV = 5.000V |

## 🔧 Tinkercad-Übung 1: LED mit Batterie

### Schaltung aufbauen

1. **Gehe zu Tinkercad** (https://www.tinkercad.com/)
2. **Erstelle einen neuen Schaltkreis**
3. **Baue folgende Schaltung auf:**

```
9V Batterie (+) → Widerstand (220Ω) → LED → 9V Batterie (-)
```

### Komponenten:
- 1x 9V Batterie
- 1x LED (rot)
- 1x Widerstand 220Ω
- Verbindungsdrähte

### Schritt-für-Schritt Anleitung:

1. **Batterie platzieren:** Ziehe eine 9V Batterie in den Arbeitsbereich
2. **LED hinzufügen:** Füge eine rote LED hinzu (achte auf die Polarität: langes Bein = +)
3. **Widerstand einfügen:** Füge einen 220Ω Widerstand hinzu
4. **Verkabeln:**
   - Rotes Kabel: Batterie (+) zu Widerstand
   - Rotes Kabel: Widerstand zu LED (+)
   - Schwarzes Kabel: LED (-) zu Batterie (-)

### 🔍 Messübung 1: Spannung messen

1. **Multimeter hinzufügen** (auf Voltmeter einstellen)
2. **Spannungsmessung parallel zur Batterie:**
   - Rote Messleitung an Batterie (+)
   - Schwarze Messleitung an Batterie (-)
   - **Erwarteter Wert:** 9V

3. **Spannungsmessung parallel zur LED:**
   - Rote Messleitung an LED (+)
   - Schwarze Messleitung an LED (-)
   - **Notiere den gemessenen Wert:** _____ V

### 🔍 Messübung 2: Strom messen

1. **Multimeter auf Amperemeter umstellen**
2. **Strommessung in Reihe zur LED:**
   - Unterbrich die Leitung zwischen Widerstand und LED
   - Führe die Leitung über das Amperemeter
   - **Notiere den gemessenen Wert:** _____ A (oder mA)

## 🧮 Rechenübung

**Gegeben:** Du hast eine LED-Statusanzeige für einen Server gemessen:
- Spannung über der LED: 2,1V
- Strom durch die LED: 18mA

**Aufgabe:** Rechne die Werte in verschiedene Einheiten um:

1. **18mA in Ampere:** _____ A
2. **2,1V in Millivolt:** _____ mV

## 🎯 Praktisches Anwendungsbeispiel

**Situation:** In der Serverraumplanung findest du folgende Angaben auf einem Netzgerät:
- **Input:** 230V AC
- **Output:** 12V DC, 5A

**Fragen:**
1. Was bedeutet "AC" und "DC"?
2. Welche Spannung liegt am Ausgang an?
3. Welcher maximale Strom kann fließen?

## ✅ Selbstüberprüfung

**Beantworte folgende Fragen:**

1. **Was ist Spannung?** 
   ☐ Die Menge der Elektronen
   ☐ Der "Druck", der Elektronen antreibt
   ☐ Die Geschwindigkeit der Elektronen

2. **In welcher Einheit wird Strom gemessen?**
   ☐ Volt (V)
   ☐ Ampere (A)
   ☐ Watt (W)

3. **Wie wird eine Spannung gemessen?**
   ☐ In Reihe zum Bauteil
   ☐ Parallel zum Bauteil
   ☐ Egal wie

4. **Wie wird ein Strom gemessen?**
   ☐ In Reihe zur Leitung
   ☐ Parallel zur Leitung
   ☐ Egal wie

## 🎯 Lösungen

### Tinkercad-Messungen (typische Werte):
- **Batteriespannung:** 9V
- **LED-Spannung:** ca. 2,0-2,2V
- **LED-Strom:** ca. 30-40mA

### Rechenübung:
1. **18mA = 0,018A**
2. **2,1V = 2.100mV**

### Praktisches Beispiel:
1. **AC** = Wechselstrom, **DC** = Gleichstrom
2. **12V** liegen am Ausgang an
3. **5A** ist der maximale Strom

### Selbstüberprüfung:
1. ✅ Der "Druck", der Elektronen antreibt
2. ✅ Ampere (A)
3. ✅ Parallel zum Bauteil
4. ✅ In Reihe zur Leitung

---

## 📝 Notizen

Platz für deine eigenen Aufzeichnungen und Erkenntnisse:

```
Meine Messergebnisse:
- Batteriespannung: _____ V
- LED-Spannung: _____ V  
- LED-Strom: _____ A

Wichtige Erkenntnisse:
- 
- 
- 
```

## 🔬 Vertiefungen für Experten

Für vertiefendes Lernen stehen dir umfangreiche **Zusatzmaterialien** zur Verfügung:

### 📚 Theoretische Vertiefungen
- **[Grundlegende Schaltzeichen](./Vertiefungen/01_Grundlegende_Schaltzeichen.md)** - Symbole der Elektrotechnik
- **[Referenzkennzeichen EN IEC 81356](./Vertiefungen/02_Referenzkennzeichen_EN_IEC_81356.md)** - Eindeutige Bauteilbezeichnungen
- **[Zählpfeile, Skalar und Vektor](./Vertiefungen/03_Zaehlpfeile_Skalar_Vektor.md)** - Richtungskonventionen
- **[Verbraucher-Zählpfeilsystem](./Vertiefungen/04_Verbraucher_Zaehlpfeilsystem.md)** - Leistungsberechnung korrekt
- **[Technische Spannungserzeugung](./Vertiefungen/05_Spannungserzeugung_Batterie.md)** - Wie Batterien funktionieren
- **[Messung von Strom und Spannung](./Vertiefungen/06_Messung_Strom_Spannung.md)** - Professionelle Messtechnik
- **[Elektrische Spannung U=W/Q](./Vertiefungen/07_Elektrische_Spannung_Formel.md)** - Physikalische Definition
- **[Stromstärke und Ladung I=Q/t](./Vertiefungen/08_Stromstaerke_Ladung_Formel.md)** - Strom verstehen
- **[Widerstand und Leitwert R=1/G](./Vertiefungen/09_Widerstand_Leitwert.md)** - Umgekehrte Proportionalität
- **[Einheiten](./Vertiefungen/10_Einheiten.md)** - SI-System und Elektrotechnik
- **[Einheitenvorsätze](./Vertiefungen/11_Einheitenvorsaetze.md)** - Präfixe richtig anwenden
- **[Runden und Fehlerrechnung](./Vertiefungen/12_Runden_Fehlerrechnung.md)** - Messgenauigkeit berücksichtigen

## 🎮 Interaktive H5P-Übungen

**Spielerisch lernen** mit interaktiven Übungen:

### 🏆 H5P-Übungsmodule
- **[Messung von Strom und Spannung](./Uebungen_H5P/01_Uebung_Messung_Strom_Spannung.md)** - Praktische Messungen
- **[Elektrische Spannung U=W/Q](./Uebungen_H5P/02_Uebung_Spannung_Formel.md)** - Energieformel anwenden  
- **[Stromstärke und Ladung I=Q/t](./Uebungen_H5P/03_Uebung_Strom_Ladung.md)** - Strom-Berechnungen
- **[Einheitenvorsätze und Rundung](./Uebungen_H5P/04_Uebung_Einheiten_Rundung.md)** - Präfixe und Genauigkeit

**Features der H5P-Übungen:**
- ✅ **Interaktive Quizzes** mit direktem Feedback
- ✅ **Drag & Drop** Schaltungsaufbau
- ✅ **Speed-Challenges** für schnelles Rechnen
- ✅ **Praxis-Szenarien** aus dem IT-Bereich
- ✅ **Gamification** mit Punkten und Badges
- ✅ **Zertifikate** als Kompetenznachweis

📖 **[Alle H5P-Übungen im Überblick](./Uebungen_H5P/README.md)**

## 📈 Dein Lernfortschritt

### ✅ Grundlagen-Checkliste
- [ ] Spannung und Strom verstehen
- [ ] LED-Schaltung aufbauen (Tinkercad)
- [ ] Spannungsmessung (parallel)
- [ ] Strommessung (in Reihe)
- [ ] Ohmsches Gesetz anwenden
- [ ] Einheiten umrechnen (mA ↔ A)
- [ ] Selbsttest bestanden

### 🎯 Expertenlevel (optional)
- [ ] Alle 12 Vertiefungen gelesen
- [ ] H5P-Übungen abgeschlossen
- [ ] Badges gesammelt
- [ ] Zertifikate erhalten
- [ ] Praxis-Challenges gemeistert

## 🚀 Bereit für Lernschritt 2?

**Grundlagen:** Wenn du die Basis-Aufgaben erfolgreich gelöst hast ✅  
**Experte:** Nach Vertiefungen und H5P-Übungen ✅

**▶️ Weiter zu [Lernschritt 2: Widerstand und Ohmsches Gesetz](../Lernschritt_2_Widerstand_Ohmsches_Gesetz/)**