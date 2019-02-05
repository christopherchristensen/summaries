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