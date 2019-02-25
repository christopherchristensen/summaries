#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:26:32 2019

@author: christopher
"""

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
from pandas import DataFrame

pw_electric = pd.read_csv('./PW_electric.csv', sep=',', skiprows=2, header=0,
encoding = "utf-8", index_col=0)
pw_electric.head()
pw_electric_luzern = DataFrame(pw_electric.ix["Luzern",1:]) 
pw_electric_luzern
pw_electric_luzern["Year"] = pd.DatetimeIndex(pw_electric_luzern.index)


pw_electric_luzern.set_index("Year", inplace=True) 
pw_electric_luzern.plot()
plt.xlabel("Jahr")
plt.ylabel("Anzahl Elektro-Autos Luzern") 

pw_electric_zürich = DataFrame(pw_electric.ix["Zürich",1:]) 
pw_electric_zürich
pw_electric_zürich["Year"] = pd.DatetimeIndex(pw_electric_zürich.index)


pw_electric_zürich.set_index("Year", inplace=True) 
pw_electric_zürich.plot()
plt.xlabel("Jahr")
plt.ylabel("Anzahl Elektro-Autos Zürich") 
plt.show()

np.log(pw_electric_luzern.astype("float")).plot()
np.log(pw_electric_zürich.astype("float")).plot()
plt.show()

luz_log = np.log(pw_electric_luzern["Luzern"])