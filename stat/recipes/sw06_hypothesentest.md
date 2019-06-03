# Hypothesentest

## Erläuterung
- Verfahren, um zu entscheiden, ob Mittelwert einer Messreihe zu einem bestimmten "wahren" Mittelwert $\mu$ passt oder nicht
- Erwartungswert gegeben (Nullhypothese)
- Standardabweichung gegeben oder auch nicht!
- kann zeigen, dass gegebener Mittelwert mit grosser Wahrscheinlichkeit nicht zur gegebenen Messreihe passt (kein Beweis)

## Vorgehen: Standardabweichung bekannt, normalverteilt, 1 Messreihe
1. Welche Annahmen sind gegeben?
    - Erwartungswert $\mu$ gegeben = Nullhypothese
    - Standardabweichung gegeben (muss nicht geschätzt werden)
    - Normalverteilt
2. Model bestimmen
    - Normalfall: $x_1, x_2, ..., x_n$ i.i.d $\mathcal{N}(\mu, \sigma^2)$
3. Nullhypothese
    - $H_0: \mu = \mu_0$
4. Alternativhypothese (mehrere Möglichkeiten)
    - Option 1: $H_A: \mu_A \neq \mu_0$ (zweiseitiger Test)
    - Option 2: $H_A: \mu_A < \mu_0$ (einseitiger Test nach unten)
    - Option 3: $H_A: \mu_A > \mu_0$ (einseitiger Test nach oben)
5. Teststatistik
    - Verteilung der Teststatistik T unter der Nullhypothese $H_0$
    - z.B. $T: \overline{X}_6 \sim \mathcal{N}\left(80, \frac{0.02^2}{6}\right)$
6. Signifikanzbereich
    - Meistens gegeben
    - Wenn nicht, dann $5\%$ nehmen
7. Verwerfungsbereich
    - Zweiseitiger Test: `st.norm.interval(alpha=0.95, loc=Nullhypothese, scale=sigma/np.sqrt(Grösse der Messreihe))`
    - Einseitiger Test (nach unten): `value = st.norm.ppf(q=0.05, loc=Nullhypothese, scale=sigma/np.sqrt(Grösse der Messreihe))` $\to$ $(-\infty, value]$
    - Einseitiger Test (nach oben): `value = st.norm.ppf(q=0.95, loc=Nullhypothese, scale=sigma/np.sqrt(Grösse der Messreihe))` $\to$ $[value, \infty)$
