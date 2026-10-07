"""Schaltpläne für Lernschritt 6 – Schaltzeichen nach DIN EN 60617,
Kennbuchstaben nach DIN EN IEC 81346, Zählpfeile im Verbraucherzählpfeilsystem.
Ausgabe: SVG (Schrift als Pfade, keine Font-Abhängigkeit) + PNG zur Kontrolle.

Aufruf:  python zeichne.py ZIELORDNER
"""
import sys
import matplotlib
matplotlib.rcParams['svg.fonttype'] = 'path'
matplotlib.rcParams['mathtext.fontset'] = 'dejavusans'
import schemdraw
import schemdraw.elements as elm
from schemdraw.elements import Element2Term
from schemdraw.segments import Segment, SegmentCircle, SegmentText

schemdraw.use('matplotlib')
schemdraw.config(fontsize=13, font='DejaVu Sans', lw=1.6)

ZIEL = sys.argv[1] if len(sys.argv) > 1 else '.'
BLAU = '#1d4ec1'   # Spannungspfeile
ROT = '#c62828'    # Strompfeile
GRAU = '#666666'


# --- DIN-Schaltzeichen, die schemdraw nicht passend mitbringt -------------
class SchliesserDIN(Element2Term):
    """Schließer (DIN EN 60617-7): Schaltglied schräg, ohne Anschlusskreise."""
    def __init__(self, **kw):
        super().__init__(**kw)
        self.segments.append(Segment([(0, 0), (1.25, 0)], visible=False))
        self.segments.append(Segment([(0, 0), (1.15, 0.5)]))   # bewegliches Schaltglied
        self.segments.append(Segment([(1.0, 0), (1.25, 0)]))   # fester Kontakt


class Messgeraet(Element2Term):
    """Messgerät (Kreis mit Kennbuchstabe V bzw. A)."""
    def __init__(self, zeichen='V', **kw):
        super().__init__(**kw)
        self.segments.append(Segment([(0, 0), (0.9, 0)], visible=False))
        self.segments.append(SegmentCircle((0.45, 0), 0.45))
        self.segments.append(SegmentText((0.45, 0), zeichen, fontsize=13,
                                         rotation_global=False))


class Zelle(Element2Term):
    """Batterie/Zelle: langer dünner Strich = Pluspol (am Anfang),
    kurzer dicker Strich = Minuspol (am Ende)."""
    def __init__(self, **kw):
        super().__init__(**kw)
        self.segments.append(Segment([(0, 0), (0.3, 0)], visible=False))
        self.segments.append(Segment([(0, 0.55), (0, -0.55)]))
        self.segments.append(Segment([(0.3, 0.25), (0.3, -0.25)], lw=4))


# --- Hilfsfunktionen -------------------------------------------------------
def leitung(d, *punkte):
    for p, q in zip(punkte, punkte[1:]):
        d.add(elm.Line().at(p).to(q))


def text(d, xy, s, farbe='black', groesse=13, ha='center', va='center'):
    d.add(elm.Label().at(xy).label(s, color=farbe, fontsize=groesse,
                                   halign=ha, valign=va))


def upfeil(d, p1, p2, s, s_xy, ha='center'):
    """Spannungspfeil von p1 nach p2 (+ → −) mit Beschriftung bei s_xy."""
    d.add(elm.Arrow(color=BLAU, lw=1.4, headwidth=0.2, headlength=0.3).at(p1).to(p2))
    text(d, s_xy, s, farbe=BLAU, ha=ha)


def ipfeil(d, mitte, richtung, s, s_xy, ha='center'):
    """Strompfeil: Pfeilspitze auf dem Leiter bei 'mitte', Richtung 'r','l','u','d'."""
    dx, dy = {'r': (1, 0), 'l': (-1, 0), 'u': (0, 1), 'd': (0, -1)}[richtung]
    x, y = mitte
    d.add(elm.Arrow(color=ROT, lw=1.6, headwidth=0.26, headlength=0.36)
          .at((x - 0.18 * dx, y - 0.18 * dy)).to((x + 0.18 * dx, y + 0.18 * dy)))
    text(d, s_xy, s, farbe=ROT, ha=ha)


def rahmen(d, x1, y1, x2, y2, titel):
    leitung_kw = dict(ls='--', color=GRAU, lw=1)
    for p, q in [((x1, y1), (x2, y1)), ((x2, y1), (x2, y2)),
                 ((x2, y2), (x1, y2)), ((x1, y2), (x1, y1))]:
        d.add(elm.Line(**leitung_kw).at(p).to(q))
    text(d, ((x1 + x2) / 2, y2 + 0.4), titel, farbe=GRAU, groesse=12)


