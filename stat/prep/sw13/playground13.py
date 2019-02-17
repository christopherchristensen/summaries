#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 08:54:55 2019

@author: christopher
"""

import matplotlib.pyplot as plt 
import numpy as np
from pandas import DataFrame
import scipy.stats as st


d = np.random.choice(a=[-1,1], size=10000, replace=True) 

x = np.cumsum(d)
plt.plot(x)
plt.xlabel("Random Walk")
plt.ylabel("y-Abweichung in [m]") 

np.random.seed(35)

# Zufällige Schritte (links -1, rechts 1)
d = np.random.choice(a=[-1,1], size=10000, replace=True) 

# fixe Konstante (delta)
delta = 5*10**(-2)

# Cumsum
x = np.cumsum(d)
y = np.zeros(10000)

# Siehe Formel zu Schritt mit Konstante
for i in range(1,10000):
    y[i] = delta+y[i-1]+d[i]

plt.plot(y)
plt.plot(x)
plt.xlabel("Random Walk mit Drift") 
plt.ylabel("y-Abweichung in [m]")
plt.legend("mit Drift", "ohne Drift")
plt.show()



w = np.random.normal(size=10000) 
plt.plot(w)

w = DataFrame(np.random.normal(size=10000)) 
w.rolling(window=3).mean().plot() 

plt.show()

st.binom.pmf(k=1, n=1, p=0.2)

