# Vertiefung: Grundlegende Schaltzeichen

## 🎯 Lernziel
Du lernst die wichtigsten Schaltzeichen der Elektrotechnik kennen, die in IT-Systemen verwendet werden.

## 📖 Was sind Schaltzeichen?

**Schaltzeichen** sind standardisierte Symbole, die elektronische Bauteile in **Schaltplänen** darstellen. Sie sind wie eine universelle Sprache - jeder Elektriker weltweit versteht sie.

### ⚡ Warum sind Schaltzeichen wichtig?
- **Universelle Verständigung** zwischen Technikern
- **Schnelle Analyse** komplexer Schaltungen
- **Dokumentation** von IT-Systemen
- **Fehlersuche** in elektronischen Geräten

## 🔧 Grundlegende Schaltzeichen für IT-Systeme

### Spannungsquellen

| Schaltzeichen | Bezeichnung | Anwendung IT |
|---------------|-------------|--------------|
| ──┃─┃── | **Batterie/Gleichspannungsquelle** | USV-Batterien, CMOS-Batterie |
| ──⊗── | **Wechselspannungsquelle** | Netzteile, Stromversorgung |

### Widerstandsartige Bauteile

| Schaltzeichen | Bezeichnung | Anwendung IT |
|---------------|-------------|--------------|
| ──▭── | **Widerstand** | Strombegrenzung, Spannungsteiler |
| ──▭──↕ | **Potentiometer** | Lautstärke, Helligkeitsregler |

### Halbleiter

| Schaltzeichen | Bezeichnung | Anwendung IT |
|---------------|-------------|--------------|
| ──▷┃── | **LED** | Statusanzeigen, Displays |
| ──▷┃── | **Diode** | Gleichrichtung, Schutzschaltungen |

### Schalter und Verbindungen

| Schaltzeichen | Bezeichnung | Anwendung IT |
|---------------|-------------|--------------|
| ──/── | **Schalter** | Power-Button, Reset-Taster |
| ──┴── | **Masse/Ground** | Bezugspotential, Schirmung |

## 🔍 Praktische Anwendung im IT-Bereich

### Server-Netzteil Schaltplan (vereinfacht)
```
230V AC  ──⊗──  [Transformator]  ──▭──  ──▷┃──  ──┃─┃──  12V DC
         Eingang                 Filter   Diode    Kondensator  Ausgang
```

### LED-Statusanzeige
```
+5V  ──▭──  ──▷┃──  ──┴──  GND
    220Ω     LED    Masse
```

## 🧮 Übung: Schaltzeichen erkennen

**Aufgabe 1:** Ordne die Schaltzeichen zu:

1. ──▭── ➔ ___________
2. ──▷┃── ➔ ___________  
3. ──┃─┃── ➔ ___________
4. ──┴── ➔ ___________

**Auswahlmöglichkeiten:** Batterie, LED, Widerstand, Masse

**Aufgabe 2:** Zeichne die fehlenden Schaltzeichen:

Eine einfache LED-Schaltung besteht aus:
- Batterie: ___________
- Widerstand: ___________  
- LED: ___________
- Masse: ___________

## 🎯 Praxisbezug: Mainboard-Schaltplan

**Situation:** Du hilfst beim Aufbau eines PCs und findest diese Symbole auf dem Mainboard-Schaltplan:

| Symbol | Bedeutung | Funktion |
|---------|-----------|----------|
| ──▭── R47 | Widerstand 47Ω | Strombegrenzung für Power-LED |
| ──▷┃── D5 | LED | Power-Statusanzeige |
| ──┴── GND | Masse | Bezugspotential |

## ✅ Selbsttest

**Kreuze die richtigen Antworten an:**

1. **Was zeigt dieses Symbol an: ──▭──**
   - ☐ Batterie
   - ☐ Widerstand ✓
   - ☐ LED
   - ☐ Schalter

2. **Welches Symbol steht für eine LED?**
   - ☐ ──┃─┃──
   - ☐ ──▷┃── ✓
   - ☐ ──▭──
   - ☐ ──⊗──

3. **Was bedeutet das Symbol ──┴──?**
   - ☐ Batterie
   - ☐ Widerstand
   - ☐ Masse ✓
   - ☐ Schalter

## 🎯 Lösungen

### Übung Aufgabe 1:
1. **──▭──** ➔ **Widerstand**
2. **──▷┃──** ➔ **LED**
3. **──┃─┃──** ➔ **Batterie**
4. **──┴──** ➔ **Masse**

### Übung Aufgabe 2:
- **Batterie:** ──┃─┃──
- **Widerstand:** ──▭──
- **LED:** ──▷┃──
- **Masse:** ──┴──

## 📝 Notizen

```
Wichtige Schaltzeichen merken:
□ Widerstand = ──▭──
□ LED = ──▷┃──  
□ Batterie = ──┃─┃──
□ Masse = ──┴──
□ Schalter = ──/──

Praxistipp: Schaltzeichen sind immer gleich,
egal ob auf Mainboard, Netzteil oder Display!
```

---

**▶️ Nächste Vertiefung:** [Referenzkennzeichen nach EN IEC 81356](./02_Referenzkennzeichen_EN_IEC_81356.md)