def quelle(d, x, y_unten, y_oben, wert='9 V', name='G1', upfeil_x=None):
    """Spannungsquelle senkrecht, Pluspol oben, mit Zuleitungen."""
    ym = (y_unten + y_oben) / 2
    # Zelle exakt in Körperlänge (0,3) setzen, Leitungen bis an die Platten
    leitung(d, (x, y_unten), (x, ym - 0.15))
    d.add(Zelle().at((x, ym + 0.15)).to((x, ym - 0.15)))
    leitung(d, (x, ym + 0.15), (x, y_oben))
    text(d, (x + 0.5, ym + 0.55), '+', groesse=12)
    text(d, (x + 0.5, ym - 0.6), '−', groesse=12)
    text(d, (x + 0.85, ym), f'${name}$  {wert}' if name else wert, ha='left')
    if upfeil_x is not None:
        upfeil(d, (upfeil_x, ym + 0.9), (upfeil_x, ym - 0.9), '$U$',
               (upfeil_x - 0.35, ym), ha='right')


def schliesser(d, x, y_oben, y_unten):
    """Schließer senkrecht zwischen y_oben und y_unten (Leitungen inklusive)."""
    ym = (y_oben + y_unten) / 2
    leitung(d, (x, y_oben), (x, ym + 0.625))
    d.add(SchliesserDIN().at((x, ym + 0.625)).to((x, ym - 0.625)))
    leitung(d, (x, ym - 0.625), (x, y_unten))
    return ym


def speichern(d, name):
    d.save(f'{ZIEL}/{name}.svg', transparent=False)
    d.save(f'{ZIEL}/{name}.png', dpi=110, transparent=False)


# ---------------------------------------------------------------------------
# Abbildung 1: Prototyp Alarmzentrale mit zwei Meldergruppen
# ---------------------------------------------------------------------------
def alarmzentrale():
    with schemdraw.Drawing(show=False) as d:
        quelle(d, 0, 0, 6, upfeil_x=-0.9)
        ipfeil(d, (0, 5.3), 'u', '$I$', (-0.4, 5.3), ha='right')
        leitung(d, (0, 6), (1.5, 6))
        d.add(elm.ResistorIEC().at((1.5, 6)).to((4.5, 6)))
        text(d, (3, 6.75), '$R1$  220 Ω')
        upfeil(d, (2.0, 5.3), (4.0, 5.3), '$U_1$', (3, 4.85))
        leitung(d, (4.5, 6), (6, 6))
        # Anzeige der Zentrale: Spannungsmesser P1 parallel zu R1
        leitung(d, (1.5, 6), (1.5, 7.9), (2.55, 7.9))
        d.add(Messgeraet('V').at((2.55, 7.9)).to((3.45, 7.9)))
        leitung(d, (3.45, 7.9), (4.5, 7.9), (4.5, 6))
        text(d, (3, 8.65), '$P1$  Anzeige')
        d.add(elm.Dot().at((1.5, 6)))
        d.add(elm.Dot().at((4.5, 6)))
        # Knoten A/B, Meldergruppen
        d.add(elm.Dot().at((6, 6)))
        text(d, (6, 6.4), 'A')
        leitung(d, (6, 6), (9, 6))
        for x, s, r, wert, i in [(6, 'S1', 'R2', '470 Ω', '2'),
                                 (9, 'S2', 'R3', '1 kΩ', '3')]:
            ym = schliesser(d, x, 6, 4.0)
            text(d, (x + 0.6, ym + 0.45), f'${s}$', ha='left')
            d.add(elm.ResistorIEC().at((x, 3.6)).to((x, 1.0)))
            leitung(d, (x, 4.0), (x, 3.6))
            leitung(d, (x, 1.0), (x, 0))
            text(d, (x + 0.45, 2.55), f'${r}$', ha='left')
            text(d, (x + 0.45, 2.0), wert, ha='left')
            ipfeil(d, (x, 0.55), 'd', f'$I_{i}$', (x + 0.35, 0.55), ha='left')
        leitung(d, (9, 0), (0, 0))
        d.add(elm.Dot().at((6, 0)))
        text(d, (6, -0.45), 'B')
        upfeil(d, (11.0, 5.7), (11.0, 0.3), '$U_{23}$', (11.3, 3.0), ha='left')
        # Rahmen: was steckt wo?
        rahmen(d, -2.3, -1.0, 5.2, 9.3, 'Alarmzentrale (Prototyp)')
        rahmen(d, 5.5, -1.0, 12.6, 9.3, 'Meldelinie mit Türkontakten')
        text(d, (9.05, 8.4), 'S1: Rack-Tür   S2: Raumtür', groesse=11)
        text(d, (9.05, 7.75), 'Tür zu ⇒ Kontakt geschlossen', groesse=11)
        speichern(d, 'LS6_Alarmzentrale_Schaltplan')


