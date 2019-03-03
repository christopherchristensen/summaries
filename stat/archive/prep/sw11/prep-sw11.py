#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:13:30 2019

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
from patsy.contrasts import Sum


# --- 11.1

df=DataFrame({
    "Luftfeuchtigkeitsniveau" : np.tile(["1", "2", "3", "4"], 5),
    "Marke": np.repeat(["1", "2", "3", "4", "5"], 4),
    "Energieverbrauch" : np.array([685, 792, 838 , 875, 722, 806, 893, 953, 733, 802, 880, 941, 811, 888, 952, 1005, 828, 920, 978, 1023]) 
})

fit = ols("Energieverbrauch ~ C(Marke, Sum) + C(Luftfeuchtigkeitsniveau, Sum)", data=df).fit()
anova_lm(fit)


interaction_plot(x=df["Luftfeuchtigkeitsniveau"], trace=df["Marke"], response=df["Energieverbrauch"])


# --- 11.2

automob = pd.read_csv("automob.dat", sep=" ")
df = DataFrame(automob)
sns.stripplot(x="STADT", y="KMP4L", hue="AUTO", jitter=True, data=automob)

fit = ols("KMP4L ~ C(STADT,Sum)*C(AUTO,Sum)", data=automob).fit() 
anova_lm(fit)

df

df.reset_index(inplace = True)
interaction_plot(x = df["STADT"], trace = df["AUTO"], response = df["KMP4L"])


fitLA = ols("KMP4L ~ C(STADT,Sum)*C(AUTO,Sum)", data=df[df["STADT"]=="Los Angeles"]).fit()
fitPL = ols("KMP4L ~ C(STADT,Sum)*C(AUTO,Sum)", data=df[df["STADT"]=="Portland"]).fit()
fitSF = ols("KMP4L ~ C(STADT,Sum)*C(AUTO,Sum)", data=df[df["STADT"]=="San Francisco"]).fit()

anova_lm(fitLA)
anova_lm(fitPL)
anova_lm(fitSF)

fitNSF = ols("KMP4L ~ C(STADT,Sum)*C(AUTO,Sum)", data=df[df["STADT"]!="San Francisco"]).fit()
anova_lm(fitNSF)


# --- 11.3
stream = pd.read_csv("stream.dat", sep=" ")
stream

sns.boxplot(x="ZNGROUP", y="DIVERSITY", data=stream)
sns.stripplot(x="ZNGROUP", y="DIVERSITY", data=stream)

fitDZ = ols("DIVERSITY ~ C(ZNGROUP, Sum) * C(STREAM, Sum)", data=stream).fit()
anova_lm(fitDZ)


fitDZ2 = ols("DIVERSITY ~ C(ZNGROUP, Sum)", data=stream).fit()
fitDZ2.summary()

anova_lm(fitDZ2)

fitDZ2.params