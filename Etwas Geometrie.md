# Etwas Geometrie

## Eukildische Geometrie

**Euklid (ca. 300 v.Chr.)**: Axiomatisierung der Geometrie

$\mathcal{E}$: Ebene, Menge von Punkten $A, B, C.. \in \mathcal{E}$

$\mathcal{G}$: Menge der Geraden $g, h \subseteq \mathcal{E}$, $\mathcal{G} \subseteq \mathcal{P}(\mathcal{E})$

$(\mathcal{E}, \mathcal{G}, \in) \quad A \in g$: "Punkt A liegt auf der Geraden g", $g(A) \iff A \in g$

### Axiom 1

Zu je zwei verschiedenen Punkten $A, B$ gibt es genau eine Gerade $g$ mit $g(A) \land g(B)$

### Axiom 2

Jede Gerade enthält mindestens zwei Punkte.

### Axiom 3

Es gibt drei Punkte $A, B, C$, die nicht alle auf einer Geraden liegen.\
$\implies$ Es gibt ein Dreieck $ABC$

> **Satz**: $g, h \in \mathcal{G}, g \neq h \implies |g \cap h| \leq 1$

---

> **Definition**: $g, h \in \mathcal{G}, g || h :\iff g = h \lor g \cap h = \emptyset$

### Parallelenaxiom

Sei $g \in \mathcal{G}, c \in \mathcal{E}$Dann gibt es genau eine Gerade $h \in \mathcal{G}$ mit $h(c)$ und $h||g$

## Heutige geometrische Axiomsysteme

David Hilbert:

- Zwischenrelation $Zw(A, B, C)$ (B liegt zwischen A und C)
- Kongruenzrelation

Kolmogorov:

- Abstand $d: \mathcal{E} \times \mathcal{E} \to \mathbb{R}^+_0, (A, B) \mapsto d(A, B)$

$\overline{AB} := \{A, B\} \cup \{C | Zw(A, C, B)\}, \quad |\overline{AB}|=d(A, B)$

> **Definition**: Eine Bewegung ist eine bijektive Funktion $f: \mathcal{E} \to \mathcal{E}$ mit der Eigenschaft $(\forall A, B \in \mathcal{E}) (d(f(A), f(B)) = d(A, B))$
>
> Spezialfälle:
>
> - Verschiebung (Translation)
> - Drehung um einen Punkt
> - Spiegelung an einer Geraden g 
>
> Aus diesen kann man alle Bewegungen durch Verkettung erhalten.

---

> Bewegungsaxiom: Zu $A, B, C, D$ mit $d(A, B)=d(C, D)$ gibt es genau zwei Bewegungen $f$ mit $f(A)=C$ und $f(B)=D$.

---

> **Definition**: $P, Q$ seien Punktmengenn, $P, Q \in \mathcal{E}$. P und Q heißen _kongruent_, wenn es eine Bewegung f gibt mit $f(P)=Q$.

### Winkel

Zwei Halbgeraden, die im selben Punkt beginnen.

### Bogenmaß

Ein Kreisbogen um einen Winkel hat bei einem Radius $r$ eine bestimmte Länge $l(r)$. Das Bogenmaß ist $\frac{l(r)}{r}$, oder die Kreisbogenlänge im Einheitskreis.

### Gradmaß

$1^o = \frac{\pi}{180}$

### Orientierung

Mathematisch positiv ist die Drehung _gegen_ den Uhrzeigersinn.