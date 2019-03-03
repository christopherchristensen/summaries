#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 21:25:46 2019

@author: christopher
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pandas import DataFrame
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


# --- 10.1
df = DataFrame({
    "Typ": np.repeat(["1", "2", "3", "4"], 6),
    "Druckfestigkeit": [655.5, 788.3, 734.3, 721.4, 679.1, 699.4,
                        789.2, 772.5, 786.9, 686.1, 732.1, 774.8,
                        737.1, 639.0, 696.3, 671.7, 717.2, 727.1,
                        535.1, 628.7, 542.4, 559.0, 586.9, 520.0]
})


plt.subplot(221)
sns.stripplot(x="Typ", y="Druckfestigkeit", data=df).plot()
plt.title("Stripplot Druckfestigkeit pro Typ")

plt.subplot(222)
sns.boxplot(x="Typ", y="Druckfestigkeit", data=df).plot()
plt.title("Boxplot Druckfestigkeit pro Typ")

plt.tight_layout()
plt.show()


fit = ols("Druckfestigkeit~Typ", data=df).fit()
fit.summary()
fit.params

# Typ 1 = 713.0000
# Typ 2 = 756.9333
# Typ 3 = 698.0667
# Typ 4 = 562.0167

pred = fit.get_prediction()
pred.conf_int()

anova_lm(fit)



# --- 10.2
data = DataFrame({
    "Behandlung": np.repeat(["A", "B", "C", "D"], [4, 6, 6, 8]),
    "Koagulationszeit": [62, 60, 63, 59,
                         63, 67, 71, 64, 65, 66,
                         68, 66, 71, 67, 68, 68,
                         56, 62, 60, 61, 63, 64, 63, 59]
})

# data.set_index("Behandlung", inplace=True)

sns.stripplot(x="Behandlung", y="Koagulationszeit", data=data).plot()
sns.boxplot(x="Behandlung", y="Koagulationszeit", data=data).plot()

# globale Parameter
data_size = data["Koagulationszeit"].size
data_sum = data["Koagulationszeit"].sum()
data_mean = data["Koagulationszeit"].sum() / data["Koagulationszeit"].size 

# Proben der einzelnen Gruppen
data_A = data[data["Behandlung"] == "A"]["Koagulationszeit"]
data_B = data[data["Behandlung"] == "B"]["Koagulationszeit"]
data_C = data[data["Behandlung"] == "C"]["Koagulationszeit"]
data_D = data[data["Behandlung"] == "D"]["Koagulationszeit"]

# Gruppenmittelwerte
mean_A = (62 + 60 + 63 + 59) / 4
mean_B = (63 + 67 + 71 + 64 + 65 + 66) / 6
mean_C = (68 + 66 + 71 + 67 + 68 + 68) / 6
mean_D = (56 + 62 + 60 + 61 + 63 + 64 + 63 + 59) / 8

# empirische Gruppenvarianzen
egv_A = ((62 - mean_A)**2 + (60 - mean_A)**2 + (63 - mean_A)**2 + (59 - mean_A)**2) / 3
egv_B = ((data_B - data_B.mean())**2).sum() / (data_B.size - 1)       
egv_C = ((data_C - data_C.mean())**2).sum() / (data_C.size - 1)
egv_D = ((data_D - data_D.mean())**2).sum() / (data_D.size - 1)

# Gruppenresiduen
res_A = ((62 - mean_A)**2 + (60 - mean_A)**2 + (63 - mean_A)**2 + (59 - mean_A)**2)
res_B = ((63 - mean_B)**2 + (67 - mean_B)**2 + (71 - mean_B)**2 + (64 - mean_B)**2 + (65 - mean_B)**2 + (66 - mean_B)**2)
res_C = ((data_C - data_C.mean())**2).sum()
res_D = ((data_D - data_D.mean())**2).sum()

# SSE und SSG
sse = res_A + res_B + res_C + res_D
ssg = ((mean_A - data_mean)**2) * 4 + ((mean_B - data_mean)**2) * 6 + ((mean_C - data_mean)**2) * 6 + ((mean_D - data_mean)**2) * 8

# MSE und MSG
mse = sse / (24-4) 
msg = ssg / (4-1)

# F
F = msg / mse

# ANOVA
fit = ols("Koagulationszeit~Behandlung", data=data).fit()
fit.params
anova_lm(fit)