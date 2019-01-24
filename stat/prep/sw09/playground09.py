#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:43:40 2019

@author: christopher
"""

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import scipy.stats as st 
import numpy as np
import seaborn as sns
df = DataFrame({
        "Treatment": np.repeat(["Kommerziell", "Vakuum", "Gemischt", "CO2"], [3, 3, 3, 3]),
        "steak_id":[7.66, 6.98, 7.80, 5.26, 5.44, 5.80, 7.41, 7.33, 7.04, 3.51, 2.91, 3.66]
})


sns.stripplot(x="Treatment", y="steak_id", data=df) 
plt.xlabel("Verpackungsmethode")
plt.ylabel("Logarithmus Bakterienzahl")
plt.show()
sns.boxplot(x="Treatment", y="steak_id", data=df) 
plt.xlabel("Verpackungsmethode")
plt.ylabel("Logarithmus Bakterienzahl")
plt.show()



df.describe()
df.head()
df

fit = smf.ols(formula='steak_id~Treatment', data=df).fit()
fit.summary()
print(fit.summary())
print(fit.params)