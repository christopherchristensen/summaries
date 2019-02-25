#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 09:48:20 2019

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


# =============================================================================
# 11.1
# =============================================================================
df1 = DataFrame({
    "Marke": np.repeat(["1", "2", "3", "4", "5"], 4),
    "Feuchtigkeit": np.tile(["1", "2", "3", "4"], 5),
    "Y": [685, 792, 838, 875,
          722, 806, 893, 953,
          733, 802, 880, 941,
          811, 888, 952, 1005,
          828, 920, 978, 1023]
})


fit = ols("Y ~ C(Marke, Sum) + C(Feuchtigkeit, Sum)", data=df1).fit()
anova_lm(fit)

fit = ols("Y ~ C(Feuchtigkeit, Sum)", data=df1).fit()
anova_lm(fit)


interaction_plot(x=df1["Feuchtigkeit"], trace=df1["Marke"], response=df1["Y"])



# =============================================================================
# 11.2
# =============================================================================
automob = pd.read_csv("./automob.dat", sep=" ")
df = DataFrame(automob)
sns.stripplot(x="STADT", y="KMP4L", hue="AUTO", jitter=True, data=automob)
sns.boxplot(x="STADT", y="KMP4L", hue="AUTO", data=automob)

fit = ols("KMP4L ~ C(STADT,Sum)*C(AUTO,Sum)", data=automob).fit() 
anova_lm(fit)

fitLA = ols("C(STADT,Sum)~C(AUTO,Sum)", data=automob[automob["STADT"] == "Los Angeles"]).fit() 
anova_lm(fit)

fitSF = ols("KMP4L ~ C(STADT,Sum)+C(AUTO,Sum)", data=automob[automob["STADT"] == "San Francisco"]).fit() 
anova_lm(fit)

fitPL = ols("KMP4L ~ C(STADT,Sum)+C(AUTO,Sum)", data=automob[automob["STADT"] == "Portland"]).fit() 
anova_lm(fit)


fitPL = ols("KMP4L ~ C(STADT,Sum)*C(AUTO,Sum)", data=automob[automob["STADT"] != "Portland"]).fit() 
anova_lm(fit)