def widerstand(d, p, q, name, wert=None, seite='links', abst=0.4):
    """Widerstand (Rechteck, DIN) von p nach q mit Beschriftung."""
    d.add(elm.ResistorIEC().at(p).to(q))
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    s = f'${name}$' + (f'\n{wert}' if wert else '')
    if p[0] == q[0]:   # senkrecht
        if seite == 'links':
            text(d, (mx - abst, my), s, ha='right')
        else:
            text(d, (mx + abst, my), s, ha='left')
    else:              # waagerecht
        text(d, (mx, my + (0.55 if wert else 0.45)), s)


def punkt(d, xy):
    d.add(elm.Dot(radius=0.09).at(xy))


# ---------------------------------------------------------------------------
# Abbildung 2: Schrittweise Vereinfachung (Ersatzschaltbilder)
# ---------------------------------------------------------------------------
def ersatzschaltbilder():
    H = 4.5      # Höhe eines Panels
    OY1 = 9.0    # Zeile 1: Ausgangsschaltung
    with schemdraw.Drawing(show=False) as d:
        def links_mit_r1(ox, oy):
            ipfeil(d, (ox, oy + 3.9), 'u', '$I$', (ox - 0.35, oy + 3.9), ha='right')
            leitung(d, (ox, oy + H), (ox + 0.6, oy + H))
            widerstand(d, (ox + 0.6, oy + H), (ox + 3.0, oy + H), 'R1', '100 Ω')
            upfeil(d, (ox + 1.1, oy + H - 0.6), (ox + 2.5, oy + H - 0.6), '$U_1$',
                   (ox + 1.8, oy + H - 1.05))

        # ① Ausgangsschaltung (oben)
        ox, oy = 2.6, OY1
        quelle(d, ox, oy, oy + H, wert='9 V', name=None, upfeil_x=ox - 0.8)
        links_mit_r1(ox, oy)
        leitung(d, (ox + 3.0, oy + H), (ox + 6.4, oy + H))
        punkt(d, (ox + 3.8, oy + H)); punkt(d, (ox + 3.8, oy))
        widerstand(d, (ox + 3.8, oy + H), (ox + 3.8, oy), 'R2', '300 Ω', seite='links', abst=0.5)
        widerstand(d, (ox + 6.4, oy + H), (ox + 6.4, oy), 'R3', '600 Ω', seite='links', abst=0.5)
        ipfeil(d, (ox + 3.8, oy + 0.45), 'd', '$I_2$', (ox + 4.1, oy + 0.45), ha='left')
        ipfeil(d, (ox + 6.4, oy + 0.45), 'd', '$I_3$', (ox + 6.7, oy + 0.45), ha='left')
        leitung(d, (ox + 6.4, oy), (ox, oy))
        upfeil(d, (ox + 7.4, oy + H - 0.3), (ox + 7.4, oy + 0.3), '$U_{23}$',
               (ox + 7.65, oy + H / 2), ha='left')
        text(d, (ox + 3.2, oy + H + 1.65), '① Ausgangsschaltung', groesse=14)

        # Übergang ① → ②
        d.add(elm.Arrow(color=GRAU, lw=2.5, headwidth=0.35, headlength=0.45)
              .at((2.4, OY1 - 0.6)).to((2.4, H + 2.3)))
        text(d, (2.8, (OY1 - 0.6 + H + 2.3) / 2), '$R2 \\parallel R3$ zusammenfassen',
             farbe=GRAU, groesse=12, ha='left')

        # ② Ersatzschaltung (unten links)
        ox, oy = 0.6, 0
        quelle(d, ox, oy, oy + H, wert='9 V', name=None, upfeil_x=None)
        links_mit_r1(ox, oy)
        leitung(d, (ox + 3.0, oy + H), (ox + 4.0, oy + H))
        widerstand(d, (ox + 4.0, oy + H), (ox + 4.0, oy), 'R_{23}', '200 Ω', seite='links', abst=0.5)
        leitung(d, (ox + 4.0, oy), (ox, oy))
        upfeil(d, (ox + 4.9, oy + H - 0.3), (ox + 4.9, oy + 0.3), '$U_{23}$',
               (ox + 5.15, oy + H / 2), ha='left')
        text(d, (ox + 2.4, oy + H + 1.65), '② Ersatzschaltung', groesse=14)

        # Übergang ② → ③
        d.add(elm.Arrow(color=GRAU, lw=2.5, headwidth=0.35, headlength=0.45)
              .at((7.3, H / 2)).to((8.8, H / 2)))
        text(d, (8.05, H / 2 + 0.55), '$R1 + R_{23}$', farbe=GRAU, groesse=12)

        # ③ Gesamtwiderstand (unten rechts)
        ox, oy = 10.0, 0
        quelle(d, ox, oy, oy + H, wert='9 V', name=None, upfeil_x=None)
        ipfeil(d, (ox, oy + 3.9), 'u', '$I$', (ox - 0.35, oy + 3.9), ha='right')
        leitung(d, (ox, oy + H), (ox + 4.0, oy + H))
        widerstand(d, (ox + 4.0, oy + H), (ox + 4.0, oy), 'R_\\mathrm{ges}', '300 Ω',
                   seite='links', abst=0.5)
        leitung(d, (ox + 4.0, oy), (ox, oy))
        text(d, (ox + 2.0, oy + H + 1.65), '③ Gesamtwiderstand', groesse=14)
        speichern(d, 'LS6_Ersatzschaltbilder')


