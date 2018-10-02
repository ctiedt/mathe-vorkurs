# Rechnen mit reellen Zahlen

## Formeln

### Summenzeichen

$$\sum^n_{i=m} f(i) := \begin{cases} 0 \impliedby n<m \\ f(m) + f(m+1) f(m+2) +...+ f(n) \impliedby n \geq m\end{cases}$$

Verallgemeinerung: $I$ sei endliche Menge.

$$\sum_{\alpha \in I} f(\alpha)$$

### Produktzeichen

$$
\prod^n_{i=m} f(i) :=
\begin{cases}
1 \impliedby n < m \\
f(m) \cdot f(m+1) \cdot f(m+2) \cdot ... \cdot f(n) \impliedby n \geq m
\end{cases}
$$

#### Übungsaufgaben

$$
\begin{aligned}
\sum^8_{i=1}i = 36  \quad \sum^{100}_{i=1}i = 5050 \\
\sum^{4}_{i=-4}i^3 = 0 \quad \sum^{10}_{i=2}3 = 27 \\
\prod^{5}_{i=1}i = 120 \quad \prod^{5}_{i=0}2 = 64
\end{aligned}
$$

- Laufvariable $i$ kann umbenannt werden, vorausgesetzt, die neue Variable kommt in $f(i)$ nicht vor
- **Indexverschiebung**: Laufbeginn und Laufende können verschoben werden, wenn dies zu einer "bequemeren" Form führt
  
$$
\sum^n_{i=m}f(i) = \sum^{n+k}_{i=m+k}f(i-k) = \sum^{n-k}_{i=m-k}f(i+k)
$$

- Will $1+3+5+...+(2n-3)+(2n-1)$ mit Summenzeichen schreiben

$$
\sum^{n}_{i=1}(2i-1) = \sum^{n+2}_{i=3}(2i-5) = \sum^{n-1}_{i=0}(2i+1) = \sum^{n-3}_{i=-2}(2i+5)
$$

Gesetze:

$$
\begin{aligned}
\sum^{n}_{i=m}(f(i)+g(i)) = \sum^{n}_{i=m}f(i) + \sum^{n}_{i=m}g(i) \\
\sum^{n}_{i=m} a \cdot f(i) = a \cdot \sum^{n}_{i=m} f(i) \\
\prod^{n}_{i=m}(f(i) \cdot g(i))= (\prod^{n}_{i=m}f(i)) \cdot (\prod^{n}_{i=m}g(i)) \\
\prod^n_{i=m}f(i)^a = (\prod^n_{i=m}f(i))^a \\
\log_a(\prod^n_{i=m}f(i)) = \sum^n_{i=m} \log_a(f(i)) \\
\sum^{n}_{i=m} \sum^{b}_{j=a}f(i, j) = \sum^{b}_{j=a} \sum^{n}_{i=m}f(i, j) = \sum_{(i, j) \in \{m, m+1, ..., n\} \times \{a, a+1, ..., b\}}f(i, j)
\end{aligned}
$$

> Für kommutative und assoziative Operationen kann man diese Schreibweisen übertragen.
>
> Beispiele:
> $\cup^n_{i=m} := \begin{cases} \emptyset \impliedby n < m \\ A_m \cup A_{m+1} \cup A_{m+2} \cup ... \cup A_n \impliedby m \leq n \end{cases}$\
> $\cup\{A_i | i \in I \} = \cup_{i \in I}A_i = \{a | (\exists i \in I) a \in A\}$
>
> $\cap^n_{i=m}A_i = \begin{cases} \mathbb{M} \impliedby n < m \\ A_m \cap A_{m+1} \cap A_{m+2} \cap ... \cap A_n \impliedby m \leq n \end{cases}$

#### Geometrische Summe

$$x \in \mathbb{R}, \sum^n_{i=0}x^i = (1+x+x^2+x^3+...+x^{n-1}+x^n)$$

$$
\begin{gathered}
(\sum^n_{i=0}x^i) \cdot (1 - x) = (\sum^n_{i=0}x^i) -(x\sum^n_{i=0}x^i) \\ = (1 + x + x^2 +... + x^n) - x(1 + x + x^2 + ... + x^n) = (1 + x + x^2 +...+ x^n) - (x + x^2 + x^3 + ... + x^n + x^{n+1}) = 1 - x^{n+1} \\
\implies \sum^n_{i=0}x^i = 1 + x + x^2 +...+ x^n = \begin{cases}
\frac{1-x^{n+1}}{1-x} \impliedby x \neq 1 \\
n + 1 \impliedby x = 1
\end{cases}
\end{gathered}$$

## Fakultät und Binomialkoeffizienten

$n!$ "n Fakultät", $n \in \mathbb{N}$

$0! = 1, \quad (n+1)! := (n!) \cdot (n+1)$

$$n! = 1 \cdot 2 \cdot 3 \cdot ... \cdot (n-1) \cdot n = \prod^n_{i=1}i, \quad (n \geq 1)$$

Die Fakultät $n!$ wächst schneller als $a^n$ für ein beliebiges $a$.

### Kombinatorische Bedeutung

