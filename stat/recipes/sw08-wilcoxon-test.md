# Wilcoxon-Test

## Erläuterung
- Kompromiss zwischen Vorzeichen- und t-Test
- Annahme
    - Verteilung ist symmetrisch
    - i.i.d.
- min. 6 Beobachtungen
- Macht 79%
- Wilcoxon meistens t- oder Vorzeichen-Test vorzuziehen
    - hat oft grössere Macht
    - selbst in ungünstigen Fällen nie viel schlechter
    - Wenn man t-Test trotzdem verwendet, immer graphisch überprüfen, grobe Abweichung von Normalverteilung (vorallem Normal-Plot)

## Vorgehen
- zweiseitig
    1. `st.wilcoxon(data-nullhypothese, correction=True)`
- einseitig
    1. `pWert1 = st.wilcoxon(data-nullhypothese, correction=True)`
    2. `pWert = 1 - (pWert1 / 2)`
- TODO: Überprüfen nach Richtigkeit (S08.2). Stimmt das auch wenn nach oben einseitig?