# ---------------------------------------------------------------------------
# Abbildung 3: Schaltungen erkennen (A–D) für die Übungen
# ---------------------------------------------------------------------------
def schaltungen_erkennen():
    H = 4.0
    with schemdraw.Drawing(show=False) as d:
        def kopf(ox, oy, buchstabe):
            text(d, (ox - 0.9, oy + H + 0.9), buchstabe, groesse=18, ha='left')

        def q(ox, oy):
            quelle(d, ox, oy, oy + H, wert='', name=None, upfeil_x=None)

        # A: Reihenschaltung R1 – R2 – R3
        ox, oy = 0, 7.5
        kopf(ox, oy, 'A'); q(ox, oy)
        leitung(d, (ox, oy + H), (ox + 0.5, oy + H))
        widerstand(d, (ox + 0.5, oy + H), (ox + 2.7, oy + H), 'R1')
        leitung(d, (ox + 2.7, oy + H), (ox + 3.1, oy + H))
        widerstand(d, (ox + 3.1, oy + H), (ox + 5.3, oy + H), 'R2')
        leitung(d, (ox + 5.3, oy + H), (ox + 6.0, oy + H))
        widerstand(d, (ox + 6.0, oy + H), (ox + 6.0, oy), 'R3', seite='links', abst=0.5)
        leitung(d, (ox + 6.0, oy), (ox, oy))

        # B: Parallelschaltung R1 ∥ R2 ∥ R3
        ox, oy = 10, 7.5
        kopf(ox, oy, 'B'); q(ox, oy)
        leitung(d, (ox, oy + H), (ox + 6.0, oy + H))
        leitung(d, (ox + 6.0, oy), (ox, oy))
        for x, n in [(2.0, 'R1'), (4.0, 'R2'), (6.0, 'R3')]:
            widerstand(d, (ox + x, oy + H), (ox + x, oy), n, seite='links', abst=0.5)
        for x in (2.0, 4.0):
            punkt(d, (ox + x, oy + H)); punkt(d, (ox + x, oy))

        # C: (R1 + R2) ∥ R3
        ox, oy = 0, 0
        kopf(ox, oy, 'C'); q(ox, oy)
        leitung(d, (ox, oy + H), (ox + 6.0, oy + H))
        leitung(d, (ox + 6.0, oy), (ox, oy))
        widerstand(d, (ox + 3.0, oy + H), (ox + 3.0, oy + 2.1), 'R1', seite='links', abst=0.5)
        leitung(d, (ox + 3.0, oy + 2.1), (ox + 3.0, oy + 1.9))
        widerstand(d, (ox + 3.0, oy + 1.9), (ox + 3.0, oy), 'R2', seite='links', abst=0.5)
        widerstand(d, (ox + 6.0, oy + H), (ox + 6.0, oy), 'R3', seite='links', abst=0.5)
        punkt(d, (ox + 3.0, oy + H)); punkt(d, (ox + 3.0, oy))

        # D: R2 ∥ R3, R1 in der Rückleitung
        ox, oy = 10, 0
        kopf(ox, oy, 'D'); q(ox, oy)
        leitung(d, (ox, oy + H), (ox + 6.0, oy + H))
        widerstand(d, (ox + 4.0, oy + H), (ox + 4.0, oy), 'R2', seite='links', abst=0.5)
        widerstand(d, (ox + 6.0, oy + H), (ox + 6.0, oy), 'R3', seite='links', abst=0.5)
        punkt(d, (ox + 4.0, oy + H)); punkt(d, (ox + 4.0, oy))
        leitung(d, (ox + 6.0, oy), (ox + 3.3, oy))
        d.add(elm.ResistorIEC().at((ox + 3.3, oy)).to((ox + 0.6, oy)))
        text(d, (ox + 1.95, oy - 0.5), '$R1$')
        leitung(d, (ox + 0.6, oy), (ox, oy))
        speichern(d, 'LS6_Schaltungen_erkennen')


if __name__ == '__main__':
    alarmzentrale()
    ersatzschaltbilder()
    schaltungen_erkennen()