$n! =$ Anzahl der Möglichkeiten, $n$ (paarweise disjunkte) Elemente in einer Reihe anzuordnen (Permutationen von $n$ Objekten)

### Exkurs: Was ist 10000! ?

Wissenschaftliche Notation: $d_0.d_1d_2...d_k \cdot 10^e$ ($e \in \mathbb{Z}$, Exponent)

Normalisiert: $d_0.d_1d_2...d_k \cdot 10^e$ mit $d_0 \neq 0$

Bsp.: $0.034 \cdot 10^7 = 3.4 \cdot 10^5 = 3.4E5$

#### Stirling'sche Formeln

grob: $n! \approx \sqrt{2 \pi n} \cdot (\frac{n}{e})^n$

genauer: $(\exists \Theta \in \{-1, +1\}) n! \approx \sqrt{2 \pi n} \cdot (\frac{n}{e})^n \cdot e^{\frac{1}{120} + \frac{\Theta}{120 n^2}}$

$z \in \mathbb{Z}, z \geq 1, B \in \mathbb{Z}, B \geq 2$

Wie viele Ziffern n hat z in Basis B?

$$
\begin{aligned}
B^{n-1} \leq z < B^n\\
\log_B(B^{n-1}) \leq \log_B(z) < \log_B(B^n) \\
n - 1 \leq \log_B(z) < n \\
n - 1 = \lfloor \log_B(z) \rfloor , \quad n = \lfloor \log_B(z) \rfloor + 1
\end{aligned}
$$

$10000! = 10^{\log(10000!)} = 10^{35659.4542} = 10^{0.4542} \cdot 10^{35659} \approx \underline{\underline{2.8 \times 10^{35659}}}$

### Binomialkoeffizient

$m, n \in \mathbb{N}, m \leq n$

$\binom{n}{m} = \frac{n!}{m! \cdot (n - m)!}$

$\binom{n}{0} := 1, \binom{0}{0} = 1, \binom{n}{1} = n, \binom{n}{n} = 1$, ($\binom{n}{m} = 0$ falls $n < m$)

$\binom{n}{m}=\binom{n}{n-m}$

$\binom{n}{m} + \binom{n}{m+1} = \binom{n+1}{m+1}$

#### Kombinatorische Bedeututng des Binomialkoeffizienten

$\binom{n}{m} =$ Anzahl der m-elementigen Teilmengen einer n-elementigen Menge

$$
\begin{gathered}
\binom{0}{0}\\
\binom{1}{0} \quad \binom{1}{1}\\
\binom{2}{0} \quad \binom{2}{1} \quad \binom{2}{2} \\
\binom{3}{0} \quad \binom{3}{1} \quad \binom{3}{2} \quad \binom{3}{3} \\
\binom{4}{0} \quad \binom{4}{1} \quad \binom{4}{2} \quad \binom{4}{3} \quad \binom{4}{4}
\end{gathered}
$$

$\binom{n}{m_1, m_2, m_3, ..., m_l} := \frac{n!}{m_1! \cdot m_2! \cdot m_3! \cdot ... \cdot m_l!}$ - Anzahl der Möglichkeiten, eine n-elementige Menge so in l Mengen zu zerlegen, dass die erste $m_1$ Elemente, die zweite $m_2$ Elemente, ..., die l-te $m_l$ Elemente enthält.

## Faktorisierung, Binomische Formeln

**Distributivgesetz**: $a \cdot b + a \cdot c = a \cdot (b + c)$\
$a \cdot c + a \cdot d + b \cdot c + b \cdot d = (a+b)(c+d)$

### Binomische Formeln

- $a^2 + 2ab + b^2 = (a+b)^2$
- $a^2 - 2ab + b^2 = (a-b)^2$
- $a^2 - b^2 = (a+b)(a-b)$

> **Binomischer Satz**:
> $$(a+b)^n = \sum^n_{m=0}a^{n-m} \cdot b^m = a^n + n \cdot a^{n-1} \cdot b + \binom{n}{2} \cdot a^{n-2} \cdot b^2 + ... + n \cdot a \cdot b^{n-1} + b^n$$

$4a^2 + 9b^2 + 12ab = (2a + 3b)^2$

$x^2 + 6xz - y^2 + 9z^2 = (x + 3z)^2 - y^2 = (x + 3z + y)(x + 3z - y)$

#### Regel von Vieta

$(x - a)(x - b) = x^2 - (a + b) \cdot x + a \cdot b$

$(x - a)(x - b)(x - c) = x^3 - (a + b + c) \cdot x^2 + (a \cdot b + a \cdot b + a \cdot c) \cdot x - a \cdot b \cdot c$

Aufgaben:

$x^2 - 13.5x + 45 = (x - 7.5)(x - 6)$

$x^2 + x - 56 = (x - 7)(x + 8)$

$a \cdot (c + b) - c \cdot (b + a) + b \cdot (c - a) =(ab + ac) - (ab + ac) + (ab - ac) = 0$

