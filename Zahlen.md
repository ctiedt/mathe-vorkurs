# Natürliche und ganze Zahlen (20.09.2018)

## Natürliche Zahlen

Undendliche Menge; Unendlichkeitsaxiom\
$\mathbb{N} := \{0, 1, 2, 3, ...\}$\
$\mathbb{N}^+ := \mathbb{N} \setminus\{0\}$

__Peano'sche Axiome__\
Die "Struktur" der natürlichen Zahlen wird durch eine *Nachfolgerfunktion* beschrieben.

- $0 \in \mathbb{N}$
- $S: \mathbb{N} \to \mathbb{N}$
- $S$ ist injektiv
- $0 \notin Bild(S)$

> **Induktionsaxiom**: $(\forall A \subseteq \mathbb{N})(0 \in A \land \forall n \in \mathbb{N})(n \in A \implies S(n) \in A) \implies A = \mathbb{N}$

### Beweise durch Induktion (Beispiel)

Es ist zu beweisen, dass eine Eigenschaft E auf alle natürlichen Zahlen zutrifft.

$A = \{n \in \mathbb{N} | E(n) \}$

Zu zeigen:

- Anfang: $0 \in A \iff E(0)$
- Induktionsvoraussetzung: $(\exists n \in \mathbb{N})$
- Induktionsbeweis: $E(n) \implies E(S(n))$

> <abbr title="Rekursive Defintion">**ADDITION (+)**</abbr>:
> - Sei $m \in \mathbb{N}$, $m$ fest
> - $m + 0 = m$
> - $m + S(n) = S(m+n)$
>
> $S(n) \equiv n + 1$
>
> Beispiel: $3 + 2 = 3 + S(1) = S(3 + 1) = S(3 + S(0)) = S(S(3)) = S(4) = 5$

---

> **Multiplikation ( $\cdot$ )**
> - $m \cdot 0 := 0$
> - $m \cdot n := m \cdot S(n) + m$

Wir wollen zeigen:\
$E(n) = \sum_{i=0}^n i=\frac{n(n+1)}{2}$

- *A*: $n=0$, $0 = \frac{0(0+1)}{2} \checkmark$
- *V*: Sei $n \in \mathbb{N}$, es sei $0+1+2+...+n=\frac{n(n+1)}{2}$
- *B*: Zu zeigen: Dann gilt auch $E(n+1)$
  - $0+1+2+...+n+(n+1)=(0+1+2+...+n)+(n+1)=\frac{n(n+1)}{2}+(n+1)=(n+1) \cdot (\frac{n}{2}+1)=(n+1) \cdot \frac{(n+2)}{2}$

> Eine Menge $A$ heißt *abzählbar*, wenn $A \sim \mathbb{N}$\
> Beispiel: $G = \{n \in \mathbb{N} | (\exists m \in \mathbb{N})(n=2m)\}$, $\mathbb{N} \sim G$\
> $\mathbb{Q}, (\mathbb{Q} \sim \mathbb{N}\}$

---

## Positionssysteme

- Römische Zahlen: $I, II, III, IV, V, VI...$ (additives System mit Abkürzungen)
- Arabische Ziffern: $0, 1, 2, ..., 9, 10, 11, ...$
- Binär/Dual: $0, 1, 10, 11, 100...$

Basis $B \in \mathbb{N}, \geq 2$\
Ziffern: $0, 1, 2, ..., B-1$, jede Ziffer *ein* Zeichen\
Notation: $z = {a_{n-1}a_{n-2}...a_0}_{(B)}$\
          $z = a_{n-1}B^{n-1}+a_{n-2}B^{n-2}+a_{n-3}B^{n-3}+...+a_{1}B^{1}+a_0$

### Umrechnung in andere Positionssysteme

$z=629_{(10)} \rightarrow B=2$

```python
z = 629
b = ""

while z != 0:
    b = (z % 2) + b
    z = b // 2
```

$z=629_{(10)} = 1001110101_{(2)} = 275_{(16)}$

