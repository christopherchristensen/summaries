#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:41:49 2019

@author: cj
"""
import numpy as np
import seaborn as sns
from pandas import DataFrame
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
# =============================================================================
# 10.1
# =============================================================================
df = DataFrame({
    "Typ": np.repeat(["T1", "T2", "T3", "T4"], [6,6,6,6]),
    "lb": [655.5, 788.3, 734.3, 721.4, 679.1, 699.4,
           789.2, 772.5, 786.9, 686.1, 732.1, 774.8,
           737.1, 639.0, 696.3, 671.7, 717.2, 727.1,
           535.1, 628.7, 542.4, 559.0, 586.9, 520.0]
})

sns.stripplot(x="Typ", y="lb", data=df)
sns.boxplot(x="Typ", y="lb", data=df)

fit = ols("lb~Typ", data=df).fit()
anova_lm(fit)

# =============================================================================
# 10.2
# =============================================================================
df = DataFrame({
    "Behandlung": np.repeat(["A", "B", "C", "D"], [4, 6, 6, 8]),
    "KZ": [62.0, 60.0, 63.0, 59.0, 63.0, 67, 71, 64, 65, 66, 68, 66, 71, 
           67, 68, 68, 56, 62, 60, 61, 63, 64, 63, 59]
})

sns.stripplot(x="Behandlung", y="KZ", data=df)
sns.boxplot(x="Behandlung", y="KZ", data=df)

n = 24
g = 4
gm = df["KZ"].sum() / 24
ma = df.loc[df["Behandlung"] == "A"]["KZ"].sum() / 4
mb = df.loc[df["Behandlung"] == "B"]["KZ"].sum() / 6
mc = df.loc[df["Behandlung"] == "C"]["KZ"].sum() / 6
md = df.loc[df["Behandlung"] == "D"]["KZ"].sum() / 8

sa = ((df.loc[df["Behandlung"] == "A"]["KZ"] - ma)**2).sum() / 3
sb = ((df.loc[df["Behandlung"] == "B"]["KZ"] - mb)**2).sum() / 5
sc = ((df.loc[df["Behandlung"] == "C"]["KZ"] - mc)**2).sum() / 5
sd = ((df.loc[df["Behandlung"] == "D"]["KZ"] - md)**2).sum() / 7

Ea = ((df.loc[df["Behandlung"] == "A"]["KZ"] - ma)**2).sum()
Eb = ((df.loc[df["Behandlung"] == "B"]["KZ"] - mb)**2).sum()
Ec = ((df.loc[df["Behandlung"] == "C"]["KZ"] - mc)**2).sum()
Ed = ((df.loc[df["Behandlung"] == "D"]["KZ"] - md)**2).sum()

DFE = n - g
DFG = g - 1

MSE = (Ea + Eb + Ec + Ed) / DFE

G = 6 * ((ma - gm)**2 + (mb - gm)**2 + (mc - gm)**2 + (md - gm)**2)
MSG = G / DFG

fit = ols("KZ~Behandlung", data=df).fit()

anova_lm(fit)