$(b - a)(a + b) + (c + b - a)(c - b - a) - (b - c)^2 = (b^2-a^2) +(c^2-bc-ac+bc-b^2-ab-ac+ab+a^2) - (b - c)^2 = -b^2 -2ac +2bc$

## Etwas Bruchrechnung

Bruchstrich = Division

$\frac{a}{b} + \frac{c}{d} = \frac{ad + cb}{bd}$, $\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}$, $\frac{a}{b} : \frac{c}{d} = \frac{ad}{bc}$

**Doppelbrüche**: Sofort auflösen

$\frac{\frac{2}{3}}{5} = \frac{2}{3} \cdot \frac{1}{5} = (2:3):5$

$$\frac{x+3}{x^2-4} + \frac{x-3}{x-2} = \frac{(x+3)(x-2) + (x-3)(x^2-4)}{(x^2-4)(x-2)} = \frac{x^2-3}{x^2-4}$$

$$\frac{3}{\frac{x+3}{x-2}} + \frac{\frac{x-102}{x-4}}{x+3} = 3 \frac{x-2}{x+3} + \frac{x-102}{(x-4)(x+3)}= \frac{3x-26}{x-4}$$

### Vergleichen von Brüchen

- swoeit wie möglich kürzen
- Wurzeln möglichst aus Nennern entfernen

$\frac{1}{\sqrt{2}} = \frac{1}{\sqrt{2}} \cdot \frac{\sqrt{2}}{\sqrt{2}} = \frac{\sqrt{2}}{2}$

## Proportionalität

Wir sprechen oft von **Größen** (zeit, Weg, Länge, Breite...)

Eine solche Größe $X$ ist gekennzeichnet durch

- Name
- Menge von möglichen Werten, die die Größe annehmen kann, eventuell versehen mit Einheiten
  - Zur Vereinfachung nehmen wir an, dass alle Zahlenwerte aus $\mathbb{R}^+$ sind
- Falls $x$ ein möglicher Wert der Größe $X$ ist, so schreiben wir $x \in X$

In verschiedenen Zusammenhängen kommen verschiedene Größen vor, die abhängig von einander sind.

Die Menge aller möglichen Zusammenhänge beschreiben wir mit einer Menge von $(n+m)$-Tupeln $\mathbb{M} \subseteq X_1 \times X_2 \times ... \times X_n \times Y_1 \times Y_2 \times ... \times Y_m$

> **Definition**: Zwei Größen $X$ und $Y$ heißen proportional, $X \sim Y$, wenn es ein $c \in \mathbb{R}^+$ gibt, sodass $\mathbb{M} \subseteq X \times Y$ folgende Form hat:
> $$\mathbb{M} = \{(x, y) \in X \times Y | \quad x \cdot c = y\}$$
>
> Der Wert $c$ heißt Proportionalitätsfaktor.
>
> Zwei Größen heißen umgekehrt proportional, $X_1 \sim \frac{1}{X_2}$, wenn es ein $c \in \mathbb{R}^+$ gibt, sodass
> $$\mathbb{M} = \{(x_1, x_2) \in X \times Y | \quad c \cdot x_1 \cdot x_2 = 1\}$$
>
> Die Größen $X_1, ..., X_m, Y_1, ..., Y_n$ stehen in einer $(n, m)$-Proportionalitätsverkettung, wenn es ein $c \in \mathbb{R}^+$ gibt, sodass
> $$\mathbb{M} = \{(x_1, ..., x_m, y_1, ..., y_n) \in X \times Y | \quad c \cdot x_1 \cdot ... \cdot x_m = y_1 \cdot ... \cdot y_n\}$$

### Aufgabe: Nichts für Vegetarier

Für die Zerlegung von $7.2t$ Schweinehälften brauchen 14 Arbeiter $8h$. Wie viele Zerleger braucht man, um $6t$ Schweinehälften in $8h$ zu zerlegen?

12 Arbeiter.

### Prozentrechnung

Spezialfall der Proportionalität

Zwei proportionale Größen

- Prozente
- andere Größe $X$

$1\% = \frac{1}{100}, \quad 1$ &#x2030;$=\frac{1}{1000}$

Gewisse Quantität der Größe $X$ wird zu $100\%(=1)$ gesetzt. Anderen Werten w entspricht dann ein gewisser Teil der $100\%$.

Grundwert $G \in X, \quad G \hat{=} 100\%$

Prozentwert $w \in X, \quad w \hat{=} p \quad (\text{prozentisch in \%})$

$(\exists c \in \mathbb{R}^+)(G = c \cdot 100\%) \land (w= c \cdot p)$

$c = \frac{G}{100\%} = \frac{w}{p}$

#### Aufgabe: Der Kapitalismus in seinem Lauf

Artikel wird um $q\%$ verteuert. Wie viel Prozent war er vorher billiger?

$\frac{q}{1 + q} \%$

#### Herleitung der Sparkassenformel

Hier: nachschüssige Zinsen per anno (p.a.)

p - "Zinsfuß", Kapital wird mit p% p.a. verzinst

q: $1+\frac{p}{100}$ - "Zinsfaktor"

$\text{Kapital} \; k_0 \implies \text{ein Jahr später} \; k_1 = k_0 + k_0 \cdot \frac{p}{100} = k_0 \cdot q$

