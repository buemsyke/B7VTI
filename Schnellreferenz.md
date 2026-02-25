# 📋 Schnellreferenz - Elektrische Grundgrößen

## 🧮 Wichtige Formeln

### Grundformeln
| Formel | Beschreibung | Einheit |
|--------|--------------|---------|
| U = R × I | Ohm'sches Gesetz | V |
| P = U × I | Leistung | W |
| P = U² / R | Leistung (mit R) | W |
| P = I² × R | Leistung (mit I) | W |
| W = P × t | Arbeit | Wh |

### Reihenschaltung
- **Strom:** I₁ = I₂ = I₃ = I_gesamt
- **Spannung:** U_gesamt = U₁ + U₂ + U₃
- **Widerstand:** R_gesamt = R₁ + R₂ + R₃

### Parallelschaltung  
- **Spannung:** U₁ = U₂ = U₃ = U_gesamt
- **Strom:** I_gesamt = I₁ + I₂ + I₃
- **Widerstand:** 1/R_gesamt = 1/R₁ + 1/R₂ + 1/R₃
- **Zwei Widerstände:** R_ges = (R₁ × R₂) / (R₁ + R₂)

### Spezialformeln
- **Spannungsteiler:** U_aus = U_ein × (R₂ / (R₁ + R₂))
- **Brückenabgleich:** R₁ × R₃ = R₂ × R₄
- **Zeitkonstante:** τ = R × C
- **Kondensator-Energie:** W = ½ × C × U²
- **Kondensator-Ladung:** C = Q / U

### Kondensatorschaltungen
- **Parallel:** C_gesamt = C₁ + C₂ + C₃
- **Reihe:** 1/C_gesamt = 1/C₁ + 1/C₂ + 1/C₃
- **Zwei in Reihe:** C_ges = (C₁ × C₂) / (C₁ + C₂)
- **Laden:** U_C(t) = U_ein × (1 - e^(-t/τ))
- **Entladen:** U_C(t) = U_start × e^(-t/τ)
- **Faustregel:** Nach 5 × τ vollständig geladen/entladen

## 📊 Einheiten und Präfixe

### Grundeinheiten
| Größe | Symbol | Einheit |
|-------|--------|---------|
| Spannung | U | Volt (V) |
| Strom | I | Ampere (A) |
| Widerstand | R | Ohm (Ω) |
| Leistung | P | Watt (W) |
| Kapazität | C | Farad (F) |

### Präfixe
| Präfix | Symbol | Faktor | Beispiel |
|--------|--------|--------|----------|
| Pico | p | 0,000000000001 | 100pF = 0,0000000001F |
| Nano | n | 0,000000001 | 100nF = 0,0000001F |
| Mikro | μ | 0,000001 | 470μF = 0,00047F |
| Milli | m | 0,001 | 20mA = 0,02A |
| Kilo | k | 1.000 | 4,7kΩ = 4.700Ω |
| Mega | M | 1.000.000 | 2,2MΩ = 2.200.000Ω |

## 🔧 Tinkercad Tipps

### Häufig verwendete Bauteile
- **Batterie:** 9V, 12V
- **Widerstände:** 220Ω, 470Ω, 1kΩ, 2,2kΩ
- **LEDs:** Rot (ca. 2V, 20mA)
- **Kondensatoren:** 100nF, 470μF, 1000μF
- **Multimeter:** Volt-/Ampere-Messung

### Messregeln
- **Spannung:** Parallel zum Bauteil messen
- **Strom:** In Reihe zur Leitung messen
- **Polarität beachten:** + an +, - an -

## 💡 Typische IT-Werte

### Spannungen
- **Netzspannung:** 230V AC
- **PC-Netzteil:** 12V, 5V, 3,3V DC
- **USB:** 5V DC
- **Logikpegel:** 3,3V, 5V

### Ströme
- **LED:** 20mA
- **USB-Gerät:** 0,5-2,1A
- **Desktop-PC:** 2-8A
- **Server:** 5-15A

### Leistungen
- **LED:** 0,1-3W
- **Laptop:** 45-90W
- **Desktop-PC:** 300-800W
- **Server:** 500-2000W

## ⚡ Sicherheitsregeln

1. **Niemals** unter Spannung arbeiten
2. **Immer** Gerät ausschalten vor Änderungen
3. **Polarität** bei Bauteilen beachten
4. **Sicherungen** nicht überbrücken
5. **Im Zweifel** → Experten fragen!

## 🔍 Fehlersuche

### Häufige Probleme
| Problem | Mögliche Ursache | Lösung |
|---------|------------------|--------|
| LED leuchtet nicht | Polarität falsch | Umdrehen |
| Zu wenig Strom | Widerstand zu groß | Kleineren R wählen |
| Bauteil wird heiß | Zu viel Strom | Größeren R vorschalten |
| Messung unplausibel | Multimeter falsch eingestellt | Messbereich prüfen |

## 📚 Weitere Hilfen

- **Tinkercad Hilfe:** https://www.tinkercad.com/learn
- **Ohm'sches Gesetz Rechner:** Online-Rechner verwenden
- **Farbcode Widerstände:** Tabellen im Internet
- **Bei Fragen:** Lehrer/Ausbilder fragen!

---

**🎯 Diese Referenz als Bookmark speichern - sie hilft bei allen Lernschritten!**
