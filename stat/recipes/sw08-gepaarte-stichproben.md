# Gepaarte und Ungepaarte Stichproben

## Gepaarte Stichproben
- Pro Versuchseinheit zwei Beobachtungen
- Beide Beobachtungen *nicht* unabhängig
- Beispiele
    - Jeden Prüfkörper mit beiden Messgeräten messen (an gleicher Versuchseinheit zweimal gemessen)
    - Ein Auge behandelt, das andere nicht

## Ungepaarte Stichproben
- Beobachtungen sind unabhängig (keine Verbindung)
- Beispiele
    - Stichprobe von Herstellungsverfahren A mit Stichprobe von Verfahren B vergleichen

## Unterscheidung gepaart oder ungepaart
- gepaart
    - jede Beobachtung kann eindeutig einer Beobachtung der anderen Gruppe zugeordnet werden
    - Stichprobengrösse in beiden Gruppen gleich
- ungepaart
    - keine Zuordnung von Beobachtungen möglich
    - Stichprobengrössen können verschieden sein
    - eine Gruppe vergrösserbar ohne andere Gruppe

## Vorgehen: Normalverteilt
- Gepaarte Stichproben
    1. `data1 = Series([25, 27, 44, 30, 67, 53, 53, 52, 60, 28])`
    2. `data2 = Series([29, 37, 56, 46, 82, 57, 80, 61, 59, 43])`
    3. `st.ttest_rel(data2, data1)`
- Ungepaarte Stichproben
    1. `data1 = Series([25, 27, 44, 30, 67, 53, 53, 52, 60, 28])`
    2. `data2 = Series([29, 37, 56, 46, 82, 57, 80, 61, 59, 43])`
    3. `st.ttest_ind(data1, data2, equal_var=False)`
- Falls gepaart und nach Vertrauensintervall gefragt
    1. `dif = data1 - data2`
    2. `t.interval(alpha=.95, df=dif.size-1, loc=dif.mean(), scale=dif.std/np.sqrt(dif.size))`
    3. TODO einseitig / zweiseitig? 
- Fall gepaart aber Differenz gegeben
    1. TODO
    2. 

## Vorgehen: Nicht-Normalverteilt
- Gepaarte Stichproben
    1. `data1 = Series([25, 27, 44, 30, 67, 53, 53, 52, 60, 28])`
    2. `data2 = Series([29, 37, 56, 46, 82, 57, 80, 61, 59, 43])`
    3. TODO: Wilcoxon aus Differenz?
- Ungepaarte Stichproben
    1. `data1 = Series([25, 27, 44, 30, 67, 53, 53, 52, 60, 28])`
    2. `data2 = Series([29, 37, 6, 46, 82, 57, 80, 61, 59, 43])`
    3. `st.mannwhitneyu(data1, data2)`