$k_n = k_0 \cdot q^n$

##### Problem

- Grundkapital $K_0$ (zu Jahresbeginn)
- jährlich mit $p\%$ verzinst
- Dazu wird am Beginn des nächsten Jahres eine feste Rate $R$ eingezahlt

Wie groß ist das Kapital $K_n$ nach $n$ Jahren?

$$
\begin{aligned}
K_0 \\
K_1 = K_0 \cdot q + R  \\
K_2 = K_1 \cdot q + R = K_0 \cdot q^2 + Rq + R \\
K_3 = K_2 \cdot q + R = K_0 \cdot q^3 + Rq^2 + Rq + R \\
K_n = K_0 \cdot q^n + R \cdot \frac{q^n - 1}{q - 1}
\end{aligned}
$$

##### Aufgabe: Zinsen

Sie nehmen einen Hypothekenkredit von 130 000 € zu einem Zinsfuß von 4.5% p.a. auf. Die Rückzahlung geschieht in gleich großen Jahresraten R, die jeweils nach Ablauf eines Jahres fällig sind (Die Höhe der letzten Rate kann kleiner als R sein).

(a) Wieviele Jahre müssen Sie zahlen, wenn R die Höhe von 5.5% von 130 000€ hat?

(b) Wie hoch muss R sein, wenn Sie den Kredit nach 20 Jahren zurückgezahlt haben wollen?

**(a)**:

$$\begin{gathered}
q = 1 + \frac{p}{100} = 1 + \frac{4.5}{100} = 1.045 \\
K_0 = 130000€ \\
|R| = 0.055 \cdot 130000€ = 7150€
\end{gathered}$$

$\text{Gesucht}: n$

```python
def kredit(n):
    k0 = 130000
    q = 1.045
    r = 7150
    return k0*q**n + r * (q**n - 1)/(q - 1)

n = 0
while kredit(n) > 0:
    n += 1

# n = 39
```

$n = 39 \; \text{Jahre}$

**(b)**:

$$
\begin{gathered}
R = \frac{q^n - 1}{q - 1} - K_0 \cdot q^n \\
R = 9993.90€
\end{gathered}
$$

## Polynome

> **Definition**: Sei $n \in \mathbb{N}$. Ein Polynom n-ten Grades in der Unbestimmten x ist ein Ausdruck der Form $f(x) = \sum_{k=0}^n a_k \cdot x^k$ mit $a_i \in \mathbb{R}$ für $i = 0..n$ und $a_n \neq 0$. Die $a_i$ heißen *Koeffizienten* von $f(x)$ und $a_n$ heißt *Leitkoeffizient* von $f(x)$.
>
> $\text{Grad}(f(x)) = n \equiv \deg(f(x)) = n$ \
> $\text{LK}(f(x)) = a_n$
>
> Es gibt noch ein weiteres Polynom, das *Nullpolynom* $0$. Das Nullpolynom hat keinen Leitkoeffizienten, und wir setzen $\text{Grad}(0) := -\infty$
>
> Die Menge aller Polynome in x wird mit $\mathbb{R}[x]$ bezeichnet.
>
> Beispiel: $f(x) = a_0, \; a_0 \neq 0, \; \text{Grad}(f(x)) = 0$

### Anmerkungen

1. Schreiben $f(x) \not\equiv 0$, falls $f(x)$ nicht das Nullpolynom ist
2. Falls $\text{Grad}(f(x)) = n, \; n <m, \; f(x) = \sum_{k=0}^n a_k \cdot x^k$, so schreiben wir manchmal auch $f(x) = \sum_{k=0}^m a_k \cdot x^k$. Dabei sind $a_{n+1} = a_{n+2} = ... = a_{m} = 0$ zu setzen
3. Ein normiertes Polynom hat $\text{LK}(f(x)) = 0$

### Rechnen mit Polynomen

Sei $f(x) = a_nx^n + ... + a_1x + a_0, \; a_n \neq 0$\
$g(x) = b_mx^m + ... + b_1x + b_0, \; b_m \neq 0$

Sei $k := \max \{n, m\}$

#### Addition

$$\begin{aligned}
f(x) + g(x) := \sum_{i=0}^k(a_i+b_i)x^i \\
0 + f(x) = f(x) + 0 := f(x)
\end{aligned}$$

#### Produkt

$$\begin{aligned}
f(x) \cdot g(x) := \sum_{i=0}^{n+m} (\sum_{j=0}^i a_j \cdot b_{i-j})x^i \\
f(x) \cdot 0 = 0 \cdot f(x) = 0 \\
\text{Sei } \alpha \in \mathbb{R}, \alpha \cdot f(x) := \sum_{i=0}^n (\alpha \cdot a_i)x^{i}
\end{aligned}$$

Für alle $f(x), \; g(x)$ gilt:

