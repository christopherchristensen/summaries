#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:46:33 2019

@author: christopher
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot


# --- 11.1
df1 = DataFrame({
    "Marke": np.repeat(["1", "2", "3", "4", "5"], 4),
    "Feuchtigkeit": np.tile(["1", "2", "3", "4"], 5),
    "Y": [685, 792, 838, 875,
          722, 806, 893, 953,
          733, 802, 880, 941,
          811, 888, 952, 1005,
          828, 920, 978, 1023]
})

# Vollständig Randomisierter Versuchsplan
fit = ols("Y ~ C(Marke, Sum) + C(Feuchtigkeit, Sum)", data=df1).fit()
anova_lm(fit)

# Mit einem F-Wert von 95.58 und P-Wert von 5.42e-09
# kann man schliessen, dass die Nullhypothese auf dem 
# Signifikanzniveau von 5% verworfen wird und somit
# signifikante Unterschiede im Energieverbrauch zwischen
# den Marken bestehen


# Vollständig randomisierter Block-Design
fit = ols("Y ~ C(Marke, Sum) + C(Feuchtigkeit, Sum)", data=df1).fit()
anova_lm(fit)

# Mit einem F-Wert von 278.20 und P-Wert von 2.36e-11
# kann man auch hier schliessen, dass die Nullhypothese
# auf dem Signifikanzniveau von 1% verworfen wird und somit
# signifikante Unterschiede zwischen den Feuchtigkeits-Blocks
# bestehen

# Ja, denn es hat einen signifikanten Einfluss auf
# die verschiedenen Energiewerte unabhängig von der
# Marken und ob sie sich gegenseitig beeinflussen

# Interaction Plot erstellen
interaction_plot(x=df1["Feuchtigkeit"], trace=df1["Marke"], response=df1["Y"])

# Man sieht im Interaction Plot deutlich, dass die
# Feuchtigkeit zu einer Wechselwirkung zwischen den
# Marken führt anhand des steigenden Energieverbrauchs
# gegen Feuchtigkeitsstufe 4. Das heisst man kann von
# der Additivität ausgehen

# Man kann die Wechselwirkung aber nicht überprüfen,
# da man zu wenig Messungen hat...

fit = ols("Y ~ C(Marke, Sum) * C(Feuchtigkeit, Sum)", data=df1).fit()
anova_lm(fit)


# --- 11.2

automob = pd.read_csv("./automob.dat", sep=" ")
df = DataFrame(automob)
sns.stripplot(x="STADT", y="KMP4L", hue="AUTO", jitter=True, data=automob)
sns.boxplot(x="STADT", y="KMP4L", hue="AUTO", data=automob)

city_means = df[df["STADT"]]

fit = ols("KMP4L ~ C(AUTO, Sum) * C(STADT, Sum)", data=df).fit()
anova_lm(fit)

# Die Nullhypothese, dass alpha (Stufe/AUTO) und beta (Blöcke/STADT)
# keine Unterschiede aufweisen, kann anhand der Alternativhypothese
# verworfen werden, da beide P-Werte im 5%-Signifikanzbereich liegen
# Auch die Wechselwirkung muss beachtet werden und dessen Nullhypothese
# kann mit 7.58e-11 verworfen werden.
df.reset_index(inplace=True)
interaction_plot(x=df["STADT"], trace=df["AUTO"], response=df["KMP4L"])

# Man sieht, dass die Städte verschiedene Einflüsse auf die 
# Autoarten haben. So hat zum Beispiel San Francisco am wenigsten
# KMP4L für das Auto 5 aber dasselbe Auto hat am meisten KM4L in LA

city_la = df[df["STADT"] == "Los Angeles"]
city_pl = df[df["STADT"] == "Portland"]
city_sf = df[df["STADT"] == "San Francisco"]

fit = ols("KMP4L ~ C(AUTO, Sum)", data=city_la).fit()
anova_lm(fit)

# Das Auto in LA hat hier einen signifikanten Unterschied
# auf dem 5%-Signifikanzniveau

fit = ols("KMP4L ~ C(AUTO, Sum)", data=city_pl).fit()
anova_lm(fit)

# Das Auto in PL hat hier einen signifikanten Unterschied
# auf dem 5%-Signifikanzniveau


fit = ols("KMP4L ~ C(AUTO, Sum)", data=city_sf).fit()
anova_lm(fit)

# Das Auto in SF hat hier einen signifikanten 
# Unterschied auf dem 5%-Signifikanzniveau



# --- 11.3
stream = pd.read_csv("./stream.dat", sep=" ")

sns.stripplot(x="ZNGROUP", y="DIVERSITY", data=stream)
sns.boxplot(x="ZNGROUP", y="DIVERSITY", data=stream)

fit = ols("DIVERSITY ~ C(ZNGROUP, Sum)", data=stream).fit()
anova_lm(fit)

fit.params

# C(ZNGROUP, Sum)[S.1]    0.091111
# C(ZNGROUP, Sum)[S.2]    0.326111
# C(ZNGROUP, Sum)[S.3]    0.011389
# C(ZNGROUP, Sum)[S.4]    0.000000

# globaler Mittelwert        1.706389
# Gruppenmittelwert [S.1]    1.797500
# Gruppenmittelwert [S.2]    2.032500
# Gruppenmittelwert [S.3]    1.717778
# Gruppenmittelwert [S.4]    1.368889 

# --> für S.4: 
# (alle anderen Abweichungen von globalem Mittelwert subtrahieren)

# Gruppe 4 scheint nicht übereinzustimmen?


fit = ols("DIVERSITY ~ C(STREAM, Sum) * C(ZNGROUP, Sum)", data=stream).fit()
anova_lm(fit)

# STREAM und ZNGROUP haben Einfluss
# Wechselwirkung nicht!
# Somit nicht additiv!

# faktorielles Experiment, da alle Gruppen als 
# Haupt-Faktoren betrachtet werden