### Horner-Schema

| $a_{(n-1)}$ | $a_{(n-2)}$          | ... | $a_1$ | $a_0$ |
| ----------- | -----------          | --- | ----- | ----- |
|     0       | $a_{(n-1)}B$         | ... |       |       |
| $a_{(n-1)}$ | $a_{(n-1)}B+a_{n-2}$ |     |       |       |

| 1 | 0 | 0 | 1 | 1  | 1  | 0  | 1   | 0   | 1   |
| - | - | - | - | -- | -- | -- | --- | --- | --- |
| 0 | 2 | 4 | 8 | 18 | 38 | 78 | 156 | 314 | 628 |
| 1 | 2 | 4 | 9 | 19 | 39 | 79 | 157 | 314 | $629_{(10)}$ |

$34591_{(10)} \rightarrow B=2, B=16$

```python
34591 // 2 = 17295
17295 // 2 = 8647
8647 // 2 = 4323
4323 // 2 = 2161
2161 // 2 = 1080
1080 // 2 = 540
540 // 2 = 270
270 // 2 = 135
135 // 2 = 67
67 // 2 = 33
33 // 2 = 16
16 // 2 = 8
8 // 2 = 4
4 // 2 = 2
2 // 2 = 1
1 // 2 = 0
```

$34591_{(10)} = 1000 0111 0001 1111_{(2)}$

```python
34591 // 16 = 2161
2161 // 16 = 135
135 // 16 = 8
8 // 16 = 0
```

$34591_{(10)} = 871F_{(16)}$

$1210121_{(3)} \rightarrow B=10$

| 1 | 2 | 1 | 0 | 1 | 2 | 1 |
| - | - | - | - | - | - | - |
| 0 | 3 |   |   |   |   |   |
| 1 | 5 |   |   |   |   |   |

$1210121_{(3)} = 1312_{(10)}$

$AFFE_{(16)} \rightarrow B=10$

$AFFE_{(16)} = 45054_{(10)}$

## Ganze Zahlen

*Motivation*: In $\mathbb{N}$ ist die Gleichung $x+1=0$ nicht lösbar.\
Idee: Wir nehmen die Lösungen $x + n = 0$ hinzu.\
                              $x = -n$ (Gegenzahl, Ausnahme $0 = -0$)

$\mathbb{Z} := \{0, 1, -1, 2, -2, 3, -3, ...\}$\
Erweiterung der Operationen + und $\cdot$ auf $\mathbb{Z}$ (Fortsetzung)\
Neue Operation: Subtraktion ( - )\
Lineare Ordnung $<$ bzw $\leq$: $...-3<-2<-1<0<1<2<3...$

$(\forall a, b, c \in \mathbb{Z})$\
$(a \leq b \land b \leq c \implies a \leq c)$\
$(a \leq b \land b \leq a \implies a = b)$\
$(a \leq a' \land b \leq b' \implies a + b \leq a' + b')$\
$(0 \leq a \leq a' \land 0 \leq b \leq b' \implies a \cdot b \leq a' \cdot b')$\
$(0 < a \land b < 0 \implies ab < 0)$\
$(a < 0 \land 0 < b \implies ab < 0)$\
$(a \cdot b = 0 \implies a=0 \lor b=0)$

Betrag: $|a| := \begin{cases}a \impliedby a \geq 0 \\ -a \impliedby a < 0\end{cases}$

> **Satz von der Division mit Rest**: Seien $a, m \in \mathbb{Z}$ und $m \geq 1$.
> Dann gibt es ganze Zahlen $q, r \in \mathbb{Z}$ mit $a = q \cdot m + r$ und $0 \leq r < m$
>
> Beispiel: $a=16, m=3$
> $a = 5 \cdot 3 + 1$; $q = 5, r = 1$

---

### Teiler