- $\text{Grad}(f(x)+g(x)) \leq \max \{ \text{Grad}(f(x)), \text{Grad}(g(x)) \}$
- $\text{Grad}(f(x) \cdot g(x)) = \text{Grad}(f(x)) + \text{Grad}(g(x))$
- $\text{LK}(f(x) \cdot g(x)) = \text{LK}(f(x)) \cdot \text{LK}(g(x))$
- $f(x) \not\equiv 0 \land g(x) \not\equiv 0 \implies f(x) \cdot g(x) \not\equiv 0$

$(2x^2 + x - 3)(x^3 + x^2 + 2) = (2x^5 + 2x^4 + 4x^2 + x^4 + x^3 +2x - 3x^3 - 3x^2 - 6) = (2x^5 + 3x^4 - 2x^3 + x^2 + 2x - 6)$

### Rechenregeln für Polynome

$$\begin{aligned}
(\forall f(x), g(x), h(x) \in \mathbb{R}[x]) \\
f(x) + g(x) = g(x) + f(x) \\
(f(x) + g(x)) + h(x) = f(x) + (g(x) + h(x)) \\
f(x) + 0 = f(x) \\
f(x) + (-f(x)) = 0 \\
f(x) \cdot g(x) = g(x) \cdot f(x)
(f(x) \cdot g(x)) \cdot h(x) = f(x) \cdot (g(x) \cdot h(x)) \\
f(x) \cdot 1 = f(x) \\
f(x) \cdot (g(x) + h(x)) = f(x) \cdot g(x) + f(x) \cdot h(x)
\end{aligned}
$$

### Polynomfunktionen

Zu jedem Polynom $f(x) = a_nx^n + ... + a_1x + a_0 \in \mathbb{R}[x]$ gehört die Polynomfunktion $f: \mathbb{R} \longrightarrow \mathbb{R}, c \longmapsto a_nc^n + ... + a_1c + a_0$

$f(c)$: Wert des Polynoms an der Stelle $x = c$

Falls $f(c) = 0$, so heißt $c$ *Nullstelle* von $f(x)$.

### Zur Berechnung

$a_nx^n + a_{n-1}x^{n-1} + ... + a_1x + a_0$

$= ((((a_nx + a_{n-1})x + a_{n-2})x + a_{n-3})x + ... + a_1)x + a_0$

| $a_n$ | $a_{n-1}$        | $a_{n-2}$                     | ... | $a_1$ | $a_0$  |
| ----- | ---------        | ---------                     | --- | ----- | -----  |
|   0   | $a_nc$           | $(a_nc + a_{n-1})c$           | ... |       |        |
| $a_n$ | $a_nc + a_{n-1}$ | $(a_nc + a_{n-1})c + a_{n-2}$ | ... |       | $f(c)$ |

### Satz von der Division mit Rest

Es seien $f(x), g(x) \in \mathbb{R}[x], \; g \not\equiv 0$.

Dann existieren eindeutig bestimmte Polynome $q(x), r(x) \in \mathbb{R}[x]$ mit
$f(x) = q(x) \cdot g(x) + r(x)$ und $\text{Grad}(r(x)) < \text{Grad}(g(x))$

### Polynomdivision

$(x^4 + 2x^3 + 6x^2 + 2x + 5) : (x^3 + 5x^2 + 11x + 15) = \overbrace{x - 3}^{q(x)}$\
$-(x^4 + 5x^3 + 11x^2 + 15x)$ \
$\qquad \;-3x^3 -5x^2 -13x + 5$\
$\qquad \; -(-3x^3 -15x^2 -33x -45)$\
$\qquad \; \; r(x) = 10x^2 + 20x + 50$

$$
\begin{aligned}
(x^3 + 5x^2 + 11x + 16):(x^2 + 2x + 5) = x + 3, r(x)=1 \\
-(x^3 + 2x^2 + 5x) \\
(3x^2 + 6x + 16) \\
\end{aligned}
$$

$$
\begin{aligned}
(2x^4 - x^3 -7x^2 + 6x + 3):(x-2) = 2x^3 + 3x^2 - x + 4\\
-(2x^4 - 4x^2) \\
(3x^3 - 7x^2 + 6x + 3) \\
-(3x^3 - 6x^2) \\
-x^2 + 6x + 3 \\
-(-x^2 + 2x) \\
4x + 3 \\
-(4x + 8) \\
11
\end{aligned}
$$

$$
\begin{aligned}
(x^2 + x - 1):(x - \frac{1}{2}) = x + \frac{3}{2}, \; \text{Rest } -\frac{1}{4}\\
-(x^2 - \frac{1}{2}x) \\
\frac{1}{2}x - 1 \\
\end{aligned}
$$

> **Definition**: Ein Polynom $g(x) \in \mathbb{R}[x], \; g(x) \not\equiv 0$ heißt Teiler von $f(x) \in \mathbb{R}[x]$, wenn es ein Polynom $h(x) \in \mathbb{R}[x]$, sodass $h(x) \cdot g(x) = f(x)$.
> $$g(x)|f(x) \iff (\exists h(x) \in \mathbb{R}[x]) h(x) \cdot g(x) = f(x)$$
> **Gleichbedeutend**: Der Rest $r(x)$ bei Division von $f(x)$ durch $g(x)$ ist $r(x) \equiv 0$.

