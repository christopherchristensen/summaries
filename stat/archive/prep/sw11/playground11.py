#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 15:45:36 2019

@author: christopher
"""

from pandas import DataFrame 
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as st
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt


Daten = DataFrame({
        "Batch": np.tile(["1", "2", "3", "4", "5", "6"], 4),
        "Methode": np.repeat(["8500", "8700", "8900", "9100"], 6),
        "Y": np.array([90.3, 89.2, 98.2, 93.9, 87.4, 97.9, 92.5, 89.5, 90.6, 94.7, 87, 95.8, 85.5,
                       90.8, 89.6, 86.2, 88, 93.4, 82.5, 89.5, 85.6, 87.4, 78.9, 90.7]) 
})

interaction_plot(x=Daten["Batch"], trace=Daten["Methode"], response=Daten["Y"]) 
plt.ylabel("Daten Y")
plt.show()

fit = ols("Y ~ C(Methode, Sum) * C(Batch, Sum)", data=Daten).fit()
fit.params
anova = anova_lm(fit)


from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt

df = DataFrame({
	"Batch": np.tile(["1", "2", "3", "4", "5", "6"], 4),
	"Methode": np.repeat(["8500", "8700", "8900", "9100"], 6),
	"Y": np.array([90.3, 89.2, 98.2, 93.9, 87.4, 97.9, 92.5, 89.5, 
                    90.6, 94.7, 87, 95.8, 85.5, 90.8, 89.6, 86.2, 
                    88, 93.4, 82.5, 89.5, 85.6, 87.4, 78.9, 90.7]) 
})

interaction_plot(x=df["Batch"],trace=df["Methode"], response=df["Y"]) 
plt.ylabel("Daten Y")
plt.show()

# Benötigt, um fehlenden Parameter zu schätzen
Methodenmittelwert_9100 = df[df["Methode"] == "9100"]["Y"].mean()
Batchmittelwert_6 = df[df["Batch"] == "6"]["Y"].mean()
globalerMittelwert = df["Y"].mean()

# geschätzte Parameter von Methoden
fit = ols("Y ~ C(Methode, Sum)", data=df).fit()
fit.params

# geschätzte Parameter von Batches
fit = ols("Y ~ C(Batch, Sum)", data=df).fit()
fit.params

# geschätzte Parameter von Methoden und Batches
# auf einmal dargestellt
fit = ols("Y ~ C(Methode, Sum) + C(Batch, Sum)", data=df).fit()
fit.params

# fehlende Parameter: Abweichung Methode 9100 und Abweichung Batch 6
ab_9100 = Methodenmittelwert_9100 - globalerMittelwert
ab_6 = Batchmittelwert_6 - globalerMittelwert



# Interaktions-Plot faktorielles Experiment
fe = DataFrame({
    "Grundierung": np.repeat(["A", "B", "C"], 6),
    "Methode": np.tile(np.repeat(["Eintauchen", "Besprühen"], 3), 3),
    "Y": [4, 4.5, 4.3, 5.4, 4.9, 5.6, 5.6, 4.9, 5.4, 5.8, 6.1, 6.3, 3.8, 3.7, 4, 5.5, 5, 5]
})

fe.describe()

interaction_plot(x=fe["Grundierung"], trace=fe["Methode"], response=fe["Y"])


el = DataFrame({
    "Temperatur": np.repeat(["15°C", "25°C"], 12),
    "Konzentration": np.tile(np.repeat(["0.16", "0.8", "4", "20"], 3), 2),
    "Y": [82, 46, 16, 20, 13, 7, 20, 14, 17, 6, 7, 5, 8, 6, 5, 4, 3, 5, 10, 7, 5, 6, 4, 5]
})

el.describe()

np.array([0])


El = DataFrame({
"Konz": np.repeat(["A", "B", "C","D"], 6),
"Temp": np.tile(np.repeat(["15C", "25C"],3),4),
"Y": np.array([82, 46, 16, 20, 13, 7, 20, 14, 17, 6, 7, 5, 8, 6, 5, 4, 3, 5, 10, 7, 5, 6, 4, 5])
})

fit = ols("Y ~ C(Konz,Sum)*C(Temp,Sum)",data=El).fit() 
fit.params
