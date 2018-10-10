# Projektive Geometrie



## Vektorgesetze / Rechenregeln

Hier sind nur jene Vektorgesetze und Rechenregeln, die während dem Unterricht behandelt wurden, aufgelistet. Diese Liste ist deswegen nicht vollständig.



### Addition / Subtraktion

> Addition und Subtraktion zweier Vektoren.

$ \vec{a} + \vec{b} = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} + \begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} a_1 + b_2 \\ a_2 + b_2 \end{bmatrix}$

$ \vec{a} - \vec{b} = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} + \left( - \begin{bmatrix} b_1 \\ b_2 \end{bmatrix} \right)= \begin{bmatrix} a_1 - b_2 \\ a_2 - b_2 \end{bmatrix}$



### Multiplikation / Division

> Multiplikation und Division mit einer skalaren Zahl.

$\displaystyle \lambda \vec{a} = \lambda \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} = \begin{bmatrix} \lambda a_1 \\ \lambda a_2 \end{bmatrix}$

$\displaystyle \frac{1}{\lambda} \vec{a} = \frac{1}{\lambda} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} = \begin{bmatrix} \frac{1}{\lambda} a_1 \\ \frac{1}{\lambda} a_2 \end{bmatrix}$



### Inverses

> Das Inverse eines Vektors zeigt in die andere Richtung.

$- \vec{a} = - \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} = \begin{bmatrix} - a_1 \\ -a_2 \end{bmatrix}$



### Nullvektor

> Ein Vektor dessen Komponenten alle verschwinden.

$\vec{0} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$



### Orthogonale Vektoren

> Das Skalarprodukt zweier Vektoren ergibt null, wenn sie senkrecht aufeinander stehen.

$$\vec{a} \bullet \vec{b} = 0 \iff \vec{a} \perp \vec{b}$$



### Betrag

> Der Betrag eines Vektors berechnet sich aus der Wurzel der Summe der quadrierten Koordinaten.

$a \equiv | \overrightarrow{a} | = \sqrt{\overrightarrow{a} \bullet \overrightarrow{a}} = \sqrt{a_1^2 + a_2^2 + ... + a_n^2}$

$| \lambda \overrightarrow{a} = |\lambda | |\overrightarrow{b} |$



### Kommutativgesetz

> Vektoren können bei Addition und Subtraktion beliebig vertauscht werden, solange sie ihr Vorzeichen behalten.

$\overrightarrow{a} + \overrightarrow{b} = \overrightarrow{b} + \overrightarrow{a}$



### Assoziativgesetz

> Bei Addition und Subtraktion kommt es nicht auf die Reihenfolge in der die Vektoren zusammengerechnet werden, solange sie ihr Vorzeichen behalten.

$\overrightarrow{a} + ( \overrightarrow{b} + \overrightarrow{c} )= ( \overrightarrow{a} + \overrightarrow{b} )+ \overrightarrow{c}$



### Existenz eines Neutralelements $\overrightarrow{0}$

> Das Dasein eines Nullvektors hat keinen Einfluss auf andere Vektoren

$\overrightarrow{a} + \overrightarrow{0} = \overrightarrow{a}$



### Existenz des Inversen

> Das Inverse eines Vektors zeigt immer in entgegengesetzte Richtung.

$\overrightarrow{a} + (-\overrightarrow{a}) = \overrightarrow{0}$



### Skalarprodukt

> Allgemein ist das Skalarprodukt wie folgt definiert.

$\overrightarrow{a} \bullet \overrightarrow{b} = | \overrightarrow{a} | \cdot | \overrightarrow{b} | \cdot cos \phi$



> Im kartesischen Koordinatensystem kann man das Skalarprodukt auch so berechnen.

$\displaystyle \overrightarrow{a} \bullet \overrightarrow{b} = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} \bullet \begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = a_1 b_2 + a_2 b_2$



> In einem Koordinatensystem, welches nicht kartesisch ist (in einem beliebigen, nicht notwendiger Weise rechtwinkligen Koordinatensystem im $\R^3$), berechnet man das Skalarprodukt wie folgt. Die Matrix $G$ wird auch **metrischer Tensor** genannt.

$\displaystyle \overrightarrow{a} \bullet \overrightarrow{b} = \sum_{i = 1}^{3} \sum_{j=1}^{3}{g_{ij} a_i b_j} = (a_1 \ \ a_2 \ \ a_3) \begin{pmatrix} g_{11} \ g_{12} \ g_{13} \\ g_{21} \ g_{22} \ g_{23} \\ g_{31} \ g_{32} \ g_{33} \end{pmatrix} \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = a^T Gb<span style="caret-color: rgb(132, 33, 162); color: rgb(132, 33, 162); display: inline"></span><span style="caret-color: rgb(132, 33, 162); color: rgb(132, 33, 162); display: inline"></span><span style="caret-color: rgb(132, 33, 162); color: rgb(132, 33, 162); display: inline"></span><span style="caret-color: rgb(132, 33, 162); color: rgb(132, 33, 162); display: inline"></span>$