$f(x) = q(x) \cdot (x - c) + r_0, \quad (r_0: \text{Konstante aus } \mathbb{R})$

$r_0 = 0 \implies f(x) = q(x) \cdot (x - c)$ \
$\implies (x - c) | f(x)$ \
$f(c) = q(c) \cdot \underbrace{(c - c)}_0 + \underbrace{r_0}_0 = 0$ \
$\implies \text{c ist Nullstelle von } f(x)$

$\implies 0 = f(c) = q(c) \cdot \underbrace{(c - c)}_0 + r_0$\
$\implies 0 = r_0$

> **Satz**: $c \in \mathbb{R}$ ist genau dann Nullstelle von $f(x) \in \mathbb{R}[x]$, wenn $(x - c) | f(x)$
> $$ f(x) = 0 \iff (x - c) | f(x) $$
---
> **Vielfachheit einer Nullstelle**: Sei $f(c)=0$. Dann folgt $(x - c) | f(x)$. Aber: Es ist möglich, dass $f(x)$ mehrfach durch $(x - c)$ teilbar ist.
>
> $\text{Vielfachheit der Nullstelle} c := \max \{k \in \mathbb{N} | (x - c)^k|f(x) \}$\
> $\text{c Nullstelle} \implies k \geq 1, \quad k \leq \text{Grad}(f(x))$
>
> $\implies \overbrace{c_1, ..., c_l}^{\text{paarweise verschieden}}$ seien die Nullstellen von $f(x)$ mit $\text{Grad}(f(x)) = n \geq 1$. $k_1, ..., k_l$ seien die zugehörigen Vielfachheiten. Dann folgt $f(x) = (x - c_1)^{k_1} \cdot (x - c_2)^{k_2} \cdot ... \cdot (x - c_l)^{k_l} \cdot f_0(x)$, wobei $f_0(x)$ keine Nullstellen in $\mathbb{R}$ hat.\
> $\implies k_1 + k_2 + ... + k_l \leq n$\
> Ein Polynom n-ten Grades kann in $\mathbb{R}$ höchstens n Nullstellen haben, wobei die Nullstellen mit ihren Vielfachheiten gezählt werden.

Sei $g(x) \in \mathbb{R}[x]$. Dann heißt $g(x)$ ein *Primpolynom* (oder irreduzibel), wenn

- $n = \text{Grad}(g(x)) \geq 1$
- $(\forall h(x) \in \mathbb{R}[x]) \quad h(x)|g(x) \implies \text{Grad}(h(x)) \in \{0, n \}$

**Gilt**: Jedes Polynom $f(x)$ mit $\text{Grad(f(x))} \geq 1$ hat eine Darstellung als Produkt von Primpolynomen.

### Primpolynome aus $\mathbb{R}[x]$

- Polynome vom Grad 1
- Polynome vom Grad 2, die keine Nullstellen in $\mathbb{R}$ haben

### Nullstellen von Polynomen vom Grad $\geq 1$

$n = 1, \quad f(x) = a_1x + a_0 \text{ mit } a_1 \neq 0$\
$a_1x + a_0 = 0 \iff x = -\frac{a_0}{a_1}$

$n = 2, \quad f(x) = a_2x^2 + a_1x + a_0 \text{ mit } a_2 \neq 0$\
$x^2 + px + q = 0 \text{ mit } p = \frac{a_1}{a_2}, \; q = \frac{a_0}{a_2}$\
$x_1, x_2 = -\frac{p}{2} \pm \sqrt{(\frac{p}{2})^2 - q}$

#### Aufgabe: Nullstellen von Polynomen zweiten Grades

$4x^2 + 4x - 3 =$

$x^2 + x - \frac{3}{4} = 0 \implies x_1, x_2 = -\frac{1}{2} \pm \sqrt{\frac{1}{4} + \frac{3}{4}} \implies x_1 = \frac{1}{2}, x_2 = -\frac{3}{2}$

$3x^2 - x - 10 =$

$x^2 -\frac{1}{3}x - \frac{10}{3} = 0 \implies x_1, x_2 = \frac{1}{3} \pm \sqrt{\frac{1}{9} + \frac{30}{9}} \implies x_1 = 2, x_2 = -\frac{5}{3}$

Sei $a_2 = 1, \quad f(x) = (x + \frac{p}{2})^2 + q - (\frac{p}{2})^2$

```python-exec
import plots

plots.draw_function(f= plots.parabola, fn="./html/parabola.png", interval=[-5, 5], title_="f(x) =  (x + 4/2)^2 + 2 - (4/2)^2")

print("![parabola.png](parabola.png)")
```

| Fall          | Bedeutung                               |
| ------------- | --------------------------------------- |
| $a_2 > 1$     | Parabel gestreckt (Nullstellen bleiben) |
| $0 < a_2 < 1$ | Parabel gestaucht (Nullstellen bleiben) |
| $a_2 < 0$     | Spiegelung der Parabel an der x-Achse   |

#### Fall $n=3$

$f(x) = a_3x^3 + a_2x^2 + a_1x + a_0$

