# Vorzeichentest

## Erläuterung

- Wenn man annimmt, dass die Daten **nicht** normalverteilt sind.
- $\mu$ wird als Median genommen, somit $P(X \leq \mu) = 0.5$
- Vorteil: Keine Annahme an Verteilung
- Nachteil: Kleinere Macht

## Vorgehen

1. Eine Nullhypothese gegeben, z.B. $H_0: \mu_0 = 10$
2. $n =$ Anzahl Beobachtungen
3. $x =$ Anzahl Beobachtungen über der Nullhypothese
4. $p = 0.5$
5. Vorzeichentest durchführen
    * Zweiseitig: `st.binom_test(x=x, n=n, p=0.5)`
    * Kleiner als: `st.binom_test(x=x, n=n, p=0.5, alternative="less")`
    * Grösser als: `st.binom_test(x=x, n=n, p=0.5, alternative="greater")`







