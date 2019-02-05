#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:34:10 2019

@author: christopher
"""

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
x = np.array([24.4, 27.6, 27.8, 27.9, 28.5, 30.1, 30.1, 30.3, 31.7, 32.2, 32.8, 33.3, 33.5, 34.1, 34.6, 35.8, 35.9, 36.8, 37.1, 39.2, 39.7])


st.probplot(x, plot=plt)
plt.ylabel("Empirische Quantile")
plt.xlabel("Theoretische Quantile")
plt.show()



from pandas import DataFrame 
import scipy.stats as st 
import numpy as np
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

df = DataFrame({
    "Treatment": np.repeat(["Kommerziell", "Vakuum", "Gemischt", "CO2"], [3, 3, 3, 3]), 
    "steak_id":[7.66, 6.98, 7.80, 5.26, 5.44, 5.80, 7.41, 7.33, 7.04, 3.51, 2.91, 3.66] 
})

sns.stripplot(x=["Treatment"], y=["steak_id"], data=df)

fit = ols("steak_id~Treatment",data=df).fit()

fit.summary()
print(fit.summary())
print(fit.params)
anova_lm(fit)

sns.stripplot(x=["Treatment"], y=["steak_id"], data=df)
