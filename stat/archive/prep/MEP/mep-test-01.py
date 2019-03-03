#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 09:16:52 2019

@author: christopher
"""

import matplotlib.pyplot as plt
import scipy.stats as st
import seaborn as sns
import pandas as pd
import numpy as np
import warnings


from statsmodels.graphics.factorplots import interaction_plot
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from patsy.contrasts import Sum
from pandas import Series, DataFrame

from statsmodels.tsa.seasonal import seasonal_decompose


# --- A2
sr = pd.read_table(r"Schiedsrichter_Lebenserwartung.txt", delim_whitespace=True)
sr.describe()
sr_tot = sr.loc[sr["0"]==0]
sr_tot = sr_tot["70"] - sr_tot["63"]
sr_leb = sr.loc[sr["0"]==1]

sr_tot.size
sr_tot.describe()

sr_tot

sr_tot.size

sr_VB = st.t.ppf(q=0.01, df=sr_tot.size-1, loc=sr_tot.mean(), scale=sr_tot.std()/np.sqrt(sr_tot.size))

sr_tot.mean()

sr_wilcox = st.wilcoxon(sr_tot, correction=True)

sr_leb.describe()

sr_leb_SF = sr_leb["63"].mean()/np.sqrt(sr_leb["63"].size)

st.t.interval(alpha=0.99, df=194, loc=sr_tot.mean(), scale=sr_tot.std()/np.sqrt(195))


# --- A3

warnings.filterwarnings("ignore")

df = DataFrame({
    "Person": np.repeat(["P1", "P2", "P3", "P4", "P5"], 3),
    "Wein": np.tile(["W1", "W2", "W3"], 5),
    "Y": np.array([1,7,5,0,4,0,1,6,4,1,5,2,1,8,10])
})

fit = ols("Y ~C(Person, Sum) + C(Wein, Sum)", data=df).fit()
fit.summary()

anova_lm(fit)

interaction_plot(x=df["Person"], trace=df["Wein"], response=df["Y"])

