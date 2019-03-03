#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:47:49 2019

@author: christopher
"""

from pandas import DataFrame 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import scipy.stats as st
import statsmodels.formula.api as smf
import statsmodels.stats.anova as anova


# --- 10.1

df=DataFrame({
        "Typ": np.repeat(["T1", "T2", "T3", "T4"], [6, 6, 6, 6]), 
        "Druckfestigkeit" : [655.5, 788.3, 734.3, 721.4, 679.1, 699.4, 789.2, 772.5, 786.9, 686.1, 732.1, 774.8,
                             737.1, 639.0, 696.3, 671.7, 717.2, 727.1, 535.1, 628.7, 542.4, 559.0, 586.9, 520.0]
})


sns.stripplot(x="Typ", y="Druckfestigkeit", data=df) 
plt.xlabel("Typ")
plt.ylabel("Druckfestigkeit")
plt.show()

sns.boxplot(x="Typ", y="Druckfestigkeit", data=df) 
plt.xlabel("Typ")
plt.ylabel("Druckfestigkeit")
plt.show()

fit = smf.ols("Druckfestigkeit~Typ", data=df).fit()

fit.summary()
fit.params

filtered = df[df["Typ"] == "T2"]

filtered.mean()

values = anova.anova_lm(fit)



# --- 10.2


df=DataFrame({
"Behandlung": np.repeat(["A", "B", "C", "D"], [4, 6, 6, 8]), 
"Koagulationszeit" : [62, 60, 63, 59, 63, 67, 71, 64, 65, 66, 68, 66, 71, 67, 68, 68, 56, 62, 60, 61, 63, 64, 63, 59]
})

sns.stripplot(x="Behandlung", y="Koagulationszeit", data=df) 
plt.xlabel("Behandlung")
plt.ylabel("Koagulationszeit")
plt.show()

sns.boxplot(x="Behandlung", y="Koagulationszeit", data=df) 
plt.xlabel("Behandlung")
plt.ylabel("Koagulationszeit")
plt.show()


df.mean()


fit = smf.ols("Koagulationszeit~Behandlung", data=df).fit()
fit.summary()
fit.params

anova.anova_lm(fit)