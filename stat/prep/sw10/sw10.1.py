#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:52:24 2019

@author: christopher
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pandas import DataFrame
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


# =============================================================================
# 10.1
# =============================================================================

x = DataFrame({
    "Typ": np.repeat(["1", "2", "3", "4"], 6),
    "Fest": [655.5, 788.3, 734.3, 721.4, 679.1, 699.4,
             789.2, 772.5, 786.9, 686.1, 732.1, 774.8,
             737.1, 639.0, 696.3, 671.7, 717.2, 727.1,
             535.1, 628.7, 542.4, 559.0, 586.9, 520.0]
})

sns.stripplot(x="Typ", y="Fest", data=x)
sns.boxplot(x="Typ", y="Fest", data=x)

fit = ols("Fest~Typ", data=x).fit()
fit.params

anova_lm(fit)


# =============================================================================
# 10.2
# =============================================================================

data = DataFrame({
    "Behandlung": np.repeat(["A", "B", "C", "D"], [4, 6, 6, 8]),
    "Koagulationszeit": [62, 60, 63, 59,
                         63, 67, 71, 64, 65, 66,
                         68, 66, 71, 67, 68, 68,
                         56, 62, 60, 61, 63, 64, 63, 59]
})

sns.stripplot(x="Behandlung", y="Koagulationszeit", data=data)
sns.boxplot(x="Behandlung", y="Koagulationszeit", data=data)


# Taschenrechnersimulation
GL_mean = data["Koagulationszeit"].sum() / data["Koagulationszeit"].size

# Proben der einzelnen Gruppen
data_A = data[data["Behandlung"] == "A"]["Koagulationszeit"]
data_B = data[data["Behandlung"] == "B"]["Koagulationszeit"]
data_C = data[data["Behandlung"] == "C"]["Koagulationszeit"]
data_D = data[data["Behandlung"] == "D"]["Koagulationszeit"]

A_mean  = data[data["Behandlung"] == "A"]["Koagulationszeit"].sum() / data[data["Behandlung"] == "A"]["Koagulationszeit"].size
B_mean  = data[data["Behandlung"] == "B"]["Koagulationszeit"].sum() / data[data["Behandlung"] == "B"]["Koagulationszeit"].size
C_mean  = data[data["Behandlung"] == "C"]["Koagulationszeit"].sum() / data[data["Behandlung"] == "C"]["Koagulationszeit"].size
D_mean  = data[data["Behandlung"] == "D"]["Koagulationszeit"].sum() / data[data["Behandlung"] == "D"]["Koagulationszeit"].size

A_var = ((data[data["Behandlung"] == "A"]["Koagulationszeit"] - A_mean)**2).sum() / (data[data["Behandlung"] == "A"]["Koagulationszeit"].size - 1)
B_var = ((data[data["Behandlung"] == "B"]["Koagulationszeit"] - B_mean)**2).sum() / (data[data["Behandlung"] == "B"]["Koagulationszeit"].size - 1)
C_var = ((data[data["Behandlung"] == "C"]["Koagulationszeit"] - C_mean)**2).sum() / (data[data["Behandlung"] == "C"]["Koagulationszeit"].size - 1)
D_var = ((data[data["Behandlung"] == "D"]["Koagulationszeit"] - D_mean)**2).sum() / (data[data["Behandlung"] == "D"]["Koagulationszeit"].size - 1)



var_pool = (A_var + B_var + C_var + D_var)
ms_e = var_pool / 4

ss_g = (4*(A_mean - GL_mean)**2 + 6*(B_mean - GL_mean)**2 +6*(C_mean - GL_mean)**2 +8*(D_mean - GL_mean)**2)
ms_g = ss_g / (4 - 1)


fit = ols("Koagulationszeit~Behandlung", data=data).fit()
anova_lm(fit)