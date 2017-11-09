# Relationale Algebra

**Kreuzprodukt A x B**: Menge aller Tupel (a,b), wobei das erste Element des Tupels aus A und das zweite aus B stammt, d.h. $A \times B = {(a,b) | a \in A \wedge b \in B}$

**Binäre Relation** (R) = Teilmenge des Kreuzproduktes $A \times B$ 

Unterschiede zwischen binären Relationen und Funktionen:

* Funktion von A nach einer Menge B ordnet jedem x $\in$ A genau ein Element $y = f(x) \in B$
* Jede Funktion $f:A \to B$ ist auch eine Relation von A nach B; nämlich $R_f = {(x,y) | x \in A \wedge y = f(x) \in B}$
* Die Relation $R_f$ einer Funktion $f$ ist nichts anderes als deren Graph $G(f) = R_f$
* Nicht jede Relation ist eine Funktion, weil zu einem best. $x$ mehrere $y$ gehören können
* Der Relationsbegriff ist somit eine Verallgemeinerung des Funktionsbegriffs

## Eigenschaften von Relationen
> Relation $R$ auf $A$ heisst **reflexiv**, falls $\forall x, y \in A ((x,x) \in R)$
> Relation $R$ auf $A$ heisst **reflexiv**, falls $\forall x, y \in A ((x,y) \in R \to (y,x) \in R)$
> Relation R auf A heisst **transitiv**, falls $\forall x, y, z \in A ((x,y) \in R \wedge (y,z) \in R \to (x,z) \in R)$

**Kombinationen von Relationen**: Da Relationen $R_1$ und $R_2$ von $A$ nach $B$ beides Teilmengen von $A \times B$ sind, ist die Vereinigung $R_1 \cup R_2$, der Durchschnitt $R_1 \cap R_2$ und die Differenzen $R_1 | R_2 R_2 | R_1$, sowie das Komplement $\overline{R_1}$ bezüglich $A \times B$ wohl definiert.

**Zusammensetzung von Relationen**: Ist $R$ eine Relation von der Menge $A$ in die Menge $B$ und ist $S$ eine Relation von $B$ nach $C$; dann ist die Zusammensetzung von $R$ und $S$ die Relation $$S \circ R = {(a,c) \in A \times C | \exists b \in B ((a, b) \in R \wedge (b,c) \in S)}$$

**Potenz einer Relation**: $R^n, n = 1,2,3 ...$ einer Relation $R$ in $A$ werden rekursiv wie folgt definiert: $R^1 = R$ und $R^{n-1} \circ R$

**Transitive Relation** (optional): Eine Relation $R$ ist genau dann transitiv, fall $\forall n \in \mathbb{N}^+ (R^n \subset R)$

## Darstellung von Relationen durch Matrizen
> Ist $R$ eine Relation von $A = {a_1, a_2, ... a_m}$ nach $B = {b_1, b_2, ..., b_n}$, dann stellt die Matrix $M_R = [m_{ij}]$ mit $$m_{ij} =
  \begin{cases}
    1,       & \quad \text{falls } (a_i, b_j) \in R n \\
    0,  & \quad \text{falls } (a_i, b_j) \notin R  \end{cases}
$$

[Hier fehlt Text von Folie 23/39]

**Digraph einer Relation** (optional): [...]

## Äquivalenzrelationen und -klassen
> Eine Relation $R$ auf einer Menge $A$ heisst **Äquivalenzrelation** falls sie reflexiv, symmetrisch und transitiv ist.

> Ist $R$ eine Äquivalenzrelation auf $A$, dann nennt man die Menge aller Elemente $x \in A$, äquivalent zu einem Element $a \in A$ sind, die **Äquivalenzklasse** von $A$ und schreibt dafür $[a]_R$, kurz $[a]$. Es gilt also $[a]_R = {x | (a,x) \in R}$. Irgend ein $b \in [a]_R$ heisst **Repräsentant** von $[a]_R$

Die Äquivalenzklassen einer Äquivalenzrelation $R$ auf der Menge $A$ liefern eine **Partitionierung** von $A$ und umgekehrt gibt es zu einer Partitionierung von $A$