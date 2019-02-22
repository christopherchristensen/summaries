#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:46:33 2019

@author: christopher
"""
import numpy as np
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