### Rechenregeln Skalarprodukt

> Für beliebige reelle Zahlen sowie beliebige Vektoren $\overrightarrow{a}$ , $\overrightarrow{b}$  und $\overrightarrow{c}$ gilt folgendes.



> Kommutativgesetz

$\overrightarrow{a} \bullet \overrightarrow{b} = \overrightarrow{b} \bullet \overrightarrow{a}$



> Distributivgesetz

$\overrightarrow{a} \bullet \left( \overrightarrow{b} + \overrightarrow{c} \right) = \overrightarrow{a} \bullet \overrightarrow{b} + \overrightarrow{a} \bullet \overrightarrow{c}$



> Andere

$\lambda \left( \overrightarrow{a} \bullet \overrightarrow{b} \right) = (\lambda \overrightarrow{a} ) \bullet \overrightarrow{b} = \overrightarrow{a} \bullet (\lambda \overrightarrow{b})$



### Linearkombination zweier Vektoren

> Wenn aus einer Kombination von Vektor  $\overrightarrow{a}$  und Vektor  $\overrightarrow{b}$   ein Vektor  $\overrightarrow{c}$  entsteht, dann ist der Vektor  $\overrightarrow{c}$  eine Linearkombination dieser zwei Vektoren und somit linear abhängig von ihnen.

$\overrightarrow{c} = \lambda \overrightarrow{a} + \mu \overrightarrow{b}$ 



### Lineare Unabhängigkeit

> Man nennt n Vektoren $a_1$ , $a_2$ , $...$ , $a_n$  linear unabhängig, falls folgendes gilt.
>
> 1. Keine Kombination ergibt den Nullvektor $\overrightarrow{0}$ , ausser
> 2. mit der trivialen Lösung, worin alle $\lambda$  null sind 

$\lambda_1 \overrightarrow{a}_1 + \lambda_2 \overrightarrow{a}_2 + ... + \lambda_n \overrightarrow{a}_n = \overrightarrow{0}$



### Einheitsvektor eines bestimmten Vektors

> Den Einheitsvektor eines bestimmten Vektors kann man aus der Division des Vektors durch seinen Betrag berechnen.

$\displaystyle e_a = \frac{\overrightarrow{a}}{| \overrightarrow{a} |} $



### Beschreibung von Geraden (2D/3D)

> **Punkt-Punktform** mit Vektoren.  $r_0$  und  $r_1$  sind hier zwei Punkte auf der Geraden.

$\overrightarrow{r} = \overrightarrow{r}_0 + t (\overrightarrow{r}_1 - \overrightarrow{r}_0)$



> **Punkt-Richtungsform** mit Vektoren.  $r_0$  ist hier ein Punkt auf der Geraden und  $\overrightarrow{r}_1$  ist der Richtungsvektor.

$\overrightarrow{r} = \overrightarrow{r}_0 + t \overrightarrow{r}_1$



> **Achsenabschnitt-Steigungsform** (nur 2D)

$y = mx + q$



> **Punkt-Richtungsform** (nur 2D). Hier ist  $(x_0, y_0)$  ein Punkt auf der Geraden und  $m$  die Steigung.

$(y-y_0) = m(x - x_0)$



> **Allgemeine Geradengleichung** (nur 2D).

$ax + by + c = 0$



### Weitere Gesetze

> Allgemeine Vektorgesetze

* $\displaystyle \lambda \left( \overrightarrow{a} + \overrightarrow{b} \right) = \lambda \overrightarrow{a} + \lambda \overrightarrow{b}$
* $\displaystyle \left( \lambda + \mu \right) \overrightarrow{a} = \lambda \overrightarrow{a} + \mu \overrightarrow{a}$

* $\displaystyle (\lambda \mu) \overrightarrow{a} = \lambda (\mu \overrightarrow{a}) = \mu (\lambda \overrightarrow{a})$
* $\displaystyle 1\overrightarrow{a} = \overrightarrow{a}$



> Im kartesischen Koordinatensystem (oder einfach wenn die Basisvektoren orthogonal zueinander stehen und auf die Länge $1$ normiert sind).

* $\displaystyle \overrightarrow{a}  = a_x \overrightarrow{e}_x + a_y \overrightarrow{e}_y = \begin{bmatrix} a_x \\ a_y \end{bmatrix}$



## Was ist ein Rechtssystem?

* Ein Koordinatensystem wobei,
  * $\overrightarrow{e_z}$ in Richtung des Daumens,
  * $\overrightarrow{e_z}$ in Richtung des Zeigefingers,
  * $\overrightarrow{e_y}$ in Richtung des Mittelfingers
  * der **rechten Hand** zeigt
* Die Basisvektoren ($\overrightarrow{e_z}$, $\overrightarrow{e_z}$ und $\overrightarrow{e_y}$) stehen orthogonal aufeinander und haben die Länge $1$.
* $\overrightarrow{a} = a_x \overrightarrow{e_x} + a_y \overrightarrow{e_y} = \begin{bmatrix} a_x \\ a_y \end{bmatrix}$