$f(x) = 0 \xrightarrow{\text{Substitution}} z^3 + pz + q = 0$

Substitution: $z = u + w$

$(u+w)^3 + p(u+w) + q = 0$\
$u^3 + 3u^2w + 3uw^2 + w^3 + p(u + w) + q = 0$\
$\underbrace{(u^3+w^3+q)}_0 + \underbrace{(3uw + p)}_{0}(u + w) = 0$

> **Satz**: Sei $f(x) = \sum_{i=0}^n a_ix^i$ mit $a_n \neq 0$ und $a_i \in \mathbb{Z}$ für $i = 0..n$. Weiter sei $\frac{p}{q}$ eine vollständig gekürzte, rationale Nullstelle mit $p, q \in \mathbb{Z}, \; q \geq 1, \; \text{ggT}(p, q) = 1$. Dann gilt $p|a_0$ und $q|a_0$.
> Falls $a_n = 1$, dann ist $q=1$. Jede rationale Nullstelle ist dann ganzzahlig.

#### Fall $n=4$

Da gibt's Formeln für. Angeblich.

#### Fall $n=5$

Da gibt's keine allgemeine Formel für. Und dabei hat man schon ewig gesucht. Galois hat die Suche für unsinnig erklärt und ist dann mit 20 oder so in einem Duell gestorben.

> "Wie kann man sich nur so jung erschießen lassen?" - Dr. Börner über Galois

## Lösen von Gleichungen und Ungleichungen

> **Terme**: Ein (Funktions-)Term ist ein "vernünftig aufgebauter" Ausdruck zur Beschreibung einer Funktion. Terme können aus folgenden Dingen bestehen:
>
> - Zeichen für Variablen und Parameter
> - Zahlen, Konstanten
> - Grundoperationen
> - Funktionszeichen
> - Technische Zeichen
>
> Meist bezeichnen wir Terme mit $f(x), g(x)...$ wie Funktionen, *aber*:
>
> - Jeder Term definiert **eine** Funktion
> - Eine Funktion kann durch **verschiedene** Terme beschrieben werden

Zu einem Term $f(x)$ gehört ein **maximaler Definitionsbereich**. Das ist die größte Teilmenge von $\mathbb{R}$, für die alle Teilterme von $f(x)$ definiert sind. Den Definitionsbereich von $f(x)$ bezeichnen wir mit $D_f$. Dieser kann eventuell eingeschränkt werden. Damit definiert ein Term $f(x)$ eine Funktion $f(x)$.

$$f: D_f \longrightarrow \mathbb{R}, x \longmapsto f(x)$$

### Umformungen von Termen

Termumformungen müssen die zugehörige Funktion unverändert lassen, einschließlich $D_f$. Gegebenenfalls müssen Änderungen separat angegeben werden.

**Beispiel**: $f(x) = \frac{x^2-x-6}{x+2}, \; D_f = \mathbb{R}\setminus\{-2\}$

$f(x) = \frac{(x+2)(x-3)}{(x+2)} = x - 3 \underline{\text{ mit } x \neq -2}$

## Gleichungen

$f(x), g(x)$ Funktionsterme.

**Gleichung**: $f(x) = g(x)$

Lösungsmenge $L = \{x \in D_f \cup D_g | f(x) = g(x) \}$

Sei $\tilde{f}(x) = \tilde{g}(x)$ eine weitere Gleichung mit $\tilde{L} = \{x \in D_{\tilde{f}} \cup D_{\tilde{g}} | \tilde{f}(x) = \tilde{g}(x) \}$

> Die Gleichungen $f(x)=g(x)$ und $\tilde{f}(x)=\tilde{g}(x)$ heißen äquivalent, falls $L = \tilde{L}$, man schreibt $f(x)=g(x) \iff \tilde{f}(x) = \tilde{g}(x)$.

Bei **äquivalenten Umformungen** ändert sich die Lösungsmenge nicht. Manchmal betrachtet man auch nichtäquivalente Umformungen.

**Folgerungen**: $f(x) = g(x) \implies \tilde{f}(x) = \tilde{g}(x) \text{ falls } L \subseteq \tilde{L}$

### Lineare Gleichungen

$ax + b = 0$

#### Fall 1

$a = 0 \implies ax + b = b \implies b = 0$

**Fall 1A**: $b \neq 0 \implies L = \emptyset$

**Fall 1B**: $b = 0 \implies L = \mathbb{R}$

### Gleichungen mit Beträgen

$|a| := \begin{cases} a \text{ falls } a \geq 0 \\ -a \text{ falls } a < 0\end{cases}$

$|a| = \sqrt{a^2}$

$|a| \geq 0, |a| = 0 \iff a = 0$

$|a \cdot b| = |a| \cdot |b|, \quad |\frac{a}{b}| = \frac{|a|}{|b|}, \quad (b \neq 0)$

- $|f(x)| = c$
- Falls $c < 0$, so $L = \emptyset$
- Falls $c \geq 0$, so $|f(x)|=c \iff f(x)=c \lor f(x)= -c$

$|f(x)| = |g(x)| \iff f(x)^2 = g(x)^2$

