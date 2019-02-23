#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 11:29:13 2019

@author: christopher
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

# --- 1.1
d1 = pd.read_csv("./child.csv", sep=",", index_col=0)
d1.shape
d1.describe()
"Netherlands" in d1.index
"China" in d1.index
d1.columns
d1.sort_values(by="Drunkenness", ascending=False)["Drunkenness"].head()
d1.nsmallest(5, "Infant.mortality")["Infant.mortality"]

d1.loc[d1["Physical.activity"] < d1["Physical.activity"].mean(), :]["Physical.activity"]



# --- 1.2
d2 = pd.read_csv("./d.fuel.dat", index_col=0)
d2.describe()
d2.loc[1] # 2560, 33, Small
d2.loc[:5] # 2440, 32, Small
d2.head()
d2["mpg"].mean() # 24.5833333
d2["mpg"].loc[7:22].mean() # 27.75

t_kml = d2["mpg"] * 0.43
t_kg = d2["weight"] * 0.45359

t_kml.mean() # 10.5708
t_kg.mean() # 1315.7890



# --- 1.3
d3 = DataFrame([2.1,2.4,2.8,3.1,4.2,4.9,5.1,6.0,6.4,7.3,10.8,12.5,13.0,13.7,
                14.8,17.6,19.6, 23.0,25.0,35.2,39.6])[0]

d3.describe()
d3.sum()      # 269.1
(d3**2).sum() # 5729.27

middle_index  = np.round(d3.size/2 + 0.5) - 1
sorted_values = d3.sort_values(ascending=True)

d3_mean       = (d3.sum() / d3.size)
d3_std        = np.sqrt(((d3 - d3_mean)**2).sum() / (d3.size - 1))
d3_median     = d3[middle_index]

d3.mean()
d3.median()
d3.std()
d3.quantile(q=[.25, .75])

z = (d3 - d3.mean()) / d3.std()
z.mean()    # -2.114710523095536e-17 (beinahe 0)
z.std()     # 1.0



# --- 1.4
# 1b
# 2c
# 3a



# --- 1.5
d4 = pd.read_csv("./geysir.dat", sep=" ", index_col=0)
d4.describe()

plt.subplot(221)
d4["Zeitspanne"].plot(kind="hist", bins=np.arange(0, 100, 2), edgecolor="black")

plt.subplot(222)
d4["Zeitspanne"].plot(kind="hist", bins=np.arange(0, 100, 10), edgecolor="black")

plt.tight_layout()
plt.show()


d4["Eruptionsdauer"].plot(kind="hist", normed=True, cumulative=True)

# 0.2 (20%)
# 3.7 min
 