$a, b \in \mathbb{Z}$, a Teiler von b, bzw. b Vielfaches von a (geschrieben $a|b$), wenn:\
$a|b \iff (\exists c \in \mathbb{Z}) a \cdot c = b$\
Falls $a \geq 1$: Der Rest bei der Division von b durch a ist $0$.\
$b = 0 \implies b = 0 = 0 \cdot a$ für alle $a \in \mathbb{Z}$\
$(\forall a \in \mathbb{Z})(a|0)$\
$a = 0, a|b \implies b = 0$

$(\forall a \in \mathbb{Z}) a|a$\
$a|b \land b|c \implies a|c$

$a|b \land b|a \iff (a=b) \lor (a=-b)$\
$a|b \land b|a \iff a|(-b)$\
$a|b \land b|a \iff (-a)|b$\
$a|b \land b|a \iff (-a)|(-b)$

$a, b \geq 1 , a|b \implies a \leq b$\
$(\forall z, z' \in \mathbb{Z})(\forall b' \in \mathbb{Z})(a|b \land a|b' \implies a|z \cdot b + z' \cdot b'$\

Sei $b \in \mathbb{Z}$. Dann hat b immer folgende Teiler: $1, (-1), b, (-b)$ ("Triviale Teiler")

$p \in \mathbb{Z}$ heißt *Primzahl*, wenn $p \geq 2$ und p nur triviale Teiler hat.\
$Primzahl(p) \iff p \geq 2 \land (\forall a \in \mathbb{Z})(a|p \implies (a=1 \lor a=p \lor a=-1 \lor a=-p)$

> **Hilfssatz**: Sei $b \in \mathbb{Z}$, $|b| \geq 2$. p sei der kleinste Teiler von b mit $p \geq 2$. Dann ist p Primzahl. Insbesondere hat jede ganze Zahl b mit $|b| \geq 2$ mindestens einen Primteiler.
>
> **Beweis**: Es gibt Teiler von b, die $\geq 2$ sind, z.B. $|b|$. Daher existiert auch ein kleinster Teiler $p|b$ mit $p \geq 2$.\
> Angenommen, p ist keine Primzahl, muss es einen nichttrivialen, positiven Teiler $a|p$ mit $a \neq 1 \land a \neq p$ geben. Also $2 \leq a < p$. Aus $a|b$ und $p|b$ folgt $a|b$. Somit gibt es einen Teiler a von b mit $2 \leq a$ und $a \leq p$. &#9889; zur Wahl von p.
> Daher ist p Primzahl.
>
> **Satz (Euklid)**: Es gibt unendlich viele Primzahlen.\
> **Beweis**: Annahme - Es gibt nur endlich viele Primzahlen.\
> n sei die Anzahl dieser (aller) Primzahlen und $p_1, p_2, p_3, ..., p_n$ seien diese Primzahlen.\
> b sei $p_1 \cdot p_2 \cdot p_3 \cdot ... \cdot p_n+1$. Dann ist $b \geq 2$ und hat nach dem Hilfssatz mindestens einen Primteiler q. Falls $b=q$, so &#9889;, weil $q > p_i$ für $(i=1...n)$\
> Falls $q < b$, so muss je $q = p_i$ für ein $i \in \{1, ..., n\}$.\
> Aber: $\lnot p_i|b$ für alle $i=1, ..., n$, denn bei der Division durch $p_i$ bleibt stets der Rest 1. &#9889;. Also Annahme falsch.

---

> **Fundamentalsatz der Arithmetik**: Jede ganze Zahl $b \geq 2$ hat eine Darstellung als Produkt von Primzahlpotenzen. $b = p{_1}^{k_1} \cdot p{_2}^{k_2} \cdot ... \cdot p{_n}^{k_n}$. Diese Darstellung ist bis auf die Reihenfolge eindeutig.
>
> Sei $b \geq 2$. Wenn b keine Primzahl ist, dann gibt es einen Primteiler q mit $q \leq \sqrt{b}$.

#### Teilbarkeitsregeln

| Teiler | Regel |
| ------ | ----- |
| 2      | Wenn die letzte Ziffer durch 2 teilbar ist |
| 3      | Wenn die Quersumme durch 3 teilbar ist |
| 4      | Wenn die letzten zwei Ziffern durch 4 teilbar sind |
| 5      | Wenn die letzte Ziffer $\in \{0, 5\}$ ist |
| 6      | Wenn die Zahl durch 2 und 3 teilbar ist |
| 7      | Wenn $a_{n-1}a_{n-2}...a_2a_1 - 2a_0$ duch 7 teilbar ist |
| 8      | Wenn die letzten drei Ziffern durch 8 teilbar sind |
| 9      | Wenn die Quersumme durch 9 teilbar ist |
| 10     | Wenn die letzte Ziffer eine 0 ist |
| 11     | Alternierende Quersummer $a_0 - a_1 + a_2 - ... \pm a_{n-2} \pm a_{n-1}$ durch 11 teilbar |

```python
def smallest_prime_divisor(x):
    for i in range(2, x+1):
        if x % i == 0:
            if x == i:
                return x
            else:
                return smallest_prime_divisor(i)

def factorise(z):
    f = []
    while z > 2:
        p = smallest_prime_divisor(z)
        f.append(p)
        z = int(z/p)
    return f

z = 15135120
div = []

while z > 2:
    p = smallest_prime_divisor(z)
    div.append(p)
    z = int(z / p)

#div = [2, 2, 2, 2, 3, 3, 3, 5, 7, 7, 11, 13]
```

#### Größter gemeinsamer Teiler

Seien $a, b \in \mathbb{Z}, a \neq 0, b \neq 0$\
$ggT(a, b) := max\{t \in \mathbb{Z} | t \geq 1 \land t|a \land t|b\}$\

a, b **teilerfremd** $\iff ggT(a, b) = 1$

#### Kleinstes gemeinsames Vielfaches

Seien $a, b \in \mathbb{Z}, a \neq 0, b \neq 0$\
$kgV(a, b) := min\{w \in \mathbb{Z} | w \geq 1 \land a|w \land b|w\}$

$kgV(a, b) \cdot ggT(a, b) = a \cdot b$

## Rationale Zahlen

*Motivation*: In $\mathbb{Z}$ ist die Gleichung $2 \cdot x = 1$ nicht lösbar.\
(Allgemein: $a \cdot x = b$ falls $\lnot a|b$; $x = \frac{b}{a}$)

$\widetilde{\mathbb{Q}} := \{\frac{b}{a} | a, b \in \mathbb{Z} \land a \neq 0 \}$

$\mathbb{Q} := \{\frac{b}{a} | a, b \in \mathbb{Z} \land a \neq 0\}$ mit der zuätzlichen Vereinbarung $\frac{b}{a}=\frac{d}{c} \iff b \cdot c = a \cdot d$

$\mathbb{Z} \ni b \mapsto \frac{b}{1} \in \mathbb{Q}$

### Rechenoperationen

$\frac{b}{a} + \frac{d}{c} := \frac{b \cdot c + a \cdot d}{a \cdot c}$

$\frac{b}{a} \cdot \frac{d}{c} := \frac{b \cdot d}{a \cdot c}$

$\frac{b}{a} : \frac{d}{c} := \frac{b}{a} \cdot \frac{c}{d}$ wenn $d \neq 0$

Jede rationale Zahl $q \in \mathbb{Q}$ hat genau eine Darstellung als unkürzbarer Bruch mit positivem Nenner $q = \frac{b}{a}$ mit $ggT(a, b) = 1$ und $a \geq 1$.

Neue Rechenregel: Wenn $q \neq 0$, dann ist $q \cdot q^{-1} = 1$ ($\frac{a}{b} \cdot \frac{b}{a} = 1$)

$q, r \in \mathbb{Q} \land q < r \implies q < \frac{q + r}{2} < r$

> **Satz**: Es gibt kein $q \in \mathbb{Q}$ mit $q^2 = 2$.
>
> **Beweis**: Annahme - Es gibt ein $q \in \mathbb{Q}$ mit $q^2 = 2$.\
> $\implies (\exists a, b \in \mathbb{Z})(q = \frac{a}{b} \land ggT(a, b) = 1 \land a, b \geq 1)$\
> $\implies (\frac{a}{b})^2 = 2$\
> $\implies a^2 = 2b^2$\
> $\implies 2|a^2$\
> $\implies 2|a$\
> $\implies (\exists a_0, a \in \mathbb{Z})(a = 2a_0)$\
> $\implies (2a_0)^2 = 2b^2$\
> $\implies 4a{_0}{^2} = 2b^2$\
> $\implies 2a{_0}^2 = b^2$\
> $\implies 2|b$\
> &#9889; da $2|a \land 2|b$ sein müsste, aber $\frac{a}{b}$ vollständig gekürzt ist

## Reelle Zahlen

### Dezimalbrüche

Ein Dezimalbruch besteht aus:

1. Vorzeichen + oder - ($v \in \{+1, -1\}$)
2. Funktion $d: \mathbb{N} \longrightarrow \mathbb{N}$ (Folge)
    - $d_0 \in \mathbb{N}$
    - $(\forall i \in \mathbb{N}^+)(d_i \in \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\})$
- Schreibweise: $\pm d_0.d{_1}d{_2}d{_3}d{_4}d{_5}...$

#### Periodische Dezimalbrüche

Ein Dezimalbruch $\pm d{_0}.d{_1}d{_2}d{_3}...$ heißt periodisch, wenn es ein $l, k \in \mathbb{N}$ gibt mit $l \geq 1, k \geq 0$, sodass für alle $d_k$ $i \in \mathbb{N}, i > k$ gilt: $d_i = d_{i+l}$

Das kleinste $l$ mit dieser Eigenschaft heißt die Periodenlänge.\
Schreibweise: $d{_0}.d{_1}d{_2}...\overline{d_{k}d_{k+1}d_{k+2}...d_{k+l}}$\
Spezialfall: Abbrechender Dezimalbruch - $d_0.d_1d_2...d_k\overline{0}$

### Definition

$\mathbb{R} := \{ \pm d | \pm d \enspace (unendlicher) \enspace Dezimalbruch \}$

- $+0 = -0$
- Neunerende: $d_0.d_1d_2..d_k\overline{9} = d_0.d_1d_2...d_{k-1}(d_k+1)$ mit $d_k < 9$

#### Lexikographische Ordnung <

Positives Vorzeichen:

- $0 < +d_0.d_1d_2d_3... < +e_0.e_1e_2e_3...$ falls $d_0 < e_0$ oder falls $d_0 = e_0 \land d_1 < e_1$ oder falls $d_0 = e_0 \land d_1 = e_1 \land d_2 < d_2$ etc.

Negatives Vorzeichen: Umgekehrt

#### Abbrechender Dezimalbruch

$\mathbb{R} \ni d_0.d_1d_2d_3...d_n \mapsto d_0 + \frac{d_1}{10} + \frac{d2}{100} + \frac{d_3}{1000} + ... + \frac{d_n}{10^n} \in \mathbb{Q}$

Zum Dezimalbruch $d_0.d_1d_2d_3...$ heißt $d^{[n]}=d_0.d_1d_2...d_n$ die n-te Näherung von d.

#### Zuordnung Dezimalbruch $\Leftrightarrow$ Rationale Zahl

Sei $q = \frac{a}{b} \in \mathbb{Q}$

Durch fortgesetzte Division kann man $q$ einen Dezimalbruch $\in \mathbb{R}$ zuordnen.

```python
 16 : 7 = 2.285714
-14
  20
 -14
   60
  -54
    40
   -35
     50
    -49
      10
      -7
       30
      -28
        2
```

$16 : 7 = 2.\overline{285714}$

Umgekehrt: Periodischer Dezimalbruch $\longmapsto$ rationale Zahl

$x = 3.1\overline{72} \quad | \cdot 10^2$\
$10^2 \cdot x = 317.2 \overline{72}$\
$10^2 \cdot x - x = 317.2 \overline{72} = 317.2 - 3.1 = 314.1$\
$99x = 314.1$\
$990x = 3141$
$x = \frac{3141}{990} = \frac{349}{110}$

Die rationalen Zahlen entsprechen so genau den periodischen Dezimalbrüchen. In diesem Sinne gilt: $\mathbb{Q} \subseteq \mathbb{R}$

TODO: Ergänzen!

```python
def to_fraction(start, repeating):
    t = 10**(len(str(repeating)))
    x = float(str(start) + str(repeating))
    b = (t - 1) * x - x
    return (b, t-1)
```

 $\frac{16}{7}_{(10)}$

```python
 16 : 7 = 10.010
-14
  2->4
     4->8
       -7
        1->2
           2->4
```

$10000_{(2)}:111_{(2)}=10.\overline{010}_{(2)}$

```python
 11 : 6 = 1.110
 -6
  5->10
     -6
      4->8
        -6
         2->4
            4->8
```

$1011_{(2)} : 110_{(2)} = 1.1\overline{10}_{(2)}$

### Schranken

> **Definition**: \
> Sei $A \subseteq R, A \neq \emptyset$. Eine Zahl $s \in \mathbb{R}$ heißt obere Schranke von A wenn $(\forall a \in A)(a \leq s)$.
> Wenn solch eine obere Schranke existiert, heißt $A$ nach oben beschränkt.
>
> Analog heißt $\tilde{s} \in \mathbb{R}$ untere Schranke $\iff (\forall a \in A)(\tilde{s} \leq a)$. In diesem Fall heißt $A$ nach unten beschränkt.

A sei nach oben beschränkt. Wenn $\{s \in \mathbb{R} | s \enspace obere \enspace Schranke \enspace von \enspace A\}$ ein kleinstes Element enthält, so heißt dieses Supremum.

$\sup{A} := \min \{ s \in \mathbb{R} | (\forall a \in A) a \leq s \}$

Analog: Infinum (größte untere Schranke):

$\inf{A} := \max \{ s \in \mathbb{R} | (\forall a \in A) a \leq s \}$

> **Satz**: Wenn $A \subseteq \mathbb{R}, A \neq \emptyset$, A nach oben beschränkt, dann existiert $\sup{A}$.\
> Wenn $A \subseteq \mathbb{R}, A \neq \emptyset$, A nach unten beschränkt, dann existiert $\inf{A}$.

$d, e \in \mathbb{R}, 0 < d, 0 < e$\
$d + e := \sup \{d^{[n]} + e^{[n]} | n \in \mathbb{N} \}$

$d \cdot e := \sup \{d^{[n]} \cdot e^{[n]} | n \in \mathbb{N} \}$

### Abzählbarkeit

$\mathbb{N} \sim \mathbb{Q}$

$\mathbb{N} \sim \mathbb{Q}^+$

$\frac{a}{b} \in \mathbb{Q}, \quad a, b \geq 1$

"Höhe" $h(\frac{a}{b}) := a + b$

$\mathbb{N} \nsim \mathbb{R}$ (Cantors Diagonalbeweis)

rational | irrational\
algebraisch | transzendent

### Identitäten in den reellen Zahlen

$\forall x, y, z \in \mathbb{R}$

$x + y = y + x$\
$(x + y) + z = x + (y + z)$\
$x + 0 = x$\
$x + (-x) = 0$\
$xy = yx$\
$(xy)z = x(yz)$\
$x(y+z)=xy+xz$\
$x \cdot 1 = x$\
$x \neq 0 \implies x \cdot x^{-1} = 1$

### Erweiterte reelle Zahlen

$\mathbb{R}_{erw} := \mathbb{R} \cup \{- \infty, + \infty \}$

$(\forall x \in \mathbb{R})( -\infty < x < +\infty)$

$\mathbb{R}^+ := \{x \in \mathbb{R} | x > 0\}$, $\mathbb{R}^+_0 := \{x \in \mathbb{R} | x \geq 0\}$

$\mathbb{R}^- := \{x \in \mathbb{R} | x < 0\}$, $\mathbb{R}^-_0 := \{x \in \mathbb{R} | x \leq 0\}$

### Intervalle

$a, b \in \mathbb{R}, a < b$

Offen: $(a, b) = ]a, b[ := \{x \in \mathbb{R} | a < x < b\}$

Geschlossen: $[a, b] := \{x \in \mathbb{R} | a \leq x \leq b\}$

Halboffen: $[a, b) := \{x \in \mathbb{R} | a \leq x < b\}$

$(a, b] := \{x \in \mathbb{R} | a < x \leq b \}$

$[a, +\infty):= \{x \in \mathbb{R} | a \leq x \}$

$(a, +\infty):= \{x \in \mathbb{R} | a < x \}$

$(-\infty, +\infty) = \mathbb{R}$

## Rechenregeln

### Potenzgesetze

$x \in \mathbb{R}, \quad m, n \in \mathbb{N}$

$x^0 := 1$ (auch $0^0=1$)

$n \geq 1 \implies x^n = \overbrace{xxx...x}$

$x^{n+1}=x^nx$

$x^{m+n}=x^m \cdot x^n = (x^n)^m$

$x \in \mathbb{R}, x \neq 0, m, n \in \mathbb{N}^+, m,n \geq 1$

$x^{-1} = \frac{1}{x}$

$x^{-n} = (\frac{1}{x})(\frac{1}{x})(\frac{1}{x})...(\frac{1}{x}) = \frac{1}{x^n}$

$x^{m-n} = \frac{x^m}{x^n} = x^m \cdot x^{-n}$

#### Potenz- und Wurzelfunktionen

$n \geq 1$

$pot_n : \mathbb{R} \Rightarrow \mathbb{R}, x \longmapsto x^n$

Beispiel: ![f(x)=x^3](cubed.png)

Für alle $n \geq 1$ gilt: $pot_n : \mathbb{R}^+_0 \longrightarrow \mathbb{R}^+_0$ ist bijektiv

Umkehrfunktionen $root_n : \mathbb{R}^+_0 \rightarrow \mathbb{R}^+_0, x \mapsto \sqrt[n]{x}$

$root_n(pot_n(x)) = x$\
$pot_n(root_n(x)) = x$\
$\sqrt[n]{x^n} = \sqrt[n]{x}^n = x$

$(\sqrt[m]{x})^n = \sqrt[m]{((\sqrt[m]{x})^n)^m} = \sqrt[m]{(\sqrt[m]{x})^{nm}} = \sqrt[m]{((\sqrt[m]{x})^m)^n} = \sqrt[m]{x^n}$

$x^{\frac{m}{n}} := (\sqrt[m]{x})^n = \sqrt[m]{x^n}$, speziell $x^{\frac{1}{m}}=\sqrt[m]{x}$

$(x^{\frac{a}{b}})^{\frac{c}{d}} = x^{\frac{ac}{bd}}$, $x^{\frac{a}{b}+\frac{c}{d}} = x^{\frac{ad + bc}{bd}}$

---

$\alpha \in \mathbb{R}, \alpha$ irrational\
$x > 0$

$x^\alpha = ?$

Ordentliche Folge (q) von rationalen Zahlen $q_n$

mit $\lim_{x \to \infty}{q}=x$

$exp(z) = e^z = \sum^{\infty}_{k=0} \frac{z^k}{k!}$

Aufgabe: $\sqrt[4]{a^{\frac{2}{3}}}$

$\sqrt[4]{a^{\frac{2}{3}}} = (a^\frac{2}{3})^\frac{1}{4} = a^{\frac{2}{12}} = a^{\frac{1}{6}}$

$\sqrt[8]{a^2b \cdot \sqrt[4]{b^{12}}} = (a^2b \cdot (b^{12})^\frac{1}{4})^\frac{1}{8} = a^\frac{1}{4} \cdot b^\frac{1}{2}$