Falls $g(x) \neq 0 \quad |f(x)|=|g(x)| \iff |\frac{f(x)}{g(x)}| = 1$

### Quadratische Gleichungen

$\frac{6}{x^2 - 9} + \frac{1}{x + 3} = 1$

Nullstelle: 4

### Gleichungen mit Wurzeln

- Beachte: $\sqrt{h(x)}$ (bei Dr. Börner $(\forall n \in \mathbb{N})(\sqrt[n]{h(x)})$) nur für $h(x) \geq 0$  definiert
- Quadrieren ist i.a. **keine** äquivalente Umformung, eine PROBE ist notwendig
  - kann aber äquivalent gemacht werden
  - $f(x)=g(x) \iff \begin{cases} f(x) \geq 0 \land g(x) \geq 0 \land f(x)^2 = g(x)^2 \lor \\ f(x) < 0 \land g(x) < 0 \land f(x)^2 = g(x^2) \end{cases}$

### Lösen mit Substitution

$x^4 -2x^2 = 15$ (biquadratische Gleichung)

**Substitution**: $z = x^2 \implies z \geq 0$

$z^2 - z = 15$

Lösen der Gleichung ergibt: $z = 5 \implies x = \pm \sqrt{5}$

### Umkehrfunktionen

$f: A \to B \text{ umkehrbar} \iff f \text{ bijektiv}$

$f: A \to B \text{ umkehrbar i.e.S} \iff f: A \to \text{Bild}(f) = f(A)$

$f: A \to B \text{ umkehrbar i.e.S} \iff f: A \to B \text{ injektiv}$

Funktion $f$ sei durch Term $f(x)$ gegeben.

- maximaler Definitionsbereich $D_f$ von $f$? (aus Term bestimmen)

$f: D_f \to \mathbb{R}$

Fragen:

- $\text{Bild}(f)$?
- ist $f$ injektiv?

$f$ ist nicht injektiv, wenn es zu einem $y \in \text{Bild}(f)$ verschiedene Lösungen $x$ gibt.

```python-exec
import plots, os
from math import e
if not "sinh.png" in os.listdir("./html"):
    plots.draw_function(f=lambda x: (e**x-e**(-x))/2, fn="./html/sinh.png", title_="sinh(x)")
print("![sinh](sinh.png)")
```

## Ungleichungen

$f(x) = g(x)$

$f(x) \leq g(x), \quad f(x) < g(x)$

$a < b \iff a \leq b \land a \neq b$

$a \leq b \iff a < b \lor a = b$

$(\forall a, b \in \mathbb{R})$

- $a \leq a$
- $a \leq b \land b \leq a \implies a = b$
- $a \leq b \land b \leq c \implies a \leq c$

$(\forall a, b, c \in \mathbb{R})$

- $\lnot a < a$
- $\lnot (a < b \land b < a)$
- $a < b \land b \land c \implies a < c$
- $a \leq b \land b < c \implies a < c$

### Wichtige Ungleichungen

#### AGM-Ungleichung

Seien $a_1, ..., a_n \in \mathbb{R}^+, n \in \mathbb{N}, n \geq 1$

Dann gilt:
$$\sqrt[n]{\prod_{i=1}^n{a_i}} \leq \frac{1}{n} \sum_{i=1}^n{a_i}$$

$\sqrt[n]{a_1 \cdot a_2 \cdot ... \cdot a_n} \leq \frac{a_1 + a_2 + ... + a_n}{n}$

#### Bernoulli-Ungleichung

$(\forall x \in \mathbb{R})(\forall n \in \mathbb{N})$

$$n \geq 1 \land x \geq -1 \implies (1+x)^n \geq 1 + nx$$

#### Caschy-Schwarz-Ungleichung

$$(\forall a_1, ..., a_n, b_1, ..., b_n \in\mathbb{R}) \quad |\sum_{i=1}^n{a_ib_i}| \leq \sqrt{\sum_{i=1}^n{a_i^2}} \cdot \sqrt{\sum_{i=1}^n{b_i^2}}$$

$f(x) \leq g(x), \quad x \in D_f \cup D_g$

$L = \{x \in D_f \cup D_g | f(x) \leq g(x) \}$

$f(x) \leq g(x), \quad t(x) \text{ sei ein Term mit } D_f \cup D_g \subseteq D_t$

$f(x) \leq g(x) \iff  f(x) + t(x) \leq g(x) + g(x)$

### Ungleichungen mit Beträgen

$|x - a| < c \iff x \in (a+c, a-c)$


$|3x+2| < |x-2|$

$\text{Fall 1: } 2 \leq x \implies x < -2$

$\text{Fall 2: } -\frac{2}{3} \leq x < 2 \implies x < - 2$

### Quadratische Ungleichungen

$x^2 + px + q < 0$

```python-exec
import plots

plots.draw_function(f=lambda x: x**2 + 3*x + -2, fn="./html/quadratische ungleichung.png")
print("![Quadratische Ungleichung](quadratische ungleichung.png)")
```

Die Lösungen befinden sich zwischen den Nullstellen, wenn die Funktion dort negative Werte annimmt.